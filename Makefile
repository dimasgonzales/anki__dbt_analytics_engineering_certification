purge:
	@echo "Removing existing Markdown files from deck/..."
	@find deck -type f -name "*.md" -delete

extract-dbt-deck: purge
	@deck=$$(ls -1t docs/dbt*.apkg 2>/dev/null | head -n1); \
	if [ -z "$$deck" ]; then echo "No dbt .apkg file found in docs/"; exit 1; fi; \
	echo "Using deck: $$deck"; \
	uv run scripts/extract_anki_to_markdown.py --in "$$deck"


extract: purge extract-dbt-deck
	@echo "Orchestrating markdown extraction from anki deck..."

auto-tag:
	@echo "Auto-tagging flashcards..."
	@uv run scripts/auto_tagger.py --strategy hybrid

auto-tag-keyword:
	@echo "Auto-tagging flashcards (keyword only)..."
	@uv run scripts/auto_tagger.py --strategy keyword

auto-tag-llm:
	@echo "Auto-tagging flashcards (LLM only)..."
	@uv run scripts/auto_tagger.py --strategy llm

coverage:
	@echo "Generating tag coverage report..."
	@uv run scripts/tag_coverage.py