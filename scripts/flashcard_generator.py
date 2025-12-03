"""Generate flashcards from extracted principles for dbt certification exam."""

from __future__ import annotations

import hashlib
import os
import random
import string
import sys
import uuid
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel, Field

# Load environment variables
load_dotenv()


class GeneratedFlashcard(BaseModel):
    """A generated flashcard for study."""
    front: str = Field(default="", description="Question or prompt for the flashcard")
    back: str = Field(default="", description="Answer or explanation")
    principle_reference: str = Field(default="", description="Reference to the source principle")


class FlashcardBatch(BaseModel):
    """Batch of flashcards generated from principles."""
    flashcards: list[GeneratedFlashcard] = Field(default_factory=list)


def build_flashcard_system_prompt() -> str:
    """Build system prompt for flashcard generation."""
    return """You are an expert flashcard creator for the dbt Analytics Engineering Certification exam.

Your task is to generate EXACTLY 2 FLASHCARDS per principle provided:
1. FACTUAL/DEFINITION card: Tests recall of what something is, does, or how to use it
2. APPLICATION/SCENARIO card: Tests ability to apply knowledge in a real-world situation

FLASHCARD BEST PRACTICES:
✓ Clear, Concise Questions: 1-2 sentences, unambiguous
✓ Focused Answers: 2-4 sentences, one concept per card
✓ Code Examples: Use triple backticks for code, YAML, CLI commands
✓ Exam-Style: Mirror certification exam question patterns
✓ Actionable: Student should be able to DO something after learning

QUESTION PATTERNS TO USE:
Factual:
- "What is [concept]?"
- "How do you [action] in dbt?"
- "What command is used to [action]?"
- "What are the four built-in data tests in dbt?"
- "What configuration is required for [feature]?"

Application/Scenario:
- "You need to [goal]. How would you accomplish this in dbt?"
- "A model is failing with [error]. What's the likely cause?"
- "When should you use [option A] vs [option B]?"
- "Given this YAML configuration, what will happen?"
- "How would you troubleshoot [problem]?"

ANSWER FORMATTING:
- Start with direct answer, then elaborate
- Use code blocks with triple backticks for:
  * CLI commands: ```bash or ``` (plain)
  * YAML configs: ```yaml or ``` (plain)
  * SQL/Jinja: ```sql or ``` (plain)
- Keep answers concise but complete
- Include "why" when relevant for understanding

AVOID:
- Ambiguous questions with multiple interpretations
- Overly long answers (>6 sentences)
- Multiple concepts in one card (split them)
- Questions requiring multi-step reasoning without context
- Trivia not relevant to practical dbt usage

OUTPUT REQUIREMENTS:
- Generate EXACTLY 2 flashcards per principle
- Set principle_reference to the principle text for tracking
- Ensure each card is self-contained (can be understood alone)"""


async def generate_flashcards_from_principles(
    principles: list[dict[str, Any]],
    model_name: str,
) -> FlashcardBatch:
    """
    Generate flashcards from a batch of principles.
    
    Args:
        principles: List of principle dicts with 'principle', 'explanation', 'example' keys
        model_name: Gemini model name
        
    Returns:
        FlashcardBatch with generated flashcards
    """
    # Build prompt with all principles
    principles_text = []
    for i, p in enumerate(principles, 1):
        example_section = f"\nExample:\n{p['example']}" if p.get('example') else ""
        principles_text.append(
            f"Principle {i}:\n"
            f"Statement: {p['principle']}\n"
            f"Explanation: {p['explanation']}\n"
            f"Exam Relevance: {p['certification_relevance']}"
            f"{example_section}"
        )
    
    system_prompt = build_flashcard_system_prompt()
    user_prompt = f"""Generate EXACTLY 2 flashcards for each of the following principles:

{chr(10).join(principles_text)}

Remember:
- Card 1 per principle: Factual/definition-based question
- Card 2 per principle: Application/scenario-based question
- Use code blocks with triple backticks for commands, YAML, SQL
- Keep questions clear and answers concise

Respond with valid JSON matching this schema:
{{
  "flashcards": [
    {{
      "front": "string",
      "back": "string",
      "principle_reference": "string"
    }}
  ]
}}"""
    
    full_prompt = f"{system_prompt}\n\n{user_prompt}"
    
    print(f"[debug] Flashcard generation - prompt length: {len(full_prompt)} chars", file=sys.stderr)
    print(f"[debug] Generating flashcards for {len(principles)} principles", file=sys.stderr)
    
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
    
    print(f"[debug] Flashcard response type: {type(raw_response)}", file=sys.stderr)
    print(f"[debug] Flashcard response preview: {str(raw_response)[:500]}", file=sys.stderr)
    
    return _parse_flashcard_batch(raw_response)


