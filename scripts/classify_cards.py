#!/usr/bin/env python3
# /// script
# dependencies = [
#   "google-genai",
#   "openai>=1.0.0",
#   "pydantic",
#   "python-dotenv",
#   "pyyaml",
# ]
# ///
"""
Automatically classify flashcards as 'Factual' or 'Scenario' using an LLM.
"""

import argparse
import asyncio
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv
from pydantic import ValidationError

# Load environment variables from .env file
load_dotenv()

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

try:  # When executed as part of the scripts package
    from .llm_structured import classify_card_batch
except ImportError:  # When executed directly via uv run scripts/classify_cards.py
    from llm_structured import classify_card_batch


def load_flashcard(card_path: Path) -> dict[str, Any]:
    """Parse flashcard markdown file and extract frontmatter + content."""
    content = card_path.read_text()
    
    # Extract YAML frontmatter
    match = re.match(r'^---\n(.*?)---\n(.*)$', content, re.DOTALL)
    if not match:
        raise ValueError(f"Invalid flashcard format: {card_path}")
    
    try:
        frontmatter = yaml.safe_load(match.group(1))
    except yaml.YAMLError as e:
        print(f"Warning: YAML error in {card_path}: {e}", file=sys.stderr)
        frontmatter = {}
        
    if frontmatter is None:
        frontmatter = {}
        
    body = match.group(2)
    
    # Extract front and back sections
    front_match = re.search(r'<front>(.*?)</front>', body, re.DOTALL)
    back_match = re.search(r'<back>(.*?)</back>', body, re.DOTALL)
    
    return {
        'path': card_path,
        'frontmatter': frontmatter,
        'front': front_match.group(1).strip() if front_match else '',
        'back': back_match.group(1).strip() if back_match else '',
        'body': body,
    }


async def llm_classify_batch(
    flashcards: list[dict[str, Any]],
    *,
    retry_count: int = 3,
    model_name: str | None = None,
    api_key: str | None = None,
    cache: dict[str, Any] | None = None,
) -> dict[Path, dict[str, Any]]:
    """Classify a batch of flashcards."""

    cards_text = []
    for i, card in enumerate(flashcards, start=1):
        cards_text.append(
            f"Card {i}:\n"
            f"Question: {card['front']}\n"
            f"Answer: {card['back']}\n"
        )

    prompt = f"""You are a dbt Analytics Engineering expert. 
Classify each flashcard as 'Factual' (tests definition/fact) or 'Scenario' (tests application/situation).

Flashcards:
{''.join(cards_text)}

Instructions:
- card_type must be 'Factual' or 'Scenario'.
- Provide confidence between 0 and 1 and a short reason for the classification.
- card_index must match the card number above (starting at 1).
"""

    # Check cache
    prompt_hash = hashlib.sha256(prompt.encode('utf-8')).hexdigest()
    cache_key = f"{model_name}:{prompt_hash}"
    if cache is not None and cache_key in cache:
        # print("Cache hit!")
        try:
            # We need to reconstruct the output format from cached data
            # The cache stores the raw structured response or the parsed dict?
            # Let's store the parsed dict for simplicity
            cached_data = cache[cache_key]
            # We need to map back to paths. The order should be deterministic if batch is same.
            output = {}
            for i, card_data in enumerate(cached_data):
                if i < len(flashcards):
                    output[flashcards[i]['path']] = card_data
            return output
        except Exception as e:
            print(f"Cache read error: {e}", file=sys.stderr)

    for retry in range(retry_count):
        try:
            structured = await classify_card_batch(
                prompt,
                model_name=model_name,
                api_key=api_key,
            )

            output: dict[Path, dict[str, Any]] = {}
            cached_list = []
            
            for card_result in structured.cards:
                idx = card_result.card_index - 1
                if 0 <= idx < len(flashcards):
                    card_path = flashcards[idx]['path']
                    result_data = {
                        "card_type": card_result.card_type,
                        "confidence": card_result.confidence,
                        "reason": card_result.reason
                    }
                    output[card_path] = result_data
                    # We need to store results in order of cards for cache to work
                    # But structured.cards might be out of order?
                    # Actually, we should build a list of results matching input flashcards
            
            # Reconstruct list for cache
            for i, card in enumerate(flashcards):
                if card['path'] in output:
                    cached_list.append(output[card['path']])
                else:
                    cached_list.append({}) # Failed or missing

            if cache is not None:
                cache[cache_key] = cached_list

            return output

        except (ValidationError, Exception) as e:
            if retry == retry_count - 1:
                print(f"LLM structured output error after {retry_count} retries: {e}", file=sys.stderr)
                return {card['path']: {} for card in flashcards}

            backoff = 2 ** retry
            print(f"Retry {retry+1}/{retry_count} after {backoff}s due to: {e}", file=sys.stderr)
            await asyncio.sleep(backoff)

    return {card['path']: {} for card in flashcards}


