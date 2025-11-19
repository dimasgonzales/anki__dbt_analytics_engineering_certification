#!/usr/bin/env python3
# /// script
# dependencies = [
#   "pyyaml>=6.0.1",
#   "openai>=1.0.0",
#   "outlines>=0.0.42",
#   "pydantic>=2.7.0",
# ]
# ///
"""
Automatically assign tags to flashcards based on content analysis.

Supports three strategies:
- keyword: Fast keyword matching against tags.json keywords
- llm: Semantic understanding using local LLM (OpenAI-compatible API)
- hybrid: Keyword first, fall back to LLM for low-confidence matches
"""

import argparse
import asyncio
import json
import re
import sys
import time
from pathlib import Path
from typing import Any

import yaml
from pydantic import ValidationError

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

try:  # When executed as part of the scripts package
    from .llm_structured import generate_tag_batch
except ImportError:  # When executed directly via uv run scripts/auto_tagger.py
    from llm_structured import generate_tag_batch


def load_tags(tags_path: Path) -> list[dict[str, Any]]:
    """Load tag definitions from tags.json."""
    with open(tags_path) as f:
        return json.load(f)


def load_flashcard(card_path: Path) -> dict[str, Any]:
    """Parse flashcard markdown file and extract frontmatter + content."""
    content = card_path.read_text()
    
    # Extract YAML frontmatter
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if not match:
        raise ValueError(f"Invalid flashcard format: {card_path}")
    
    frontmatter = yaml.safe_load(match.group(1))
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


def keyword_score_tags(
    flashcard: dict[str, Any],
    tags: list[dict[str, Any]],
    max_tags: int = 3
) -> list[tuple[str, float, str]]:
    """
    Score tags based on keyword matching.
    
    Returns list of (child_tag, score, reason) tuples sorted by score descending.
    Normalizes scores by keyword count to avoid bias toward tags with more keywords.
    """
    content = (flashcard['front'] + ' ' + flashcard['back']).lower()
    scores = []
    
    for tag in tags:
        child_tag = tag['child_tag']
        keywords = tag['keywords']
        
        # Count keyword matches
        matches = sum(1 for kw in keywords if kw.lower() in content)
        
        # Normalize by keyword count to avoid bias
        # Add small bonus for multiple matches
        if matches > 0:
            normalized_score = (matches / len(keywords)) + (matches * 0.1)
            matched_kws = [kw for kw in keywords if kw.lower() in content]
            reason = f"Keywords: {', '.join(matched_kws[:3])}"
            scores.append((child_tag, normalized_score, reason))
    
    # Sort by score descending and return top N
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:max_tags]


def prefilter_tags(
    flashcard: dict[str, Any],
    tags: list[dict[str, Any]],
    min_tags: int = 10
) -> list[dict[str, Any]]:
    """Pre-filter tags by keyword matching to reduce prompt size."""
    content = (flashcard['front'] + ' ' + flashcard['back']).lower()
    relevant = []
    
    for tag in tags:
        if any(kw.lower() in content for kw in tag['keywords']):
            relevant.append(tag)
    
    # If too few matches, use all tags
    return relevant if len(relevant) >= min_tags else tags


async def llm_score_tags_batch(
    flashcards: list[dict[str, Any]],
    tags: list[dict[str, Any]],
    tag_list: str,
    llm_url: str,
    *,
    max_tags: int = 3,
    retry_count: int = 3,
    model_name: str | None = None,
) -> dict[Path, list[tuple[str, float, str]]]:
    """Score tags for a single batch using structured LLM output."""

    cards_text = []
    for i, card in enumerate(flashcards, start=1):
        cards_text.append(
            f"Card {i}:\n"
            f"Question: {card['front']}\n"
            f"Answer: {card['back']}\n"
        )

    prompt = f"""You are a dbt Analytics Engineering expert. Assign up to {max_tags} child_tags to each flashcard.

Available tags:
{tag_list}

Flashcards:
{''.join(cards_text)}

Instructions:
- Use child_tag names exactly as listed.
- Provide confidence between 0 and 1 and a short reason for every tag.
- card_index must match the card number above (starting at 1).
"""

    for retry in range(retry_count):
        try:
            structured = await generate_tag_batch(
                prompt,
                llm_url=llm_url,
                model_name=model_name or "qwen/qwen3-coder-30b",
            )

            output: dict[Path, list[tuple[str, float, str]]] = {}
            for card_result in structured.cards:
                idx = card_result.card_index - 1
                if 0 <= idx < len(flashcards):
                    card_path = flashcards[idx]['path']
                    tag_tuples = [
                        (tag.tag, float(tag.confidence), tag.reason)
                        for tag in card_result.tags[:max_tags]
                    ]
                    output[card_path] = tag_tuples

            return output

        except (ValidationError, Exception) as e:
            if retry == retry_count - 1:
                print(f"LLM structured output error after {retry_count} retries: {e}", file=sys.stderr)
                return {card['path']: [] for card in flashcards}

            backoff = 2 ** retry
            print(f"Retry {retry+1}/{retry_count} after {backoff}s due to: {e}", file=sys.stderr)
            await asyncio.sleep(backoff)

    return {card['path']: [] for card in flashcards}