def _parse_flashcard_batch(raw: Any) -> FlashcardBatch:
    """Parse LLM response into FlashcardBatch."""
    if isinstance(raw, FlashcardBatch):
        return raw
    
    payload: dict[str, Any]
    if isinstance(raw, dict):
        payload = raw
    elif isinstance(raw, str):
        import json
        import re
        
        # Try direct parsing first (for properly escaped JSON strings)
        try:
            payload = json.loads(raw)
            if isinstance(payload, dict) and 'flashcards' in payload:
                # Success!
                pass
            else:
                raise ValueError("Not expected format")
        except (json.JSONDecodeError, ValueError):
            # Try to extract JSON from string (may have extra text)
            raw_text = raw.strip()
            
            # Look for JSON object in the response
            json_match = re.search(r'\{.*\}', raw_text, re.DOTALL)
            if json_match:
                json_str = json_match.group(0)
            else:
                json_str = raw_text
            
            try:
                payload = json.loads(json_str)
            except json.JSONDecodeError as err:
                print(f"[warn] Failed to parse flashcard response as JSON: {err}", file=sys.stderr)
                print(f"[warn] Raw response preview: {raw_text[:200]}...", file=sys.stderr)
                return FlashcardBatch(flashcards=[])
    else:
        print(f"[warn] Unexpected flashcard response type: {type(raw)}", file=sys.stderr)
        return FlashcardBatch(flashcards=[])
    
    try:
        result = FlashcardBatch.model_validate(payload)
        print(f"[debug] Successfully validated {len(result.flashcards)} flashcards", file=sys.stderr)
        return result
    except Exception as e:
        print(f"[warn] Failed to validate flashcard batch: {e}", file=sys.stderr)
        print(f"[warn] Payload keys: {list(payload.keys()) if isinstance(payload, dict) else 'not a dict'}", file=sys.stderr)
        if isinstance(payload, dict) and 'flashcards' in payload:
            print(f"[warn] Flashcards in payload: {len(payload['flashcards'])} items", file=sys.stderr)
        return FlashcardBatch(flashcards=[])


def generate_flashcard_uuid(source_file: str, principle_text: str, existing_uuids: set[str]) -> tuple[str, int]:
    """
    Generate UUID5 for flashcard with collision detection.
    
    Args:
        source_file: Relative path to source documentation file
        principle_text: The principle text used as seed
        existing_uuids: Set of existing UUIDs in deck to check for collisions
        
    Returns:
        Tuple of (uuid_string, collision_count)
    """
    collisions = 0
    seed_text = f"{source_file}:{principle_text}"
    
    while True:
        # Generate UUID5 from seed text
        namespace = uuid.UUID('6ba7b810-9dad-11d1-80b4-00c04fd430c8')  # DNS namespace
        generated_uuid = str(uuid.uuid5(namespace, seed_text))
        
        if generated_uuid not in existing_uuids:
            return generated_uuid, collisions
        
        # Collision detected - append random suffix
        collisions += 1
        suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
        seed_text = f"{source_file}:{principle_text}:{suffix}"


def generate_short_guid(content: str) -> str:
    """Generate short GUID for flashcard (similar to Anki's format)."""
    hash_obj = hashlib.md5(content.encode())
    hash_hex = hash_obj.hexdigest()
    # Take first 10 chars and make it look like Anki's base62-ish format
    return hash_hex[:10]


def write_flashcard_to_deck(
    flashcard: GeneratedFlashcard,
    source_file: str,
    output_dir: Path,
    existing_uuids: set[str],
    principle_text: str,
) -> tuple[str, int]:
    """
    Write a flashcard to the deck directory.
    
    Args:
        flashcard: The flashcard to write
        source_file: Relative path to source documentation
        output_dir: Output directory (deck/)
        existing_uuids: Set of existing UUIDs for collision detection
        principle_text: Principle text for UUID generation
        
    Returns:
        Tuple of (uuid, collision_count)
    """
    # Generate UUID with collision handling
    card_uuid, collisions = generate_flashcard_uuid(source_file, principle_text, existing_uuids)
    existing_uuids.add(card_uuid)
    
    # Generate short GUID
    guid = generate_short_guid(f"{flashcard.front}:{flashcard.back}")
    
    # Build YAML frontmatter (sorted alphabetically for stable diffs)
    frontmatter = {
        'citations': [source_file],
        'guid': guid,
        'source': 'llm',
        'uuid': card_uuid,
    }
    
    # Build flashcard content
    content = f"""---
{yaml.dump(frontmatter, default_flow_style=False, sort_keys=False)}---

<front>

{flashcard.front}

</front>

---

<back>

{flashcard.back}

</back>
"""
    
    # Write to file
    output_file = output_dir / f"{card_uuid}.md"
    output_file.write_text(content)
    
    return card_uuid, collisions
