.PHONY: clean-deck dbt-deck

clean:
	@echo "Removing existing Markdown files from deck/..."
	@find deck -type f -name "*.md" -delete

dbt-deck:
	@deck=$$(ls -1t decks/dbt_deck*.json 2>/dev/null | head -n1); \
	if [ -z "$$deck" ]; then echo "No dbt deck found in decks/"; exit 1; fi; \
	echo "Using deck: $$deck"; \
	uv run scripts/anki_to_markdown.py --in "$$deck"


run: clean dbt-deck
	echo "Running preview_deck.py on generated markdown files..."