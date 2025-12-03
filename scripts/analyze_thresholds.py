import csv
import os
import statistics

SIMILARITY_FILE = "similarity_scores.csv"

def analyze():
    # Handle paths
    base_dir = os.getcwd()
    if os.path.basename(base_dir) == "scripts":
        base_dir = os.path.dirname(base_dir)
    
    path = os.path.join(base_dir, SIMILARITY_FILE)
    
    if not os.path.exists(path):
        print("File not found.")
        return

    scores = []
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                scores.append(float(row['similarity_score']))
            except ValueError:
                continue
    
    if not scores:
        print("No scores found.")
        return

    scores.sort(reverse=True)
    count = len(scores)
    
    print(f"Total Pairs: {count}")
    print(f"Max Score: {max(scores):.4f}")
    print(f"Min Score: {min(scores):.4f}")
    print("-" * 20)
    print("Percentiles (Score required to be in top X%):")
    print(f"Top 0.1%: {scores[int(count * 0.001)]:.4f}")
    print(f"Top 1%:   {scores[int(count * 0.01)]:.4f}")
    print(f"Top 5%:   {scores[int(count * 0.05)]:.4f}")
    print(f"Top 10%:  {scores[int(count * 0.10)]:.4f}")
    print(f"Median:   {statistics.median(scores):.4f}")
    print("-" * 20)
    print("Distribution counts:")
    print(f"> 0.99: {sum(1 for s in scores if s >= 0.99)}")
    print(f"> 0.95: {sum(1 for s in scores if s >= 0.95)}")
    print(f"> 0.90: {sum(1 for s in scores if s >= 0.90)}")
    print(f"> 0.85: {sum(1 for s in scores if s >= 0.85)}")

if __name__ == "__main__":
    analyze()