async def llm_classify_cards(
    flashcards: list[dict[str, Any]],
    *,
    batch_size: int = 10,
    max_concurrent: int = 3,
    model_name: str | None = None,
    retry_count: int = 3,
    api_key: str | None = None,
    cache: dict[str, Any] | None = None,
) -> dict[Path, dict[str, Any]]:
    """
    Classify cards using LLM with parallel batch processing.
    """
    # Split into batches
    batches = [flashcards[i:i+batch_size] for i in range(0, len(flashcards), batch_size)]
    
    # Process batches with concurrency limit
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def bounded_process(batch_idx: int, batch: list[dict[str, Any]]):
        async with semaphore:
            start_time = time.time()
            result = await llm_classify_batch(
                batch,
                retry_count=retry_count,
                model_name=model_name,
                api_key=api_key,
                cache=cache,
            )
            elapsed = time.time() - start_time
            print(f"Batch {batch_idx+1}/{len(batches)} completed in {elapsed:.1f}s ({elapsed/len(batch):.2f}s per card)")
            return result
    
    # Process all batches in parallel
    batch_results = await asyncio.gather(
        *[bounded_process(i, batch) for i, batch in enumerate(batches)]
    )
    
    # Merge results
    output = {}
    for batch_result in batch_results:
        output.update(batch_result)
    
    return output


