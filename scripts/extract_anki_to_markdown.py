#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = [
#   "markdownify>=0.11.0",
# ]
# ///
import argparse
import html
import json
import re
import sqlite3
import tempfile
import uuid
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Dict, List, Tuple

from markdownify import markdownify as md


@dataclass
class CleaningRule:
    """Represents a text cleaning rule with a name, pattern, and transformation."""
    name: str
    pattern: re.Pattern
    replacement: str | Callable[[re.Match], str]
    description: str = ""
    
    def apply(self, text: str) -> tuple[str, bool]:
        """Apply the cleaning rule to text. Returns (cleaned_text, was_changed)."""
        if callable(self.replacement):
            new_text = self.pattern.sub(self.replacement, text)
        else:
            new_text = self.pattern.sub(self.replacement, text)
        return new_text, new_text != text


# Default cleaning rules - easily extensible
DEFAULT_CLEANING_RULES = [
    CleaningRule(
        name="context_prefix",
        pattern=re.compile(r"^\[[^\]]+\]\s*", re.IGNORECASE),
        replacement="",
        description="Remove bracketed prefixes like '[Context: ...]' or '[Jinja]' from start of text"
    ),
    # Add more rules here as needed, e.g.:
    # CleaningRule(
    #     name="trailing_whitespace",
    #     pattern=re.compile(r"\s+$", re.MULTILINE),
    #     replacement="",
    #     description="Remove trailing whitespace from lines"
    # ),
]


def apply_cleaning_rules(text: str, rules: List[CleaningRule] = None) -> str:
    """Apply a list of cleaning rules to text."""
    if rules is None:
        rules = DEFAULT_CLEANING_RULES
    
    for rule in rules:
        text, _ = rule.apply(text)
    
    return text


def extract_code_from_table(table_html: str) -> str:
    """Extract code text from a syntax-highlighted HTML table."""
    # Find the <td class="code"> section
    code_match = re.search(r'<td class="code">(.*?)</td>', table_html, re.DOTALL)
    if not code_match:
        return ""
    
    code_content = code_match.group(1)
    
    # Strip all HTML tags
    code_text = re.sub(r'<[^>]+>', '', code_content)
    
    # Unescape HTML entities
    code_text = html.unescape(code_text)
    
    # Strip leading/trailing whitespace
    return code_text.strip()


def convert_code_tables(html_content: str) -> str:
    """Convert syntax-highlighted HTML tables to markdown code blocks."""
    def replace_table(match):
        table_html = match.group(0)
        code = extract_code_from_table(table_html)
        if code:
            return f"\n```\n{code}\n```"
        return match.group(0)
    
    # Replace all highlighttable instances
    return re.sub(
        r'<table class="highlighttable">.*?</table>',
        replace_table,
        html_content,
        flags=re.DOTALL
    )


def load_apkg(path: Path) -> List[Dict[str, Any]]:
    """Extract and parse notes from an Anki .apkg file."""
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        # Extract the .apkg ZIP archive
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall(temp_path)
        
        # Find the SQLite database (try both names)
        db_path = temp_path / "collection.anki2"
        if not db_path.exists():
            db_path = temp_path / "collection.anki21"
        
        if not db_path.exists():
            raise FileNotFoundError(f"No collection database found in {path}")
        
        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        # Query all notes
        cursor.execute("""
            SELECT id, guid, mid, mod, tags, flds, sfld, csum, flags, data
            FROM notes
        """)
        
        notes = []
        for row in cursor.fetchall():
            # Fields are separated by \x1f character
            fields = row['flds'].split('\x1f')
            
            # Tags are space-separated
            tags = row['tags'].strip().split() if row['tags'] else []
            
            note = {
                'id': row['id'],
                'guid': row['guid'],
                'model_id': row['mid'],
                'modified': row['mod'],
                'tags': tags,
                'fields': fields,
                'sort_field': row['sfld'],
                'checksum': row['csum'],
                'flags': row['flags'],
                'data': row['data']
            }
            notes.append(note)
        
        conn.close()
        
        return notes


def convert_multiline_code_tags(html_content: str) -> Tuple[str, List[str]]:
    """Convert <code> tags containing <br> to markdown code blocks."""
    code_blocks = []
    
    def replace_code(match):
        code_content = match.group(1)
        # Check if it contains line breaks
        if '<br>' in code_content.lower():
            # Strip HTML tags and decode entities
            code_text = re.sub(r'<br\s*/?>', '\n', code_content, flags=re.IGNORECASE)
            code_text = re.sub(r'<[^>]+>', '', code_text)
            code_text = html.unescape(code_text)
            code_text = code_text.strip()
            # Store the code block and return a placeholder (using unusual chars to avoid escaping)
            placeholder = f"XXXXXCODEBLOCKXXXXX{len(code_blocks)}XXXXXCODEBLOCKXXXXX"
            code_blocks.append(code_text)
            return placeholder
        return match.group(0)
    
    result = re.sub(r'<code>(.*?)</code>', replace_code, html_content, flags=re.DOTALL)
    return result, code_blocks


