import json
from pathlib import Path

# Define paths relative to the workspace root
SOURCE_DIR = Path("docs/site_docs.getdbt.com")
DEST_DIR = Path("docs/cleaned_docs")

def clean_content(content):
    """
    Extracts essential content from markdown by removing header/footer noise.
    """
    lines = content.split('\n')
    
    # Find the start of actual content
    # Look for the first H1 heading (# Title) or the article content
    start_idx = 0
    found_start = False
    
    # Skip everything until we hit the main title/content
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Skip source URL line
        if i == 0 and stripped.startswith('# Source:'):
            continue
            
        # Skip initial title lines that are just page metadata
        if i <= 5 and any(x in stripped for x in ['| dbt Developer', '| dbt Developer Hub']):
            continue
            
        # Navigation/menu markers to skip
        if any(marker in stripped for marker in [
            '[Skip to main content]',
            '[![dbt Logo]',
            '[Docs](#)',
            '[Guides]',
            '[APIs]',
            '[Help](#)',
            '[Community](#)',
            '[Account](#)',
            '[Install VS Code extension]',
            'dbt platform (Latest)',
            'Search`⌘``K`',
            '[dbt Docs]'
        ]):
            continue
            
        # Menu items with bullets
        if stripped.startswith('* [') and any(x in stripped for x in [
            'Product docs', 'References', 'Best practices', 'Developer blog',
            'Release notes', 'FAQs', 'Support and billing', 'Courses',
            'Join the dbt Community', 'Create a free account', 'Log in to dbt'
        ]):
            continue
            
        # Found first substantial heading or content
        if stripped.startswith('# ') and len(stripped) > 3 and not any(x in stripped for x in ['Source:', '|']):
            start_idx = i
            found_start = True
            break
        
        # Or find first paragraph of actual content
        if len(stripped) > 50 and not stripped.startswith('[') and not stripped.startswith('*'):
            start_idx = i
            found_start = True
            break
    
    # Find the end of actual content - cut off everything after the main article
    end_idx = len(lines)
    
    # Look for clear end-of-article markers
    end_markers = [
        '#### Comments',
        '**Tags:**',
        '[Newer post',
        '[Older post',
        '[Previous',
        '[Next',
        'Get started',
        '##### Resources',
        '[Edit this page]',
        'Was this page helpful?'
    ]
    
    for i in range(start_idx, len(lines)):
        stripped = lines[i].strip()
        # Check for any end marker
        for marker in end_markers:
            if stripped.startswith(marker):
                end_idx = i
                break
        if end_idx < len(lines):
            break
    
    # Extract the content section
    cleaned_lines = lines[start_idx:end_idx]
    
    # Additional filtering of remaining noise
    final_lines = []
    skip_next = False
    in_nav_section = True  # Assume we start in navigation until proven otherwise
    
    for i, line in enumerate(cleaned_lines):
        if skip_next:
            skip_next = False
            continue
            
        stripped = line.strip()
        
        # Skip empty lines at the boundaries
        if not stripped:
            final_lines.append(line)
            continue
        
        # Navigation sections often start with bullets - skip them until we hit real content
        if in_nav_section:
            # If we see a bullet point with link or just plain bullet
            if stripped.startswith('* '):
                continue
            # If we see nested bullets
            if stripped.startswith('+ [') or stripped.startswith('- ['):
                continue
            # If this looks like a heading or substantial paragraph, we're past navigation
            if stripped.startswith('#') or (len(stripped) > 50 and not stripped.startswith('[')):
                in_nav_section = False
        
        # Skip navigation breadcrumbs
        if i < 10 and stripped.startswith('[') and '](' in stripped and any(x in stripped for x in ['dbt Docs', 'Blog', 'Commands', 'References']):
            continue
            
        # Skip version selector
        if '[v](#)' in stripped or stripped in ['* dbt platform (Latest)', '* dbt Fusion engine', '* Core v1.11 Beta']:
            continue
        
        # Skip table of contents links at the end (often appear after main content)
        if stripped.startswith('* [') and i > len(cleaned_lines) - 20:
            # This might be a TOC section at the end
            continue
        
        final_lines.append(line)
    
    result = "\n".join(final_lines).strip()
    
    # Remove any remaining blocks of repeated navigation
    # Clean up multiple consecutive empty lines
    while '\n\n\n' in result:
        result = result.replace('\n\n\n', '\n\n')
    
    # Final pass: remove any remaining TOC sections at the end
    # These often start with "* [" bullets listing sections
    lines_final = result.split('\n')
    final_cut = len(lines_final)
    
    # Look for sections that are just TOC links (multiple consecutive bullet links)
    consecutive_bullets = 0
    for i in range(len(lines_final) - 1, -1, -1):
        stripped = lines_final[i].strip()
        if stripped.startswith('* [') and '](#' in stripped:
            consecutive_bullets += 1
            if consecutive_bullets >= 3:  # If we see 3+ TOC-style bullets in a row
                final_cut = i
        elif stripped:  # Non-empty, non-bullet line
            consecutive_bullets = 0
    
    if final_cut < len(lines_final):
        result = "\n".join(lines_final[:final_cut]).strip()
    
    return result

