#!/usr/bin/env python3
# /// script
# dependencies = [
#   "pyyaml>=6.0.1",
#   "openai>=1.0.0",
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
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml
from openai import OpenAI


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


def llm_score_tags(
    flashcards: list[dict[str, Any]],
    tags: list[dict[str, Any]],
    client: OpenAI,
    max_tags: int = 3
) -> dict[Path, list[tuple[str, float, str]]]:
    """
    Score tags using LLM semantic understanding.
    
    Batches multiple flashcards per API call for efficiency.
    Returns dict mapping card_path -> list of (child_tag, score, reason) tuples.
    """
    # Build tag reference for LLM
    tag_descriptions = []
    for tag in tags:
        tag_descriptions.append(
            f"- {tag['child_tag']}: {tag['description']}"
        )
    tag_list = '\n'.join(tag_descriptions)
    
    # Build batch prompt with multiple cards
    cards_text = []
    for i, card in enumerate(flashcards):
        cards_text.append(
            f"Card {i+1}:\n"
            f"Question: {card['front']}\n"
            f"Answer: {card['back']}\n"
        )
    
    prompt = f"""You are a dbt Analytics Engineering expert. Assign the most relevant tags to each flashcard.

Available tags:
{tag_list}

Flashcards:
{chr(10).join(cards_text)}

For each card, return the top {max_tags} most relevant tags (use child_tag names only).
Consider:
1. Primary concept (what is the card mainly about?)
2. Secondary concepts (what supporting topics are mentioned?)
3. Use tag descriptions to understand semantic relationships

Return ONLY valid JSON (no markdown):
{{
  "cards": [
    {{
      "card_index": 1,
      "tags": [
        {{"tag": "child_tag_name", "confidence": 0.95, "reason": "brief explanation"}},
        ...
      ]
    }},
    ...
  ]
}}"""

    try:
        response = client.chat.completions.create(
            model="qwen3-next-80b-a3b-instruct",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_tokens=2000,
        )
        
        # Parse JSON response
        response_text = response.choices[0].message.content.strip()
        # Remove markdown code blocks if present
        response_text = re.sub(r'^```json\s*\n?', '', response_text)
        response_text = re.sub(r'\n?```\s*$', '', response_text)
        
        result = json.loads(response_text)
        
        # Map results back to flashcards
        output = {}
        for card_result in result.get('cards', []):
            idx = card_result['card_index'] - 1
            if 0 <= idx < len(flashcards):
                card_path = flashcards[idx]['path']
                tag_tuples = [
                    (t['tag'], t['confidence'], t['reason'])
                    for t in card_result.get('tags', [])
                ]
                output[card_path] = tag_tuples
        
        return output
    
    except Exception as e:
        print(f"LLM API error: {e}", file=sys.stderr)
        # Return empty results for all cards
        return {card['path']: [] for card in flashcards}


def hybrid_score_tags(
    flashcard: dict[str, Any],
    tags: list[dict[str, Any]],
    client: OpenAI,
    threshold: float,
    max_tags: int = 3
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
    
    # Fall back to LLM
    llm_results = llm_score_tags([flashcard], tags, client, max_tags)
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
        default=5,
        help='Number of cards per LLM API call (default: 5)'
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
        default='http://localhost:1234/v1',
        help='OpenAI-compatible API base URL (default: http://localhost:1234/v1)'
    )
    
    args = parser.parse_args()
    
    # Load tags
    if not args.tags_file.exists():
        print(f"Error: {args.tags_file} not found", file=sys.stderr)
        return 1
    
    tags = load_tags(args.tags_file)
    print(f"Loaded {len(tags)} tags from {args.tags_file}")
    
    # Initialize LLM client if needed
    client = None
    if args.strategy in ('llm', 'hybrid'):
        client = OpenAI(base_url=args.llm_url, api_key="not-needed")
        print(f"Initialized LLM client: {args.llm_url}")
    
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
        print(f"Using LLM strategy (batch size: {args.batch_size})...")
        for i in range(0, len(flashcards), args.batch_size):
            batch = flashcards[i:i+args.batch_size]
            print(f"Processing batch {i//args.batch_size + 1}/{(len(flashcards)-1)//args.batch_size + 1}...")
            
            try:
                results = llm_score_tags(batch, tags, client, args.max_tags)
                
                for card in batch:
                    card_results = results.get(card['path'], [])
                    if card_results:
                        tag_names = [r[0] for r in card_results]
                        update_flashcard_tags(card['path'], tag_names, args.dry_run)
                        stats['tagged'] += 1
                        stats['llm'] += 1
                        
                        if args.dry_run:
                            for tag, conf, reason in card_results:
                                print(f"    {tag} (conf: {conf:.2f}) - {reason}")
                    else:
                        stats['failed'] += 1
            except Exception as e:
                print(f"Error processing batch: {e}", file=sys.stderr)
                stats['failed'] += len(batch)
    
    elif args.strategy == 'hybrid':
        print(f"Using hybrid strategy (threshold: {args.threshold})...")
        for card in flashcards:
            try:
                results, strategy = hybrid_score_tags(
                    card, tags, client, args.threshold, args.max_tags
                )
                
                if results:
                    tag_names = [r[0] for r in results]
                    update_flashcard_tags(card['path'], tag_names, args.dry_run)
                    stats['tagged'] += 1
                    stats[strategy] += 1
                    
                    if args.dry_run:
                        print(f"  Strategy: {strategy}")
                        for tag, score, reason in results:
                            print(f"    {tag} (score: {score:.2f}) - {reason}")
                else:
                    stats['failed'] += 1
            except Exception as e:
                print(f"Error processing {card['path'].name}: {e}", file=sys.stderr)
                stats['failed'] += 1
    
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