def convert_html_to_markdown(html: str) -> str:
    """Convert HTML to markdown, handling special cases."""
    if not html:
        return ""
    
    # Preprocess: strip <center> tags
    html = re.sub(r'</?center>', '', html)
    
    # Preprocess: convert syntax-highlighted tables to markdown code blocks
    html = convert_code_tables(html)
    
    # Preprocess: convert multiline <code> tags to markdown code blocks (with placeholders)
    html, code_blocks = convert_multiline_code_tags(html)
    
    # Convert HTML to markdown using markdownify
    markdown = md(html, heading_style="ATX", bullets="-")
    
    # Restore code blocks from placeholders
    for i, code_block in enumerate(code_blocks):
        placeholder = f"XXXXXCODEBLOCKXXXXX{i}XXXXXCODEBLOCKXXXXX"
        markdown = markdown.replace(placeholder, f"\n```\n{code_block}\n```")
    
    # Remove non-breaking spaces
    markdown = markdown.replace("&nbsp;", " ")
    
    # Clean up excessive newlines (more than 2 consecutive) - AFTER code blocks restored
    markdown = re.sub(r'\n{3,}', '\n\n', markdown)
    
    # Strip leading/trailing whitespace
    markdown = markdown.strip()
    
    return markdown


def extract_links(text: str) -> tuple[str, List[str]]:
    """Extract markdown and HTML links from text, returning cleaned text and list of URLs."""
    urls = []
    
    # Extract markdown links [text](url)
    markdown_links = re.findall(r'\[([^\]]*)\]\(([^)]+)\)', text)
    for link_text, url in markdown_links:
        urls.append(url)
        # Remove the markdown link, keep the text if it exists
        if link_text:
            text = text.replace(f'[{link_text}]({url})', link_text)
        else:
            text = text.replace(f'[]({url})', '')
    
    # Extract bare URLs in angle brackets <url>
    angle_urls = re.findall(r'<(https?://[^>]+)>', text)
    for url in angle_urls:
        urls.append(url)
        text = text.replace(f'<{url}>', '')
    
    # Extract bare URLs (not in markdown links or angle brackets)
    bare_urls = re.findall(r'(?<!\()(?<!\[)https?://[^\s<>\[\]()]+', text)
    for url in bare_urls:
        urls.append(url)
        text = text.replace(url, '')
    
    # Clean up extra whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = text.strip()
    
    return text, urls


def build_note_markdown(note: Dict[str, Any], note_uuid: str) -> str:
    """Build markdown for a single note with frontmatter and XML tags."""
    fields = note.get("fields", [])
    if not isinstance(fields, list) or len(fields) < 2:
        return ""
    
    front = fields[0] or ""
    back = fields[1] or ""
    tags = [tag for tag in (note.get("tags") or []) if tag]
    guid = note.get("guid", "")
    
    # Convert HTML to markdown
    front_md = convert_html_to_markdown(front)
    back_md_raw = convert_html_to_markdown(back)
    
    # Apply cleaning rules to front
    front_md = apply_cleaning_rules(front_md)
    
    # Extract links from back
    back_md, citations = extract_links(back_md_raw)
    
    parts: List[str] = []
    
    # Add frontmatter (sorted alphabetically for stable diffs)
    parts.append("---")
    if citations:
        parts.append("citations:")
        for url in citations:
            parts.append(f"  - {url}")
    parts.append(f"guid: {guid}")
    parts.append("source: apkg")
    if tags:
        parts.append("tags:")
        for tag in tags:
            parts.append(f"  - {tag}")
    parts.append(f"uuid: {note_uuid}")
    parts.append("---")
    parts.append("")
    
    # Add front and back with horizontal divider between them
    parts.append("<front>")
    if front_md:
        parts.append("")
        parts.append(front_md)
        parts.append("")
    parts.append("</front>")
    parts.append("")
    parts.append("---")
    parts.append("")
    # Add back tag with preserved leading/trailing whitespace
    parts.append("<back>")
    if back_md:
        parts.append("")
        parts.append(back_md)
        parts.append("")
    parts.append("</back>")
    parts.append("")  # Trailing newline after </back>
    
    return "\n".join(parts)


def main() -> None:
    parser = argparse.ArgumentParser(description="Export each note from an Anki .apkg file to individual markdown files.")
    parser.add_argument("--in", dest="input_path", default="docs/dbt_Analytics_Engineering_Certification_Exam.apkg", help="Path to .apkg file (default: docs/dbt_Analytics_Engineering_Certification_Exam.apkg)")
    parser.add_argument("--out", dest="output_dir", default="deck", help="Output directory for markdown files (default: deck)")
    args = parser.parse_args()

    in_path = Path(args.input_path)
    out_dir = Path(args.output_dir)

    if not in_path.exists():
        raise SystemExit(f"Input file not found: {in_path}")

    notes: List[Dict[str, Any]] = load_apkg(in_path)

    out_dir.mkdir(parents=True, exist_ok=True)
    
    # Use a consistent namespace UUID for deterministic UUID generation
    NAMESPACE_UUID = uuid.UUID('6ba7b810-9dad-11d1-80b4-00c04fd430c8')  # DNS namespace
    
    created_count = 0
    for note in notes:
        # Generate a deterministic UUID based on the note's GUID
        # This ensures the same note always gets the same UUID
        note_uuid = str(uuid.uuid5(NAMESPACE_UUID, note.get('guid', '')))
            
        markdown = build_note_markdown(note, note_uuid)
        if not markdown:
            continue
        
        out_path = out_dir / f"{note_uuid}.md"
        out_path.write_text(markdown, encoding="utf-8")
        created_count += 1

    print(f"Created {created_count} markdown files in {out_dir}")


if __name__ == "__main__":
    main()
