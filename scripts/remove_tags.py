import os
import sys

def get_project_root():
    """
    Determines the project root.
    Assumes the script is either in <root>/scripts/ or <root>/
    """
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    
    # Check if we are in 'scripts' directory
    if os.path.basename(script_dir) == 'scripts':
        return os.path.dirname(script_dir)
    
    # Assume we are in root if not in scripts
    return script_dir

def remove_tags_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    in_frontmatter = False
    in_tags = False
    frontmatter_count = 0

    for line in lines:
        stripped = line.strip()
        
        # Detect frontmatter delimiters
        if stripped == '---':
            frontmatter_count += 1
            if frontmatter_count == 1:
                in_frontmatter = True
            elif frontmatter_count == 2:
                in_frontmatter = False
                in_tags = False # Ensure we exit tag mode
            
            new_lines.append(line)
            continue

        if in_frontmatter:
            # Check for start of tags section
            if stripped.startswith('tags:'):
                in_tags = True
                continue # Skip the 'tags:' line

            if in_tags:
                # If we are in tags section, skip indented lines (list items)
                # or empty lines that might be part of the block formatting
                if line.startswith((' ', '\t')) or stripped == '':
                    continue
                else:
                    # We found a line that is not indented and not empty
                    # This means we are out of the tags section (e.g. new key)
                    in_tags = False
                    new_lines.append(line)
            else:
                # Not in tags section, keep the line
                new_lines.append(line)
        else:
            # Not in frontmatter, keep everything
            new_lines.append(line)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

def main():
    root_dir = get_project_root()
    deck_dir = os.path.join(root_dir, 'deck')
    
    if not os.path.exists(deck_dir):
        print(f"Error: deck directory not found at {deck_dir}")
        sys.exit(1)
        
    count = 0
    # Iterate over .md files
    for filename in os.listdir(deck_dir):
        if filename.endswith('.md'):
            file_path = os.path.join(deck_dir, filename)
            remove_tags_from_file(file_path)
            count += 1
            
    print(f"Processed {count} files. Tags removed.")

if __name__ == "__main__":
    main()
