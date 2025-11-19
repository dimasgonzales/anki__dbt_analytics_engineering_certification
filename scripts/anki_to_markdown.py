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
import uuid
from pathlib import Path
from typing import Any, Dict, List, Tuple

from markdownify import markdownify as md


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


def load_deck(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


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
    
    # Extract links from back
    back_md, citations = extract_links(back_md_raw)
    
    parts: List[str] = []
    
    # Add frontmatter
    parts.append("---")
    parts.append(f"uuid: {note_uuid}")
    parts.append(f"guid: {guid}")
    if tags:
        parts.append("tags:")
        for tag in tags:
            parts.append(f"  - {tag}")
    if citations:
        parts.append("citations:")
        for url in citations:
            parts.append(f"  - {url}")
    parts.append("---")
    parts.append("")
    
    # Add front and back with horizontal divider between them
    parts.append("<front>")
    parts.append(front_md)
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
    parser = argparse.ArgumentParser(description="Export each note from an Anki/CrowdAnki-like JSON deck to individual markdown files.")
    parser.add_argument("--in", dest="input_path", default="decks/dbt_deck.json", help="Path to deck JSON (default: dbt/deck.json)")
    parser.add_argument("--out", dest="output_dir", default="deck", help="Output directory for markdown files (default: deck)")
    args = parser.parse_args()

    in_path = Path(args.input_path)
    out_dir = Path(args.output_dir)

    if not in_path.exists():
        raise SystemExit(f"Input file not found: {in_path}")

    deck = load_deck(in_path)
    notes: List[Dict[str, Any]] = deck.get("notes", [])

    out_dir.mkdir(parents=True, exist_ok=True)
    
    created_count = 0
    for note in notes:
        # Generate a new UUID for each card
        note_uuid = str(uuid.uuid4())
            
        markdown = build_note_markdown(note, note_uuid)
        if not markdown:
            continue
        
        out_path = out_dir / f"{note_uuid}.md"
        out_path.write_text(markdown, encoding="utf-8")
        created_count += 1

    print(f"Created {created_count} markdown files in {out_dir}")


if __name__ == "__main__":
    main()