def update_flashcard_classification(
    card_path: Path,
    card_type: str,
    dry_run: bool = False
) -> None:
    """Update card_type in flashcard frontmatter as a tag."""
    # Convert to tag format: card_type/factual or card_type/scenario
    tag_name = f"card_type/{card_type.lower()}"
    
    with open(card_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    in_frontmatter = False
    frontmatter_count = 0
    tags_found = False
    tags_indent = ""
    
    # First pass: read lines and identify where to insert/modify
    # We need to:
    # 1. Remove existing 'card_type: ...' lines in frontmatter
    # 2. Find 'tags:' section
    # 3. Add our tag if missing
    
    # Let's do a single pass to filter out old property and find tags
    processed_lines = []
    existing_tags = set()
    tags_line_index = -1
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        if stripped == '---':
            frontmatter_count += 1
            if frontmatter_count == 1:
                in_frontmatter = True
            elif frontmatter_count == 2:
                in_frontmatter = False
            processed_lines.append(line)
            continue
            
        if in_frontmatter:
            # Remove old property
            if stripped.startswith('card_type:'):
                continue
                
            # Check for tags start
            if stripped.startswith('tags:'):
                tags_found = True
                tags_line_index = len(processed_lines)
                processed_lines.append(line)
                continue
            
            # Check for existing tags (list items)
            if tags_found and stripped.startswith('- '):
                # We are inside tags list (assuming indentation matches or it's just the next lines)
                # A simple heuristic: if it starts with dash, it's a list item.
                # We should check if this specific tag already exists
                current_tag = stripped[2:].strip()
                existing_tags.add(current_tag)
                
                # If we find a conflicting card_type tag, we might want to remove it?
                # The user request implies we should set the correct one.
                # If we are setting 'factual', and 'scenario' exists, we should probably remove 'scenario'.
                if current_tag.startswith('card_type/') and current_tag != tag_name:
                    continue # Remove conflicting tag
                
                processed_lines.append(line)
                continue
            
            # If we hit something else and we were in tags, we are done with tags
            if tags_found and not stripped.startswith('- ') and stripped:
                tags_found = False
            
            processed_lines.append(line)
        else:
            processed_lines.append(line)

    # Now we need to insert the tag if it's not there
    if tag_name not in existing_tags:
        if tags_line_index != -1:
            # Tags section exists, append to it
            # We need to know the indentation. Usually 2 spaces.
            # Let's peek at the next line after tags: if it exists and starts with dash
            indent = "  " # Default
            if tags_line_index + 1 < len(processed_lines):
                next_line = processed_lines[tags_line_index + 1]
                if next_line.strip().startswith('- '):
                    indent = next_line[:next_line.find('- ')]
            
            processed_lines.insert(tags_line_index + 1, f"{indent}- {tag_name}\n")
        else:
            # No tags section, insert it before the second '---'
            # Find the second '---'
            second_dash_index = -1
            fm_count = 0
            for i, line in enumerate(processed_lines):
                if line.strip() == '---':
                    fm_count += 1
                    if fm_count == 2:
                        second_dash_index = i
                        break
            
            if second_dash_index != -1:
                processed_lines.insert(second_dash_index, "tags:\n")
                processed_lines.insert(second_dash_index + 1, f"  - {tag_name}\n")

    if dry_run:
        print(f"\n[DRY RUN] Would update {card_path.name}:")
        print(f"  Tag: {tag_name}")
    else:
        with open(card_path, 'w', encoding='utf-8') as f:
            f.writelines(processed_lines)


def main():
    parser = argparse.ArgumentParser(
        description="Auto-classify flashcards as Factual or Scenario"
    )
    parser.add_argument(
        '--batch-size',
        type=int,
        default=10,
        help='Number of cards per LLM API call (default: 10)'
    )
    parser.add_argument(
        '--force',
        action='store_true',
        help='Force re-classification of all cards'
    )
    parser.add_argument(
        '--max-concurrent',
        type=int,
        default=3,
        help='Maximum concurrent LLM batch requests (default: 3)'
    )
    parser.add_argument(
        '--apply',
        action='store_true',
        dest='no_dry_run',
        help='Apply changes to files (default is dry-run)'
    )
    parser.add_argument(
        '--deck-dir',
        type=Path,
        default=Path('deck'),
        help='Path to deck directory (default: deck/)'
    )
    parser.add_argument(
        '--llm-model',
        type=str,
        default='deepseek-chat',
        help='LLM model name (default: deepseek-chat)'
    )
    parser.add_argument(
        '--gemini-api-key',
        type=str,
        default=None,
        help='DeepSeek API key (defaults to DEEPSEEK_API_KEY environment variable)'
    )
    
    args = parser.parse_args()
    args.dry_run = not args.no_dry_run
    
    # Get API key
    api_key = args.gemini_api_key or os.environ.get('DEEPSEEK_API_KEY')
    if not api_key:
        print("Error: DeepSeek API key required", file=sys.stderr)
        print("Set DEEPSEEK_API_KEY environment variable or use --gemini-api-key", file=sys.stderr)
        return 1
    
    # Find all flashcard files
    if not args.deck_dir.exists():
        print(f"Error: {args.deck_dir} not found", file=sys.stderr)
        return 1
    
    card_files = sorted(args.deck_dir.glob('*.md'))
    print(f"Found {len(card_files)} flashcards in {args.deck_dir}/")
    
    # Load all flashcards
    flashcards = []
    for card_file in card_files:
        try:
            flashcards.append(load_flashcard(card_file))
        except Exception as e:
            print(f"Warning: Failed to load {card_file.name}: {e}", file=sys.stderr)
    
    print(f"Successfully loaded {len(flashcards)} flashcards")
    
    original_count = len(flashcards)
    
    # Filter out already classified cards
    if not args.force:
        cards_to_process = []
        skipped_count = 0
        for card in flashcards:
            tags = card.get('frontmatter', {}).get('tags', [])
            if any(t in tags for t in ['card_type/factual', 'card_type/scenario']):
                skipped_count += 1
            else:
                cards_to_process.append(card)
        
        if skipped_count > 0:
            print(f"Skipping {skipped_count} already classified cards (use --force to re-process)")
        
        flashcards = cards_to_process
    
    if not flashcards:
        print("No cards to classify.")
        return 0

    print(f"\nClassifying {len(flashcards)} cards (batch size: {args.batch_size}, concurrent: {args.max_concurrent})...")
    start_time = time.time()
    
    stats = {
        'total': len(flashcards),
        'classified': 0,
        'failed': 0,
    }

    # Load cache
    cache_file = Path('.llm_cache.json')
    cache = {}
    if cache_file.exists():
        try:
            cache = json.loads(cache_file.read_text())
        except Exception as e:
            print(f"Warning: Failed to load cache: {e}", file=sys.stderr)

    try:
        results = asyncio.run(llm_classify_cards(
            flashcards,
            batch_size=args.batch_size,
            max_concurrent=args.max_concurrent,
            model_name=args.llm_model,
            api_key=api_key,
            cache=cache,
        ))
        
        # Save cache
        try:
            cache_file.write_text(json.dumps(cache, indent=2))
        except Exception as e:
            print(f"Warning: Failed to save cache: {e}", file=sys.stderr)
        
        for card in flashcards:
            card_data = results.get(card['path'])
            if card_data and card_data.get('card_type'):
                card_type = card_data['card_type']
                confidence = card_data.get('confidence', 0.0)
                reason = card_data.get('reason', '')
                
                update_flashcard_classification(
                    card['path'], 
                    card_type, 
                    dry_run=args.dry_run
                )
                stats['classified'] += 1
                
                if args.dry_run:
                    print(f"    {card_type} (conf: {confidence:.2f}) - {reason}")
            else:
                stats['failed'] += 1
                print(f"Failed to classify {card['path'].name}", file=sys.stderr)
    
    except Exception as e:
        print(f"Error processing flashcards: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        stats['failed'] = len(flashcards)
    
    elapsed = time.time() - start_time
    print(f"\nTotal processing time: {elapsed:.1f}s ({elapsed/len(flashcards):.2f}s per card)")
    
    # Print summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Total flashcards: {original_count}")
    if not args.force:
        print(f"Skipped (already classified): {original_count - len(flashcards)}")
    print(f"Processed: {len(flashcards)}")
    print(f"Successfully classified: {stats['classified']}")
    print(f"Failed: {stats['failed']}")
    
    if args.dry_run:
        print("\n[DRY RUN] No files were modified. Run without --dry-run to apply changes.")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
