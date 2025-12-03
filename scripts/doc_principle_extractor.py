"""Extract key principles from dbt documentation for certification exam flashcards."""

from __future__ import annotations

import json
import os
import sys
from typing import Any

import tiktoken
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel, Field

# Load environment variables
load_dotenv()


class DocumentPrinciple(BaseModel):
    """A key principle extracted from documentation."""
    principle: str = Field(default="", description="Concise principle statement")
    explanation: str = Field(default="", description="Detailed explanation")
    certification_relevance: str = Field(default="", description="Why this matters for exam")
    example: str = Field(default="", description="Code example (optional)")


class PrincipleExtraction(BaseModel):
    """Structured output containing extracted principles."""
    principles: list[DocumentPrinciple] = Field(default_factory=list)


def count_tokens(text: str, encoding_name: str = "cl100k_base") -> int:
    """Count tokens in text using tiktoken."""
    encoding = tiktoken.get_encoding(encoding_name)
    return len(encoding.encode(text))


def truncate_document(content: str, max_tokens: int = 6000, encoding_name: str = "cl100k_base") -> str:
    """Truncate document content to fit within token limit."""
    encoding = tiktoken.get_encoding(encoding_name)
    tokens = encoding.encode(content)
    
    if len(tokens) <= max_tokens:
        return content
    
    # Truncate and add note
    truncated_tokens = tokens[:max_tokens]
    truncated_text = encoding.decode(truncated_tokens)
    return f"{truncated_text}\n\n... [Document truncated to fit token limit]"


def build_system_prompt() -> str:
    """Build comprehensive system prompt for principle extraction."""
    return """You are an expert dbt Analytics Engineering instructor preparing students for the dbt Analytics Engineering Certification exam.

Your task is to extract 3-5 KEY PRINCIPLES from the provided dbt documentation that are CRITICAL for exam success.

CERTIFICATION EXAM TOPICS TO PRIORITIZE:
- Data Tests: not_null, unique, accepted_values, relationships, custom generic tests, singular tests
- Materializations: table, view, incremental (strategies: merge, append, insert_overwrite), ephemeral
- Jinja & Macros: ref(), source(), control structures (if/for), variables, custom macros, environment variables
- CLI Commands: dbt run, dbt test, dbt build, dbt seed, dbt snapshot, flags (--select, --full-refresh, --fail-fast)
- Project Configuration: dbt_project.yml, profiles.yml, model configs, vars, tags
- Sources & Seeds: source freshness, loader configuration, CSV handling
- Deployment & Jobs: environments, job scheduling, deferral, production runs
- DAG & Dependencies: model dependencies, upstream/downstream relationships, ref() logic
- Documentation: docs generate, doc blocks, descriptions, lineage
- Snapshots: SCD Type 2, timestamp vs check strategy
- Packages: packages.yml, dbt_utils, hub packages
- Error Handling: compilation errors, runtime errors, debugging strategies

PRINCIPLE QUALITY CRITERIA:
✓ Actionable: Students can apply it directly in their work
✓ Exam-Relevant: Likely to appear on certification questions
✓ Specific: Include commands, syntax, configuration keys
✓ Complete: Enough context to understand WHY it matters
✓ Example-Rich: Code snippets, YAML configs, CLI commands when applicable

OUTPUT REQUIREMENTS:
- Extract 3-5 principles (no more, no less)
- Each principle should be a clear, standalone concept
- Include concrete examples in code blocks when relevant
- Explain certification relevance explicitly
- Focus on what students need to KNOW, DO, and TROUBLESHOOT

Do NOT extract:
- Generic software engineering advice
- Overly basic concepts already known
- Topics not relevant to dbt certification
- Redundant or overlapping principles"""


