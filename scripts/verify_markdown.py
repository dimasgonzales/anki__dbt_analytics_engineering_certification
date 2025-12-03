# /// script
# dependencies = [
#   "genanki",
#   "pyyaml",
#   "markdown",
#   "Pygments",
# ]
# ///

import sys
import os

# Add current directory to path so we can import from scripts
sys.path.append(os.getcwd())

from scripts.publish_anki_deck import parse_flashcard

def main():
    card_path = 'deck/test_card_code.md'
    if not os.path.exists(card_path):
        print(f"Error: {card_path} not found")
        return

    data = parse_flashcard(card_path)
    if data:
        print("Answer HTML:")
        print(data['answer'])
    else:
        print("Failed to parse card")

if __name__ == "__main__":
    main()
