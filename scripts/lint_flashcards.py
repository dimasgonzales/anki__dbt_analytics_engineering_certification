#!/usr/bin/env python3
"""
Lint flashcards to ensure they adhere to the required format and constraints.
"""

# /// script
# dependencies = [
#   "pyyaml",
# ]
# ///

import argparse
import json
import re
import sys
import yaml
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple

# Constants
REQUIRED_KEYS = {'guid', 'uuid', 'tags'}
VALID_CARD_TYPES = {'factual', 'scenario'}

def load_valid_tags(tags_path: Path) -> Set[str]:
    """Load valid child tags from tags.json."""
    if not tags_path.exists():
        print(f"Error: {tags_path} not found.", file=sys.stderr)
        sys.exit(1)
    
    with open(tags_path, 'r') as f:
        data = json.load(f)
    
    return {item['child_tag'] for item in data}

def lint_file(
    file_path: Path, 
    valid_tags: Set[str], 
    seen_uuids: Dict[str, Path]
) -> List[str]:
    """Lint a single flashcard file and return a list of error messages."""
    errors = []
    content = file_path.read_text()
    
    # 1. Check Frontmatter
    # Expecting file to start with ---, then YAML, then ---
    match = re.match(r'^---\n(.*?)---\n(.*)$', content, re.DOTALL)
    if not match:
        errors.append("Invalid file format: Missing frontmatter delimiters or structure.")
        return errors

    frontmatter_str = match.group(1)
    body = match.group(2)

    try:
        frontmatter = yaml.safe_load(frontmatter_str)
    except yaml.YAMLError as e:
        errors.append(f"Invalid YAML in frontmatter: {e}")
        return errors
    
    if not isinstance(frontmatter, dict):
        errors.append("Frontmatter is not a dictionary.")
        return errors

    # 1a. Valid tags
    if 'tags' not in frontmatter:
        errors.append("Missing 'tags' in frontmatter.")
    elif not isinstance(frontmatter['tags'], list):
        errors.append("'tags' must be a list.")
    else:
        for tag in frontmatter['tags']:
            if tag.startswith('card_type/'):
                continue
            if tag not in valid_tags:
                errors.append(f"Invalid tag: '{tag}'")

    # 1b. guid, uuid, factual/scenario
    for key in ['guid', 'uuid']:
        if key not in frontmatter:
            errors.append(f"Missing required key: '{key}'")
    
    # Check card_type (must be a tag now)
    if 'card_type' in frontmatter:
        errors.append("Deprecated key 'card_type' found in frontmatter. Use 'card_type/...' tag instead.")
    
    # Verify at least one card_type tag exists
    card_type_tags = [t for t in frontmatter.get('tags', []) if t.startswith('card_type/')]
    if not card_type_tags:
        errors.append("Missing card_type tag (e.g., 'card_type/factual').")
    else:
        for ct_tag in card_type_tags:
            ctype = ct_tag.split('/', 1)[1]
            if ctype not in VALID_CARD_TYPES:
                errors.append(f"Invalid card_type tag: '{ct_tag}'. Suffix must be one of {VALID_CARD_TYPES}")

    # 2. Unique UUID
    if 'uuid' in frontmatter:
        uuid = frontmatter['uuid']
        if uuid in seen_uuids:
            errors.append(f"Duplicate UUID '{uuid}' found. Also in {seen_uuids[uuid].name}")
        else:
            seen_uuids[uuid] = file_path

    # 3. XML tags in body
    if '<front>' not in body or '</front>' not in body:
        errors.append("Missing <front>...</front> tags in body.")
    if '<back>' not in body or '</back>' not in body:
        errors.append("Missing <back>...</back> tags in body.")

    # 4. Horizontal line separator
    # Check for separator between front and back
    # We expect the structure: <front>...</front>\n\n---\n\n<back>...</back>
    # But let's be a bit flexible on whitespace, but strict on the order.
    
    # Regex to find the separator specifically between front and back
    # Using a regex that looks for </front> ... --- ... <back>
    separator_match = re.search(r'</front>.*?(\n---\n).*?<back>', body, re.DOTALL)
    if not separator_match:
        errors.append("Missing horizontal line separator '---' between </front> and <back>.")

    # 5. Stray horizontal lines
    # Count total '---' lines in the file.
    # Should be exactly 3: start of file, end of frontmatter, separator between front/back.
    # We match lines that are exactly '---' (possibly with surrounding whitespace if that's how they appear, 
    # but usually they are on their own line).
    # The regex ^---$ with multiline flag should catch them.
    
    horizontal_lines = re.findall(r'^---$', content, re.MULTILINE)
    if len(horizontal_lines) != 3:
        errors.append(f"Incorrect number of horizontal lines (---). Expected 3, found {len(horizontal_lines)}. Check for stray separators.")

    return errors

def main():
    parser = argparse.ArgumentParser(description="Lint flashcards.")
    parser.add_argument('--deck-dir', type=Path, default=Path('deck'), help='Path to deck directory')
    parser.add_argument('--tags-file', type=Path, default=Path('tags.json'), help='Path to tags.json')
    args = parser.parse_args()

    if not args.deck_dir.exists():
        print(f"Error: {args.deck_dir} not found.", file=sys.stderr)
        sys.exit(1)

    valid_tags = load_valid_tags(args.tags_file)
    seen_uuids = {}
    
    files = sorted(args.deck_dir.glob('*.md'))
    total_files = len(files)
    files_with_errors = 0
    total_errors = 0

    print(f"Linting {total_files} files in {args.deck_dir}...\n")

    for file_path in files:
        errors = lint_file(file_path, valid_tags, seen_uuids)
        if errors:
            files_with_errors += 1
            total_errors += len(errors)
            print(f"File: {file_path.name}")
            for err in errors:
                print(f"  - {err}")
            print()

    print("-" * 40)
    print(f"Linting complete.")
    print(f"Files checked: {total_files}")
    print(f"Files with errors: {files_with_errors}")
    print(f"Total errors: {total_errors}")

    if total_errors > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()
