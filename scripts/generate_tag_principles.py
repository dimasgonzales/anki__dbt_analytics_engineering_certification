#!/usr/bin/env python3
# /// script
# dependencies = [
#   "openai>=1.0.0",
#   "pydantic>=2.7.0",
#   "python-dotenv>=1.0.0",
#   "tiktoken>=0.5.0",
#   "pyyaml>=6.0",
# ]
# ///
"""
Extract key principles for each tag from existing flashcards.

This script:
1. Loads tags.json and all flashcards.
2. Groups flashcards by tag.
3. For each tag, aggregates flashcard content.
4. Uses LLM to identify 3-5 Key Principles that these cards test.
5. Saves the result to tag_principles.json.
"""

import argparse
import asyncio
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List

import tiktoken
from dotenv import load_dotenv
from openai import AsyncOpenAI
from pydantic import BaseModel, Field

# Load environment variables
load_dotenv()

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

# --- Data Models ---

class TagPrinciple(BaseModel):
    """A key principle identified for a specific tag."""
    principle: str = Field(..., description="Concise statement of the principle")
    description: str = Field(..., description="Explanation of what this principle covers")
    key_concepts: List[str] = Field(..., description="List of specific concepts/keywords involved")

class TagPrinciplesResult(BaseModel):
    """Container for principles extracted for a tag."""
    tag: str
    principles: List[TagPrinciple]

# --- Helper Functions ---

def load_tags(tags_path: Path) -> List[Dict[str, Any]]:
    with open(tags_path) as f:
        return json.load(f)

def load_flashcards(deck_dir: Path) -> List[Dict[str, Any]]:
    cards = []
    for f in deck_dir.glob("*.md"):
        try:
            content = f.read_text()
            # Simple parsing to find tags
            # We assume tags are in frontmatter
            import yaml
            import re
            # Fix regex to handle empty frontmatter or no newline before closing ---
            match = re.match(r'^---\n(.*?)---\n(.*)$', content, re.DOTALL)
            if match:
                fm_text = match.group(1)
                body = match.group(2)
                
                try:
                    frontmatter = yaml.safe_load(fm_text)
                except yaml.YAMLError as e:
                    print(f"Warning: YAML error in {f.name}: {e}", file=sys.stderr)
                    frontmatter = {}
                
                if frontmatter is None:
                    frontmatter = {}

                # Extract front/back for content analysis
                front_match = re.search(r'<front>(.*?)</front>', body, re.DOTALL)
                back_match = re.search(r'<back>(.*?)</back>', body, re.DOTALL)
                
                front = front_match.group(1).strip() if front_match else ""
                back = back_match.group(1).strip() if back_match else ""
                
                cards.append({
                    "path": f,
                    "tags": frontmatter.get("tags", []),
                    "content": f"Q: {front}\nA: {back}"
                })
        except Exception as e:
            print(f"Error loading {f.name}: {e}", file=sys.stderr)
    return cards

def count_tokens(text: str, encoding_name: str = "cl100k_base") -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    return len(encoding.encode(text))

# --- LLM Logic ---

async def extract_principles_for_tag(
    tag: str,
    tag_description: str,
    cards_content: List[str],
    model_name: str,
    api_key: str
) -> TagPrinciplesResult:
    
    # Aggregate content (truncate if too large)
    full_text = "\n\n---\n\n".join(cards_content)
    max_tokens = 8000 # Reduced limit for speed/safety
    if count_tokens(full_text) > max_tokens:
        # Simple truncation
        encoding = tiktoken.get_encoding("cl100k_base")
        tokens = encoding.encode(full_text)
        full_text = encoding.decode(tokens[:max_tokens]) + "\n...[truncated]"

    client = AsyncOpenAI(api_key=api_key, base_url="https://api.deepseek.com", timeout=60.0)
    
    system_prompt = f"""
    You are analyzing a set of flashcards for the dbt Analytics Engineering Certification.
    Tag: {tag}
    Tag Description: {tag_description}
    
    Task:
    Identify 3-5 KEY PRINCIPLES that these flashcards are testing.
    Abstract the specific questions into broader principles that a student needs to master.
    
    Respond ONLY with valid JSON matching this schema:
    {{
        "tag": "{tag}",
        "principles": [
            {{
                "principle": "string (Concise statement)",
                "description": "string (Detailed explanation)",
                "key_concepts": ["string", "string"]
            }}
        ]
    }}
    """
    
    user_prompt = f"""
    Flashcards Content:
    {full_text}
    """
    
    try:
        response = await client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            response_format={"type": "json_object"},
            temperature=0.3
        )
        
        # Parse response
        import json
        data = json.loads(response.choices[0].message.content)
        return TagPrinciplesResult(**data)
        
    except Exception as e:
        print(f"Error extracting principles for tag '{tag}': {e}", file=sys.stderr)
        return TagPrinciplesResult(tag=tag, principles=[])

# --- Main ---

async def main_async():
    parser = argparse.ArgumentParser(description="Generate principles for tags.")
    parser.add_argument("--tags-file", type=Path, default=Path("tags.json"))
    parser.add_argument("--deck-dir", type=Path, default=Path("deck"))
    parser.add_argument("--output-file", type=Path, default=Path("tag_principles.json"))
    parser.add_argument("--model", default="deepseek-chat")
    parser.add_argument("--limit-tags", type=int, help="Limit number of tags to process (for testing)")
    parser.add_argument("--concurrency", type=int, default=5, help="Max concurrent tags to process")
    
    args = parser.parse_args()
    
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        print("Error: DEEPSEEK_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    print(f"Loading tags from {args.tags_file}...")
    tags = load_tags(args.tags_file)
    
    print(f"Loading flashcards from {args.deck_dir}...")
    cards = load_flashcards(args.deck_dir)
    print(f"Loaded {len(cards)} cards.")
    
    # Group cards by tag
    cards_by_tag = {t['child_tag']: [] for t in tags}
    for card in cards:
        for t in card['tags']:
            if t in cards_by_tag:
                cards_by_tag[t].append(card['content'])
    
    # Process tags
    results = {}
    processed_count = 0
    
    tags_to_process = [t for t in tags if cards_by_tag[t['child_tag']]]
    if args.limit_tags:
        tags_to_process = tags_to_process[:args.limit_tags]
        
    print(f"Processing {len(tags_to_process)} tags with associated cards...")
    
    semaphore = asyncio.Semaphore(args.concurrency)
    
    async def process_tag(tag_def):
        async with semaphore:
            tag_name = tag_def['child_tag']
            content = cards_by_tag[tag_name]
            
            print(f"Extracting principles for '{tag_name}' ({len(content)} cards)...")
            
            res = await extract_principles_for_tag(
                tag=tag_name,
                tag_description=tag_def['description'],
                cards_content=content,
                model_name=args.model,
                api_key=api_key
            )
            return tag_name, res

    tasks = [process_tag(t) for t in tags_to_process]
    batch_results = await asyncio.gather(*tasks)
    
    for tag_name, res in batch_results:
        if res.principles:
            results[tag_name] = [p.model_dump() for p in res.principles]
            processed_count += 1

    print(f"Saving results to {args.output_file}...")
    with open(args.output_file, 'w') as f:
        json.dump(results, f, indent=2)
        
    print(f"Done. Processed {processed_count} tags.")

def main():
    asyncio.run(main_async())

if __name__ == "__main__":
    main()