async def llm_score_tags(
    flashcards: list[dict[str, Any]],
    tags: list[dict[str, Any]],
    llm_url: str,
    *,
    max_tags: int = 3,
    batch_size: int = 10,
    max_concurrent: int = 3,
    model_name: str | None = None,
    retry_count: int = 3,
) -> dict[Path, list[tuple[str, float, str]]]:
    """
    Score tags using LLM with parallel batch processing.
    
    Processes multiple batches concurrently for better throughput.
    Returns dict mapping card_path -> list of (child_tag, score, reason) tuples.
    """
    # Build tag list once (shared across all batches)
    tag_descriptions = []
    for tag in tags:
        tag_descriptions.append(
            f"- {tag['child_tag']}: {tag['description']}"
        )
    tag_list = '\n'.join(tag_descriptions)
    
    # Split into batches
    batches = [flashcards[i:i+batch_size] for i in range(0, len(flashcards), batch_size)]
    
    # Process batches with concurrency limit
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def bounded_process(batch_idx: int, batch: list[dict[str, Any]]):
        async with semaphore:
            start_time = time.time()
            result = await llm_score_tags_batch(
                batch,
                tags,
                tag_list,
                llm_url,
                max_tags=max_tags,
                retry_count=retry_count,
                model_name=model_name,
            )
            elapsed = time.time() - start_time
            print(f"Batch {batch_idx+1}/{len(batches)} completed in {elapsed:.1f}s ({elapsed/len(batch):.2f}s per card)")
            return result
    
    # Process all batches in parallel (with semaphore limiting concurrency)
    batch_results = await asyncio.gather(
        *[bounded_process(i, batch) for i, batch in enumerate(batches)]
    )
    
    # Merge results from all batches
    output = {}
    for batch_result in batch_results:
        output.update(batch_result)
    
    return output


async def hybrid_score_tags(
    flashcard: dict[str, Any],
    tags: list[dict[str, Any]],
    llm_url: str,
    threshold: float,
    max_tags: int = 3,
    batch_size: int = 10,
    model_name: str | None = None,
) -> tuple[list[tuple[str, float, str]], str]:
    """
    Hybrid approach: keyword first, LLM fallback for low confidence.
    
    Returns (tag_list, strategy_used).
    """
    # Try keyword matching first
    keyword_results = keyword_score_tags(flashcard, tags, max_tags)
    
    # Check if we have confident results
    if keyword_results and keyword_results[0][1] >= threshold:
        return keyword_results, "keyword"
    
    # Fall back to LLM (single card batch)
    llm_results = await llm_score_tags(
        [flashcard],
        tags,
        llm_url,
        max_tags=max_tags,
        batch_size=1,
        max_concurrent=1,
        model_name=model_name,
    )
    return llm_results.get(flashcard['path'], []), "llm"


def update_flashcard_tags(
    card_path: Path,
    tags: list[str],
    dry_run: bool = False
) -> None:
    """Add or update tags field in flashcard frontmatter."""
    content = card_path.read_text()
    
    # Extract frontmatter and body
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if not match:
        raise ValueError(f"Invalid flashcard format: {card_path}")
    
    frontmatter = yaml.safe_load(match.group(1))
    body = match.group(2)
    
    # Update or add tags
    frontmatter['tags'] = tags
    
    # Reconstruct file
    new_content = f"---\n{yaml.dump(frontmatter, default_flow_style=False, sort_keys=False)}---\n{body}"
    
    if dry_run:
        print(f"\n[DRY RUN] Would update {card_path.name}:")
        print(f"  Tags: {tags}")
    else:
        card_path.write_text(new_content)