async def extract_principles(
    document_content: str,
    document_path: str,
    model_name: str,
    max_doc_tokens: int = 6000,
) -> PrincipleExtraction:
    """
    Extract key principles from a documentation file using LLM.
    
    Args:
        document_content: Raw markdown content of the documentation
        document_path: Path to the source document (for context)
        model_name: Gemini model name
        max_doc_tokens: Maximum tokens for document content
        
    Returns:
        PrincipleExtraction with list of extracted principles
    """
    # Truncate document if needed
    truncated_content = truncate_document(document_content, max_doc_tokens)
    
    # Build prompt
    system_prompt = build_system_prompt()
    user_prompt = f"""Source Document: {document_path}

Document Content:
{truncated_content}

Extract 3-5 key principles from this documentation that are essential for the dbt Analytics Engineering Certification exam.
Focus on actionable knowledge with concrete examples.

Respond with valid JSON matching this schema:
{{
  "principles": [
    {{
      "principle": "string",
      "explanation": "string",
      "certification_relevance": "string",
      "example": "string"
    }}
  ]
}}"""
    
    full_prompt = f"{system_prompt}\n\n{user_prompt}"
    
    print(f"[debug] Sending prompt to LLM (length: {len(full_prompt)} chars)", file=sys.stderr)
    
    # Call Gemini API
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    
    response = await client.aio.models.generate_content(
        model=model_name,
        contents=full_prompt,
        config=genai.types.GenerateContentConfig(
            response_mime_type="application/json",
        ),
    )
    
    raw_response = response.text
    
    print(f"[debug] Principle extraction - response type: {type(raw_response)}", file=sys.stderr)
    print(f"[debug] Principle extraction - response preview: {str(raw_response)[:500]}", file=sys.stderr)
    
    # Parse response
    return _parse_principle_extraction(raw_response)


def _parse_principle_extraction(raw: Any) -> PrincipleExtraction:
    """Parse LLM response into PrincipleExtraction."""
    if isinstance(raw, PrincipleExtraction):
        return raw
    
    payload: dict[str, Any]
    if isinstance(raw, dict):
        payload = raw
    elif isinstance(raw, str):
        import json
        import re
        
        # The response might be properly escaped JSON as a string
        # Try direct parsing first
        try:
            payload = json.loads(raw)
            if isinstance(payload, dict) and 'principles' in payload:
                # Success!
                pass
            else:
                # Not the expected format, try to find JSON in the response
                raise ValueError("Not expected format")
        except (json.JSONDecodeError, ValueError):
            # Try to find JSON object in the response (may have extra text before/after)
            json_match = re.search(r'\{[\s\S]*"principles"[\s\S]*\}', raw)
            if not json_match:
                print("[warn] No JSON found in response", file=sys.stderr)
                print(f"[warn] Response: {raw[:500]}", file=sys.stderr)
                return PrincipleExtraction(principles=[])
            
            json_str = json_match.group(0)
            
            # Fix common JSON issues from LLM output
            # Remove any trailing commas before closing braces/brackets
            json_str = re.sub(r',(\s*[}\]])', r'\1', json_str)
            
            try:
                payload = json.loads(json_str)
            except json.JSONDecodeError as err:
                print(f"[warn] Failed to parse LLM response as JSON: {err}", file=sys.stderr)
                print(f"[warn] JSON string: {json_str[:500]}", file=sys.stderr)
                return PrincipleExtraction(principles=[])
    else:
        print(f"[warn] Unexpected LLM response type: {type(raw)}", file=sys.stderr)
        return PrincipleExtraction(principles=[])
    
    try:
        result = PrincipleExtraction.model_validate(payload)
        print(f"[debug] Successfully validated {len(result.principles)} principles", file=sys.stderr)
        return result
    except Exception as e:
        print(f"[warn] Failed to validate principle extraction: {e}", file=sys.stderr)
        print(f"[warn] Payload keys: {list(payload.keys()) if isinstance(payload, dict) else 'not a dict'}", file=sys.stderr)
        return PrincipleExtraction(principles=[])
