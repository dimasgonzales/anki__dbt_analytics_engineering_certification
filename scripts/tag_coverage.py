import json
import os
import sys
from collections import defaultdict

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
    
    # Assume we are in root if not in scripts (or handle other cases if needed)
    return script_dir

def load_valid_tags(root_dir):
    """Load tags and return both valid child tags set and parent-child mapping."""
    tags_path = os.path.join(root_dir, 'tags.json')
    if not os.path.exists(tags_path):
        print(f"Error: tags.json not found at {tags_path}")
        sys.exit(1)
        
    with open(tags_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    valid_tags = set()
    parent_to_children = defaultdict(list)
    
    for item in data:
        if 'child_tag' in item:
            child_tag = item['child_tag']
            parent_tag = item.get('parent_tag', 'unknown')
            valid_tags.add(child_tag)
            parent_to_children[parent_tag].append(child_tag)
            
    return valid_tags, parent_to_children

def parse_tags_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Extract frontmatter
    if not content.startswith('---'):
        return []
        
    parts = content.split('---', 2)
    if len(parts) < 3:
        return []
        
    frontmatter = parts[1]
    lines = frontmatter.split('\n')
    
    tags = []
    in_tags_section = False
    
    for line in lines:
        stripped_line = line.strip()
        
        if not stripped_line:
            continue
            
        if stripped_line.startswith('tags:'):
            in_tags_section = True
            continue
            
        if in_tags_section:
            # Check if this line is a list item (starts with -)
            if stripped_line.startswith('-'):
                tag = stripped_line.lstrip('- ').strip()
                tags.append(tag)
            # Check if we've moved to a new key (e.g. "other_key:")
            elif ':' in stripped_line:
                in_tags_section = False
                
    return tags

def calculate_hierarchical_stats(parent_to_children, tag_to_cards, total_cards):
    """Calculate parent and child level statistics."""
    parent_stats = {}
    
    for parent, children in parent_to_children.items():
        # Collect all cards tagged with any child of this parent
        parent_cards = set()
        child_stats = {}
        
        for child in children:
            child_cards = tag_to_cards.get(child, set())
            parent_cards.update(child_cards)
            child_stats[child] = {
                'count': len(child_cards),
                'percentage': (len(child_cards) / total_cards * 100) if total_cards > 0 else 0
            }
        
        parent_stats[parent] = {
            'count': len(parent_cards),
            'percentage': (len(parent_cards) / total_cards * 100) if total_cards > 0 else 0,
            'children': child_stats
        }
    
    return parent_stats

def print_hierarchical_tree(parent_stats, parent_to_children, total_cards):
    """Print hierarchical tree of tag coverage."""
    print("\n" + "="*60)
    print("TAG COVERAGE BY HIERARCHY")
    print("="*60)
    
    # Sort parents alphabetically
    for parent in sorted(parent_to_children.keys()):
        stats = parent_stats[parent]
        print(f"\n{parent}: {stats['count']}/{total_cards} cards ({stats['percentage']:.1f}%)")
        
        # Sort children alphabetically
        for child in sorted(parent_to_children[parent]):
            child_stats = stats['children'][child]
            print(f"  - {child}: {child_stats['count']}/{total_cards} cards ({child_stats['percentage']:.1f}%)")

def main():
    root_dir = get_project_root()
    deck_dir = os.path.join(root_dir, 'deck')
    
    valid_tags, parent_to_children = load_valid_tags(root_dir)
    found_tags = set()
    tag_to_cards = defaultdict(set)
    card_to_tags = {}
    
    if not os.path.exists(deck_dir):
        print(f"Error: deck directory not found at {deck_dir}")
        sys.exit(1)
        
    # Iterate over .md files
    total_cards = 0
    for filename in os.listdir(deck_dir):
        if filename.endswith('.md'):
            total_cards += 1
            file_path = os.path.join(deck_dir, filename)
            file_tags = parse_tags_from_file(file_path)
            found_tags.update(file_tags)
            card_to_tags[filename] = file_tags
            
            # Track which cards have each tag
            for tag in file_tags:
                tag_to_cards[tag].add(filename)
    
    # Count untagged cards and collect their filenames
    untagged_cards = sorted([filename for filename, tags in card_to_tags.items() if len(tags) == 0])
    untagged_count = len(untagged_cards)
    
    # Identify undefined tags
    undefined_tags = sorted(list(found_tags - valid_tags))
    
    # Calculate hierarchical statistics
    parent_stats = calculate_hierarchical_stats(parent_to_children, tag_to_cards, total_cards)
    
    # Print hierarchical tree
    print_hierarchical_tree(parent_stats, parent_to_children, total_cards)
    
    # Print untagged cards
    print(f"\n" + "="*60)
    print(f"UNTAGGED CARDS: {untagged_count}/{total_cards} cards ({(untagged_count/total_cards*100) if total_cards > 0 else 0:.1f}%)")
    print("="*60)
    if untagged_cards:
        for card in untagged_cards:
            print(f"  - deck/{card}")
    
    # Calculate overall coverage
    # Coverage = (valid tags that appear in at least one file) / (total valid tags)
    used_valid_tags = found_tags.intersection(valid_tags)
    
    if len(valid_tags) > 0:
        coverage_pct = (len(used_valid_tags) / len(valid_tags)) * 100
    else:
        coverage_pct = 0.0
    
    # List unused tags
    unused_tags = sorted(list(valid_tags - found_tags))
    if unused_tags:
        print(f"\nUNUSED VALID TAGS: {len(unused_tags)}/{len(valid_tags)}")
        for tag in unused_tags:
            print(f"  - {tag}")
        
    # Output undefined tags
    if undefined_tags:
        print(f"\nUNDEFINED TAGS (not in tags.json): {len(undefined_tags)}")
        for tag in undefined_tags:
            print(f"  - {tag}")
    
    print(f"\n" + "="*60)
    print(f"OVERALL TAG COVERAGE: {len(used_valid_tags)}/{len(valid_tags)} tags used ({coverage_pct:.1f}%)")
    print("="*60)

if __name__ == "__main__":
    main()