def main():
    parser = argparse.ArgumentParser(
        description="Auto-assign tags to flashcards based on content analysis"
    )
    parser.add_argument(
        '--strategy',
        choices=['keyword', 'llm', 'hybrid'],
        default='hybrid',
        help='Tagging strategy (default: hybrid)'
    )
    parser.add_argument(
        '--threshold',
        type=float,
        default=0.3,
        help='Confidence threshold for hybrid mode (default: 0.3)'
    )
    parser.add_argument(
        '--max-tags',
        type=int,
        default=3,
        help='Maximum number of tags per card (default: 3)'
    )
    parser.add_argument(
        '--batch-size',
        type=int,
        default=10,
        help='Number of cards per LLM API call (default: 10)'
    )
    parser.add_argument(
        '--max-concurrent',
        type=int,
        default=3,
        help='Maximum concurrent LLM batch requests (default: 3)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview changes without modifying files'
    )
    parser.add_argument(
        '--deck-dir',
        type=Path,
        default=Path('deck'),
        help='Path to deck directory (default: deck/)'
    )
    parser.add_argument(
        '--tags-file',
        type=Path,
        default=Path('tags.json'),
        help='Path to tags.json (default: tags.json)'
    )
    parser.add_argument(
        '--llm-url',
        type=str,
        default='http://127.0.0.1:1234/v1',
        help='OpenAI-compatible API base URL (default: http://127.0.0.1:1234/v1)'
    )
    parser.add_argument(
        '--llm-model',
        type=str,
        default='qwen/qwen3-coder-30b',
        help='LLM model name to use for llm/hybrid strategies'
    )
    
    args = parser.parse_args()
    
    # Load tags
    if not args.tags_file.exists():
        print(f"Error: {args.tags_file} not found", file=sys.stderr)
        return 1
    
    tags = load_tags(args.tags_file)
    print(f"Loaded {len(tags)} tags from {args.tags_file}")
    
    if args.strategy in ('llm', 'hybrid'):
        print(f"LLM endpoint: {args.llm_url}")
        print(f"Batch size: {args.batch_size}, Max concurrent: {args.max_concurrent}")
    
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
    
    print(f"Successfully loaded {len(flashcards)} flashcards\n")
    
    # Process based on strategy
    stats = {
        'total': len(flashcards),
        'tagged': 0,
        'keyword': 0,
        'llm': 0,
        'failed': 0,
    }
    
    if args.strategy == 'keyword':
        print("Using keyword matching strategy...")
        for card in flashcards:
            try:
                results = keyword_score_tags(card, tags, args.max_tags)
                if results:
                    tag_names = [r[0] for r in results]
                    update_flashcard_tags(card['path'], tag_names, args.dry_run)
                    stats['tagged'] += 1
                    stats['keyword'] += 1
                    
                    if args.dry_run:
                        for tag, score, reason in results:
                            print(f"    {tag} (score: {score:.2f}) - {reason}")
            except Exception as e:
                print(f"Error processing {card['path'].name}: {e}", file=sys.stderr)
                stats['failed'] += 1
    
    elif args.strategy == 'llm':
        print(f"Using LLM strategy (batch size: {args.batch_size}, concurrent: {args.max_concurrent})...")
        start_time = time.time()
        
        try:
            # Process all flashcards with parallel batching
            results = asyncio.run(llm_score_tags(
                flashcards,
                tags,
                args.llm_url,
                max_tags=args.max_tags,
                batch_size=args.batch_size,
                max_concurrent=args.max_concurrent,
                model_name=args.llm_model,
            ))
            
            for card in flashcards:
                card_results = results.get(card['path'], [])
                if card_results:
                    tag_names = [r[0] for r in card_results]
                    update_flashcard_tags(card['path'], tag_names, args.dry_run)
                    stats['tagged'] += 1
                    stats['llm'] += 1
                    
                    if args.dry_run:
                        print(f"\n[DRY RUN] Would update {card['path'].name}:")
                        print(f"  Tags: {tag_names}")
                        for tag, conf, reason in card_results:
                            print(f"    {tag} (conf: {conf:.2f}) - {reason}")
                else:
                    stats['failed'] += 1
        
        except Exception as e:
            print(f"Error processing flashcards: {e}", file=sys.stderr)
            stats['failed'] = len(flashcards)
        
        elapsed = time.time() - start_time
        print(f"\nTotal processing time: {elapsed:.1f}s ({elapsed/len(flashcards):.2f}s per card)")
    
    elif args.strategy == 'hybrid':
        print(f"Using hybrid strategy (threshold: {args.threshold})...")
        start_time = time.time()
        
        async def process_all_hybrid():
            tasks = []
            for card in flashcards:
                tasks.append(
                    hybrid_score_tags(
                        card,
                        tags,
                        args.llm_url,
                        args.threshold,
                        args.max_tags,
                        args.batch_size,
                        model_name=args.llm_model,
                    )
                )
            return await asyncio.gather(*tasks, return_exceptions=True)
        
        try:
            all_results = asyncio.run(process_all_hybrid())
            
            for card, result in zip(flashcards, all_results):
                if isinstance(result, Exception):
                    print(f"Error processing {card['path'].name}: {result}", file=sys.stderr)
                    stats['failed'] += 1
                    continue
                
                results, strategy = result
                
                if results:
                    tag_names = [r[0] for r in results]
                    update_flashcard_tags(card['path'], tag_names, args.dry_run)
                    stats['tagged'] += 1
                    stats[strategy] += 1
                    
                    if args.dry_run:
                        print(f"\n[DRY RUN] Would update {card['path'].name}:")
                        print(f"  Strategy: {strategy}")
                        print(f"  Tags: {tag_names}")
                        for tag, score, reason in results:
                            print(f"    {tag} (score: {score:.2f}) - {reason}")
                else:
                    stats['failed'] += 1
        
        except Exception as e:
            print(f"Error in hybrid processing: {e}", file=sys.stderr)
            stats['failed'] = len(flashcards)
        
        elapsed = time.time() - start_time
        print(f"\nTotal processing time: {elapsed:.1f}s ({elapsed/len(flashcards):.2f}s per card)")
    
    # Print summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Total flashcards: {stats['total']}")
    print(f"Successfully tagged: {stats['tagged']}")
    if args.strategy == 'hybrid':
        print(f"  - Via keyword: {stats['keyword']}")
        print(f"  - Via LLM: {stats['llm']}")
    print(f"Failed: {stats['failed']}")
    
    if args.dry_run:
        print("\n[DRY RUN] No files were modified. Run without --dry-run to apply changes.")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
