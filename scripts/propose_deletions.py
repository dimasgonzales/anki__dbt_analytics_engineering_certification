import csv
import json
import os
import sys

# Configuration
SIMILARITY_FILE = "similarity_scores.csv"
OUTPUT_FILE = "proposed_deletions.json"

def propose_deletions():
    # Determine paths
    # Assuming script is run from project root or scripts/
    base_dir = os.getcwd()
    if os.path.basename(base_dir) == "scripts":
        base_dir = os.path.dirname(base_dir)
    
    similarity_path = os.path.join(base_dir, SIMILARITY_FILE)
    output_path = os.path.join(base_dir, OUTPUT_FILE)
    
    if not os.path.exists(similarity_path):
        print(f"Error: {similarity_path} not found.")
        return

    print(f"Reading {similarity_path}...")
    
    pairs = []
    with open(similarity_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            pairs.append({
                "card_1": row['card_1'],
                "card_2": row['card_2'],
                "score": float(row['similarity_score'])
            })
    
    # Sort by score descending (highest similarity first)
    pairs.sort(key=lambda x: x['score'], reverse=True)
    
    deleted_cards = set()
    proposed_deletions = []
    
    print("Processing pairs (Greedy Liveness Strategy)...")
    
    for pair in pairs:
        c1 = pair['card_1']
        c2 = pair['card_2']
        score = pair['score']
        
        # If either is already marked for deletion, we can't use this pair
        # to justify deleting the other (transitive property safety).
        if c1 in deleted_cards or c2 in deleted_cards:
            continue
            
        # Both are "alive". We found a high similarity pair.
        # We need to pick one to delete.
        # Heuristic: Delete the one with the longer filename? Or just arbitrary c2?
        # Let's arbitrarily delete c2 (the second one in the pair).
        # In a real scenario, we might check which one has more tags, etc.
        # For now, we'll keep c1 and delete c2.
        
        to_delete = c2
        kept = c1
        
        deleted_cards.add(to_delete)
        proposed_deletions.append({
            "filename": to_delete,
            "reason": f"High similarity ({score:.4f}) to {kept}",
            "kept_filename": kept,
            "score": score
        })

    print(f"Found {len(proposed_deletions)} cards to prune.")
    
    with open(output_path, 'w') as f:
        json.dump(proposed_deletions, f, indent=2)
        
    print(f"Wrote proposed deletions to {output_path}")

if __name__ == "__main__":
    propose_deletions()
