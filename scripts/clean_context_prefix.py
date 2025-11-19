#!/usr/bin/env python3
"""Utility to strip "[Context: ...]" and other bracketed prefixes from Anki deck notes."""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

# Match any "[prefix]" or "[prefix: details]" pattern at the start of a string
CONTEXT_PREFIX = re.compile(r"^\[[^\]]+\]\s*", re.IGNORECASE)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Remove bracketed prefixes like '[Context: ...]' or '[Jinja]' from note titles in a CrowdAnki deck JSON file."
    )
    parser.add_argument(
        "deck_path",
        type=Path,
        nargs="?",
        default=Path("dbt/deck.json"),
        help="Path to the deck JSON file (defaults to dbt/deck.json).",
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=None,
        help="Output path for the cleaned deck. If not provided, creates a new file with '_cleaned' suffix.",
    )
    parser.add_argument(
        "-y", "--yes",
        action="store_true",
        help="Skip confirmation prompt (auto-approve changes).",
    )
    return parser.parse_args()


def strip_prefix(value: Any) -> tuple[Any, bool]:
    if isinstance(value, str):
        new_value = CONTEXT_PREFIX.sub("", value, count=1)
        return new_value, new_value != value
    return value, False


def scan_prefixes(notes: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    """Scan notes and return list of prefixes that would be removed from note titles."""
    prefixes = []
    for note in notes:
        fields = note.get("fields") or []
        if fields:  # Check the first field (title)
            title = fields[0]
            if isinstance(title, str):
                match = CONTEXT_PREFIX.match(title)
                if match:
                    prefix = match.group(0).strip()
                    new_title = CONTEXT_PREFIX.sub("", title, count=1)
                    prefixes.append({
                        "prefix": prefix,
                        "old_title": title[:100] + ("..." if len(title) > 100 else ""),
                        "new_title": new_title[:100] + ("..." if len(new_title) > 100 else ""),
                    })
    return prefixes


def process_notes(notes: List[Dict[str, Any]]) -> int:
    """Process notes and remove prefixes from the first field (title) only."""
    changes = 0
    for note in notes:
        fields = note.get("fields") or []
        if fields:  # Only process the first field (title)
            new_field, changed = strip_prefix(fields[0])
            if changed:
                fields[0] = new_field
                changes += 1
    return changes


def load_deck(path: Path) -> Dict[str, Any]:
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def write_deck(path: Path, deck: Dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8") as fh:
        json.dump(deck, fh, ensure_ascii=False, indent=4)
        fh.write("\n")


def main() -> None:
    args = parse_args()
    deck_path = args.deck_path

    if not deck_path.exists():
        raise SystemExit(f"Deck file not found: {deck_path}")

    # Determine output path
    if args.output:
        output_path = args.output
    else:
        # Create output path with timestamp
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        stem = deck_path.stem
        output_path = deck_path.parent / f"{stem}-{timestamp}{deck_path.suffix}"

    deck = load_deck(deck_path)
    notes = deck.get("notes", [])

    # Scan for prefixes
    prefixes = scan_prefixes(notes)
    
    if not prefixes:
        print("No bracketed prefixes found; no output file created.")
        return

    # Display scan results
    print(f"\nFound {len(prefixes)} note(s) with bracketed prefixes:\n")
    
    # Group by prefix type for cleaner display
    prefix_groups: Dict[str, int] = {}
    for item in prefixes:
        prefix = item["prefix"]
        prefix_groups[prefix] = prefix_groups.get(prefix, 0) + 1
    
    for prefix, count in sorted(prefix_groups.items()):
        print(f"  {prefix}: {count} note(s)")
    
    print("\nExample transformations:")
    for i, item in enumerate(prefixes[:3], 1):  # Show first 3 examples
        print(f"\n{i}. Prefix: {item['prefix']}")
        print(f"   Old: {item['old_title']}")
        print(f"   New: {item['new_title']}")
    
    if len(prefixes) > 3:
        print(f"\n   ... and {len(prefixes) - 3} more")
    
    # Ask for confirmation unless --yes flag is set
    if not args.yes:
        print(f"\n{len(prefixes)} note title(s) will be modified.")
        print(f"Output will be written to: {output_path}")
        response = input("Proceed with removing prefixes? [y/N]: ").strip().lower()
        if response not in ("y", "yes"):
            print("Cancelled.")
            return

    # Process notes
    modified_fields = process_notes(notes)
    write_deck(output_path, deck)
    print(f"\n✓ Removed prefixes from {modified_fields} note title(s).")
    print(f"✓ Cleaned deck written to: {output_path}")
    print(f"✓ Original file unchanged: {deck_path}")


if __name__ == "__main__":
    main()
