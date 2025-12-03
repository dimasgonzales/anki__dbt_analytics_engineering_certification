# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "rich",
# ]
# ///

import json
import os
import sys
from collections import defaultdict
from rich.console import Console
from rich.table import Table
from rich import box

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

def parse_card_data(file_path):
    """Extract tags and card_type from frontmatter."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    tags = []
    card_type = "Unknown"
    
    # Extract frontmatter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter = parts[1]
            lines = frontmatter.split('\n')
            
            in_tags_section = False
            
            for line in lines:
                stripped_line = line.strip()
                if not stripped_line:
                    continue
                
                # Extract Tags
                if stripped_line.startswith('tags:'):
                    in_tags_section = True
                    continue
                    
                if in_tags_section:
                    if stripped_line.startswith('-'):
                        tag = stripped_line.lstrip('- ').strip()
                        tags.append(tag)
                        # Check for card_type tag
                        if tag.startswith('card_type/'):
                            # Extract type, e.g., "factual" from "card_type/factual"
                            # Capitalize to match "Factual"/"Scenario" convention if desired, 
                            # or keep as is. The previous script used "Factual"/"Scenario" (Title Case).
                            # Let's title case it to be safe and consistent with previous output.
                            ctype = tag.split('/', 1)[1]
                            card_type = ctype.title() 
                    elif ':' in stripped_line:
                        in_tags_section = False
                        
    return tags, card_type

def main():
    console = Console()
    root_dir = get_project_root()
    deck_dir = os.path.join(root_dir, 'deck')
    
    if not os.path.exists(deck_dir):
        console.print(f"[bold red]Error:[/bold red] deck directory not found at {deck_dir}")
        sys.exit(1)

    valid_tags, parent_to_children = load_valid_tags(root_dir)
    
    # Data Aggregation
    # tag -> set of filenames
    tag_to_cards = defaultdict(set)
    # filename -> card_type
    card_types = {}
    
    total_cards = 0
    untagged_cards = []
    found_tags = set()
    
    # Iterate over .md files
    for filename in os.listdir(deck_dir):
        if filename.endswith('.md'):
            total_cards += 1
            file_path = os.path.join(deck_dir, filename)
            file_tags, card_type = parse_card_data(file_path)
            
            card_types[filename] = card_type
            found_tags.update(file_tags)
            
            if not file_tags:
                untagged_cards.append(filename)
            
            for tag in file_tags:
                tag_to_cards[tag].add(filename)

    # --- Visualization ---
    
    console.print("\n[bold blue]Anki Sandbox - Tag Coverage[/bold blue]\n")
    
    # Create Main Table
    table = Table(box=box.SIMPLE_HEAD)
    table.add_column("Tag", style="cyan", no_wrap=True)
    table.add_column("Total", justify="right", style="white")
    table.add_column("% Deck", justify="right", style="green")
    table.add_column("Factual", justify="right", style="blue")
    table.add_column("Scenario", justify="right", style="magenta")

    def get_stats(filenames):
        count = len(filenames)
        factual = sum(1 for f in filenames if card_types.get(f) == 'Factual')
        scenario = sum(1 for f in filenames if card_types.get(f) == 'Scenario')
        return count, factual, scenario

    def fmt_pct(val, total):
        if not val or not total: return "-"
        pct = (val / total) * 100
        return f"{val} ({pct:.0f}%)"
    
    def fmt_deck_pct(val, total_deck):
        if not val or not total_deck: return "-"
        pct = (val / total_deck) * 100
        return f"{pct:.1f}%"

    # Sort parents
    for parent in sorted(parent_to_children.keys()):
        # Aggregate Parent Stats
        parent_cards = set()
        for child in parent_to_children[parent]:
            parent_cards.update(tag_to_cards.get(child, set()))
            
        p_count, p_factual, p_scenario = get_stats(parent_cards)
        
        # Add Parent Row
        table.add_row(
            f"[bold]{parent}[/bold]",
            str(p_count),
            fmt_deck_pct(p_count, total_cards),
            fmt_pct(p_factual, p_count),
            fmt_pct(p_scenario, p_count)
        )
        
        # Sort children
        for child in sorted(parent_to_children[parent]):
            child_cards = tag_to_cards.get(child, set())
            if child_cards:
                c_count, c_factual, c_scenario = get_stats(child_cards)
                
                table.add_row(
                    f"  {child}",
                    str(c_count),
                    fmt_deck_pct(c_count, total_cards),
                    fmt_pct(c_factual, c_count),
                    fmt_pct(c_scenario, c_count)
                )
            else:
                table.add_row(f"  [dim]{child}[/dim]", "0", "-", "-", "-")
        
        # Add empty row for spacing
        table.add_row("", "", "", "", "")

    console.print(table)
    
    # Summary Section
    console.print("\n[bold]Summary Statistics[/bold]")
    summary_table = Table(box=box.SIMPLE, show_header=False)
    summary_table.add_column("Metric", style="cyan")
    summary_table.add_column("Value", style="white")
    
    used_valid_tags = found_tags.intersection(valid_tags)
    coverage_pct = (len(used_valid_tags) / len(valid_tags) * 100) if valid_tags else 0
    
    summary_table.add_row("Total Cards", str(total_cards))
    summary_table.add_row("Untagged Cards", f"{len(untagged_cards)} ({len(untagged_cards)/total_cards*100:.1f}%)" if total_cards else "0")
    summary_table.add_row("Tag Coverage", f"{len(used_valid_tags)}/{len(valid_tags)} ({coverage_pct:.1f}%)")
    
    console.print(summary_table)
    
    # Untagged Cards List
    if untagged_cards:
        console.print(f"\n[bold red]Untagged Cards ({len(untagged_cards)}):[/bold red]")
        for card in untagged_cards:
            console.print(f"  - deck/{card}")

    # Undefined Tags
    undefined_tags = sorted([t for t in (found_tags - valid_tags) if not t.startswith('card_type/')])
    if undefined_tags:
        console.print(f"\n[bold red]Undefined Tags ({len(undefined_tags)}):[/bold red]")
        for tag in undefined_tags:
            console.print(f"  - {tag}")

if __name__ == "__main__":
    main()
