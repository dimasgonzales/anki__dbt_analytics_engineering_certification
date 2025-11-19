# Anki Deck for dbt Analytics Engineering Certification

This repo mantains the flashcards to study for dbtLabs's "dbt Analytics Engineering Certification". The repo keeps the flashcards as markdown files in the `deck` directory.

It has utilitities for 
- automatic anki deck creation, apgk generation
- tag coverage analysis
- automatic tagger for flashcards
- flashcard claims authenticator

# Usage

## Auto-tagging Flashcards

Automatically assign hierarchical tags to flashcards based on content analysis:

```bash
# Hybrid strategy (keyword + LLM fallback, recommended)
make auto-tag

# Keyword-only (fast, deterministic)
make auto-tag-keyword

# LLM-only (slow, most accurate)
make auto-tag-llm

# Preview changes without modifying files
make auto-tag-dry

# Check tag coverage after tagging
make tag-report
```

**Strategies:**
- `keyword`: Fast matching against tag keywords (< 1 sec, 60-75% accuracy)
- `llm`: Semantic understanding via local LLM at localhost:1234 (2-5 min, 85-95% accuracy)
- `hybrid`: Keyword first, LLM fallback for low confidence (30 sec - 2 min, 80-90% accuracy)

**Advanced usage:**
```bash
# Custom threshold for hybrid mode
uv run scripts/auto_tagger.py --strategy hybrid --threshold 0.4

# Adjust max tags per card
uv run scripts/auto_tagger.py --max-tags 2

# Use different LLM endpoint
uv run scripts/auto_tagger.py --llm-url http://localhost:1234/v1
```

# TODO

- [ ] create a process to prune/remove duplicate flashcards
- [x] automatic tagger