def main():
    # Ensure destination directory exists
    if not DEST_DIR.exists():
        DEST_DIR.mkdir(parents=True)
        print(f"Created directory: {DEST_DIR}")

    # 1. Process and copy index.json
    index_path = SOURCE_DIR / "index.json"
    if index_path.exists():
        print(f"Processing index file: {index_path}")
        try:
            with open(index_path, 'r', encoding='utf-8') as f:
                index_data = json.load(f)
            
            new_index = []
            for entry in index_data:
                original_local_path = entry.get('local_path')
                if original_local_path:
                    # Convert source path to dest path for the index
                    # e.g. docs/site_docs.getdbt.com/folder/file.md -> docs/cleaned_docs/folder/file.md
                    try:
                        # We assume local_path in json is relative to repo root
                        p = Path(original_local_path)
                        # Find relative path from the source directory
                        # Note: original_local_path might be like "docs/site_docs.getdbt.com/..."
                        # We need to handle if it is relative to cwd or absolute (unlikely in json)
                        
                        # Check if path starts with the source dir name
                        if str(SOURCE_DIR) in str(p):
                             rel_path = p.relative_to(SOURCE_DIR)
                        elif str(p).startswith("docs/site_docs.getdbt.com"):
                             # Handle string manipulation if Path fails due to cwd context
                             rel_path = Path(str(p).replace("docs/site_docs.getdbt.com/", ""))
                        else:
                             # Fallback or skip
                             print(f"Skipping path adjustment for: {original_local_path}")
                             new_index.append(entry)
                             continue

                        new_local_path = str(DEST_DIR / rel_path)
                        
                        entry['local_path'] = new_local_path
                        new_index.append(entry)
                    except Exception as e:
                        print(f"Warning: Could not adjust path {original_local_path}: {e}")
                        new_index.append(entry)
            
            # Write new index
            dest_index_path = DEST_DIR / "index.json"
            with open(dest_index_path, 'w', encoding='utf-8') as f:
                json.dump(new_index, f, indent=2)
            print(f"Wrote new index to: {dest_index_path}")
            
        except Exception as e:
            print(f"Error processing index.json: {e}")

    # 2. Process markdown files
    print("Processing markdown files...")
    count = 0
    for file_path in SOURCE_DIR.rglob("*.md"):
        try:
            # Read original content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Clean content
            cleaned = clean_content(content)
            
            # Determine destination path
            rel_path = file_path.relative_to(SOURCE_DIR)
            dest_path = DEST_DIR / rel_path
            
            # Ensure subdirectories exist
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Write cleaned content
            with open(dest_path, 'w', encoding='utf-8') as f:
                f.write(cleaned)
            
            count += 1
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    print(f"Successfully processed {count} markdown files.")

if __name__ == "__main__":
    main()
