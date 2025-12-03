#!/usr/bin/env python3
"""
Fix structural errors in flashcards.
"""

# /// script
# dependencies = [
#   "pyyaml",
# ]
# ///

import argparse
import re
import sys
import yaml
from pathlib import Path
from typing import Optional

def fix_file(file_path: Path, dry_run: bool = False) -> bool:
    """
    Fix a single flashcard file.
    Returns True if changes were made (or would be made).
    """
    try:
        content = file_path.read_text()
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
        return False

    original_content = content

    # 1. Fix Double Start Delimiters
    # Some files start with:
    # ---
    # ---
    # tags: ...
    #
    # We want to remove one of the first two lines if both are '---'.
    lines = content.splitlines()
    if len(lines) > 1 and lines[0].strip() == '---' and lines[1].strip() == '---':
        # Remove the first line
        content = '\n'.join(lines[1:]) + '\n'

    # 2. Parse Frontmatter and Body
    # We use a regex that is tolerant of the content
    match = re.match(r'^---\n(.*?)---\n(.*)$', content, re.DOTALL)
    if not match:
        print(f"Skipping {file_path.name}: Could not parse frontmatter structure.", file=sys.stderr)
        return False

    frontmatter_str = match.group(1)
    body = match.group(2)

    try:
        frontmatter = yaml.safe_load(frontmatter_str)
    except yaml.YAMLError as e:
        print(f"Skipping {file_path.name}: Invalid YAML in frontmatter: {e}", file=sys.stderr)
        return False

    if not isinstance(frontmatter, dict):
        print(f"Skipping {file_path.name}: Frontmatter is not a dictionary.", file=sys.stderr)
        return False

    # 3. Extract Front and Back
    # We look for <front>...</front> and <back>...</back> ignoring everything else (like stray separators)
    front_match = re.search(r'<front>(.*?)</front>', body, re.DOTALL)
    back_match = re.search(r'<back>(.*?)</back>', body, re.DOTALL)

    if not front_match or not back_match:
        print(f"Skipping {file_path.name}: Could not find <front> and <back> tags.", file=sys.stderr)
        return False

    front_content = front_match.group(1).strip()
    back_content = back_match.group(1).strip()

    # 4. Reconstruct File
    # We rebuild the file with strict formatting:
    # ---
    # <yaml>
    # ---
    #
    # <front>
    # ...
    # </front>
    #
    # ---
    #
    # <back>
    # ...
    # </back>
    
    # Dump yaml with block style for lists (tags)
    # We want to preserve the order if possible, but yaml.safe_dump doesn't guarantee it.
    # However, for these simple files, it's usually fine.
    # We use sort_keys=False to keep insertion order if python dict preserves it (Python 3.7+ does).
    
    new_frontmatter_str = yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True, default_flow_style=False).strip()
    
    new_content = f"""---
{new_frontmatter_str}
---

<front>
{front_content}
</front>

---

<back>
{back_content}
</back>
"""

    if new_content != original_content:
        if dry_run:
            print(f"[DRY RUN] Would fix {file_path.name}")
        else:
            file_path.write_text(new_content)
            print(f"Fixed {file_path.name}")
        return True
    
    return False

def main():
    parser = argparse.ArgumentParser(description="Fix structural errors in flashcards.")
    parser.add_argument('--deck-dir', type=Path, default=Path('deck'), help='Path to deck directory')
    parser.add_argument('--dry-run', action='store_true', help='Do not modify files, just show what would be fixed')
    args = parser.parse_args()

    if not args.deck_dir.exists():
        print(f"Error: {args.deck_dir} not found.", file=sys.stderr)
        sys.exit(1)

    files = sorted(args.deck_dir.glob('*.md'))
    total_files = len(files)
    fixed_files = 0

    print(f"Scanning {total_files} files in {args.deck_dir}...\n")

    for file_path in files:
        if fix_file(file_path, dry_run=args.dry_run):
            fixed_files += 1

    print("-" * 40)
    print(f"Complete.")
    print(f"Files scanned: {total_files}")
    print(f"Files fixed: {fixed_files}")

if __name__ == "__main__":
    main()
