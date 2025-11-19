#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "google-genai>=0.4.0",
#     "python-dotenv>=1.0.1",
# ]
# ///
"""Rewrite long Anki answers into concise bullet lists via the Gemini SDK."""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Tuple

from dotenv import load_dotenv
from google import genai
from google.genai import types

Deck = Dict[str, Any]
DEFAULT_MODEL = "gemini-2.5-flash"
SYSTEM_PROMPT = (
    "You help learners clean up verbose flashcard answers. "
    "Rewrite each answer as a short HTML unordered list (<ul><li>...</li></ul>) with no code fences. "
    "Preserve factual content, math, and inline HTML tags. Use at most 5 bullet points unless detail is critical."
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Rewrite long answers inside an Anki / CrowdAnki JSON deck so that "
            "Back fields become concise bullet lists."
        )
    )
    parser.add_argument("--deck", default="dbt/deck.json", help="Path to the source deck JSON.")
    parser.add_argument(
        "--output",
        default=None,
        help=(
            "Destination path for the updated deck. If omitted, writes beside the input deck "
            "using a timestamped file name."
        ),
    )
    parser.add_argument(
        "--field-index",
        type=int,
        default=1,
        help="Fields index to rewrite (default: 1 for Back side).",
    )
    parser.add_argument(
        "--min-chars",
        type=int,
        default=220,
        help="Only rewrite answers whose stripped length meets or exceeds this value.",
    )
    parser.add_argument(
        "--max-notes",
        type=int,
        default=None,
        help="Limit the number of notes rewritten during a run (default: unlimited).",
    )
    parser.add_argument(
        "--model",
        default=None,
        help="Override model name (else GEMINI_MODEL env or gemini-2.5-flash).",
    )
    parser.add_argument(
        "--base-url",
        default=None,
        help="(Ignored) Gemini SDK uses the Google-hosted endpoint.",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.4,
        help="Sampling temperature passed to the chat completion call.",
    )
    parser.add_argument(
        "--max-retries",
        type=int,
        default=4,
        help="Maximum retries on transient API failures.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show which notes would change without writing any files.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Rewrite even if the answer already looks like bullet points.",
    )
    return parser.parse_args()


def ensure_client(base_url: str | None, model_override: str | None) -> Tuple[genai.Client, str]:
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise SystemExit("Missing GEMINI_API_KEY. Add it to your environment or .env file.")
    if base_url:
        print("google-genai does not support custom base URLs; ignoring --base-url", file=sys.stderr)
    model = model_override or os.getenv("GEMINI_MODEL") or DEFAULT_MODEL
    client = genai.Client(api_key=api_key)
    return client, model


def load_deck(path: Path) -> Deck:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def save_deck(path: Path, deck: Deck) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(deck, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def default_output_path(deck_path: Path) -> Path:
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    new_name = f"{deck_path.stem}-{timestamp}{deck_path.suffix}"
    return deck_path.with_name(new_name)


def looks_bulleted(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return False
    lowered = stripped.lower()
    if "<ul" in lowered or "<ol" in lowered:
        return True
    lines = [line.strip() for line in stripped.splitlines()]
    bullet_lines = sum(1 for line in lines if line.startswith(("-", "*", "•")))
    return bullet_lines >= max(2, len(lines) // 2) if lines else False


def needs_rewrite(text: str, min_chars: int, force: bool) -> bool:
    stripped = text.strip()
    if force:
        return bool(stripped)
    if len(stripped) < min_chars:
        return False
    return not looks_bulleted(stripped)


def rewrite_answer(
    client: genai.Client,
    model: str,
    answer: str,
    temperature: float,
    max_retries: int,
) -> str:
    user_prompt = (
        "Rewrite the following flashcard answer as a concise HTML unordered list. "
        "Do not include introductory sentences, conclusions, or code fences.\n\n"
        "Answer to rewrite:\n" + answer.strip()
    )
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model=model,
                contents=user_prompt,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT,
                    temperature=temperature,
                ),
            )
            content = response.text or ""
            return content.strip()
        except Exception as exc:  # retry on transient faults
            if attempt == max_retries - 1:
                raise
            backoff = 2 ** attempt
            print(f"⚠ Gemini API error ({exc}); retry {attempt + 1}/{max_retries} in {backoff}s...", file=sys.stderr, flush=True)
            time.sleep(backoff)
    return answer


def process_deck(
    deck: Deck,
    client: genai.Client | None,
    model: str,
    field_index: int,
    min_chars: int,
    max_notes: int | None,
    temperature: float,
    max_retries: int,
    dry_run: bool,
    force: bool,
) -> Tuple[int, int]:
    notes = deck.get("notes")
    if not isinstance(notes, list):
        raise SystemExit("Deck JSON is missing a notes array.")

    total_candidates = 0
    rewritten = 0

    for idx, note in enumerate(notes):
        fields = note.get("fields")
        if not isinstance(fields, list) or len(fields) <= field_index:
            continue
        original = str(fields[field_index] or "")
        if not needs_rewrite(original, min_chars, force):
            continue
        total_candidates += 1
        if max_notes is not None and rewritten >= max_notes:
            break
        if dry_run:
            rewritten += 1
            preview = original.strip()
            preview_len = len(preview)
            print(
                f"[dry-run] Note {idx}: would rewrite ~{preview_len} chars (field {field_index})."
            )
            continue
        if client is None:
            raise RuntimeError("OpenAI client is not initialized; rerun without --dry-run.")
        print(f"Rewriting note {idx} ({rewritten + 1}/{len([n for n in notes if isinstance(n.get('fields'), list) and len(n['fields']) > field_index and needs_rewrite(str(n['fields'][field_index] or ''), min_chars, force)])} candidates, ~{len(original.strip())} chars)...", flush=True)
        new_answer = rewrite_answer(
            client=client,
            model=model,
            answer=original,
            temperature=temperature,
            max_retries=max_retries,
        )
        if not new_answer:
            continue
        rewritten += 1
        fields[field_index] = new_answer
        print(f"✓ Note {idx} rewritten successfully", flush=True)
        # Rate limit: brief pause between API calls to reduce server load
        time.sleep(0.5)

    return total_candidates, rewritten


def main() -> None:
    args = parse_args()
    deck_path = Path(args.deck)
    if not deck_path.exists():
        raise SystemExit(f"Deck not found: {deck_path}")
    output_path = Path(args.output) if args.output else default_output_path(deck_path)

    if args.dry_run:
        load_dotenv()
        model = args.model or os.getenv("GEMINI_MODEL") or DEFAULT_MODEL
        client = None
    else:
        client, model = ensure_client(args.base_url, args.model)
    deck = load_deck(deck_path)

    candidates, rewritten = process_deck(
        deck=deck,
        client=client,
        model=model,
        field_index=args.field_index,
        min_chars=args.min_chars,
        max_notes=args.max_notes,
        temperature=args.temperature,
        max_retries=args.max_retries,
        dry_run=args.dry_run,
        force=args.force,
    )

    if args.dry_run:
        print(f"Dry run complete: {candidates} candidates, {rewritten} would change.")
        return

    if rewritten:
        save_deck(output_path, deck)
        print(
            f"Updated deck saved to {output_path} (rewrote {rewritten} of {candidates} candidates using model {model})."
        )
    else:
        print("No answers met the rewrite criteria; nothing changed.")


if __name__ == "__main__":
    main()
