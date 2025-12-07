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

generate-flashcards:
	@echo "Generating flashcards from docs (all files, resumable)..."
	@uv run scripts/generate_flashcards_from_docs.py --model gemini-3-pro-preview --resume
# incase you want to limit the number of generated flashcards for testing purposes, uncomment the following line and comment the above line
# 	@uv run scripts/generate_flashcards_from_docs.py --limit 5 --model gemini-3-pro-preview

publish:
	@echo "Publishing flashcards to Anki..."
	@uv run scripts/publish_anki_deck.py

start-webapp:
	@echo "Attempting to kill previous server process (if any)..."
	@pkill -f "uv run server.py" || true
	@echo "Starting server..."
	@cd flashcard-app && uv run server.py