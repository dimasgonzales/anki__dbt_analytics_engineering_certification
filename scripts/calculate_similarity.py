# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pandas",
#     "numpy",
#     "sentence-transformers",
#     "scikit-learn",
# ]
# ///

import os
import re
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import glob

# Configuration
DECK_DIR = "deck"
MODEL_NAME = "all-MiniLM-L6-v2"
OUTPUT_FILE = "similarity_scores.csv"

def parse_flashcard(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract front
    front_match = re.search(r'<front>(.*?)</front>', content, re.DOTALL)
    front_text = front_match.group(1).strip() if front_match else ""
    
    # Extract back
    back_match = re.search(r'<back>(.*?)</back>', content, re.DOTALL)
    back_text = back_match.group(1).strip() if back_match else ""
    
    # Extract UUID if needed, or just use filename
    filename = os.path.basename(filepath)
    
    return {
        "filename": filename,
        "front": front_text,
        "back": back_text,
        "full_text": f"{front_text} {back_text}"
    }

def main():
    print("Loading flashcards...")
    # Use absolute path for deck dir if running from root
    deck_path = os.path.abspath(DECK_DIR)
    flashcard_files = glob.glob(os.path.join(deck_path, "*.md"))
    
    flashcards = []
    for filepath in flashcard_files:
        try:
            card_data = parse_flashcard(filepath)
            if card_data["full_text"].strip(): # Only add if there is text
                flashcards.append(card_data)
        except Exception as e:
            print(f"Error parsing {filepath}: {e}")
            
    df = pd.DataFrame(flashcards)
    print(f"Loaded {len(df)} flashcards.")
    
    if len(df) == 0:
        print("No flashcards found.")
        return

    print(f"Loading model {MODEL_NAME}...")
    model = SentenceTransformer(MODEL_NAME)
    
    print("Generating embeddings...")
    embeddings = model.encode(df['full_text'].tolist(), show_progress_bar=True)
    
    print("Calculating similarity matrix...")
    similarity_matrix = cosine_similarity(embeddings)
    
    # Create a DataFrame for the similarity matrix
    sim_df = pd.DataFrame(similarity_matrix, index=df['filename'], columns=df['filename'])
    
    # We can also find the top N similar cards for each card
    print("Finding unique pairwise similarities...")
    
    results = []
    filenames = df['filename'].tolist()
    num_files = len(filenames)
    
    # Iterate through upper triangle of the matrix (excluding diagonal)
    for i in range(num_files):
        for j in range(i + 1, num_files):
            score = similarity_matrix[i][j]
            results.append({
                "card_1": filenames[i],
                "card_2": filenames[j],
                "similarity_score": score
            })
            
    results_df = pd.DataFrame(results)
    # Sort by similarity score descending
    results_df = results_df.sort_values(by="similarity_score", ascending=False)
    results_df.to_csv(OUTPUT_FILE, index=False)
    print(f"Similarity scores saved to {OUTPUT_FILE}")
    
    # Also save the full matrix if needed, but it might be large. 
    # For now, just the pairwise list is probably more useful for analysis.

if __name__ == "__main__":
    main()
