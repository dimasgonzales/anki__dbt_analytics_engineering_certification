from __future__ import annotations

import json
import sys
from typing import Any

from openai import AsyncOpenAI
from outlines import Generator, models, types
from pydantic import BaseModel, Field


class TagResult(BaseModel):
    tag: str = Field(..., min_length=1, description="Child tag identifier from tags.json")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score between 0 and 1")
    reason: str = Field(..., min_length=1, description="Short explanation for the tag")


class CardPrediction(BaseModel):
    card_index: int = Field(..., ge=1, description="1-based index of the card in the batch")
    tags: list[TagResult] = Field(default_factory=list)


class BatchPrediction(BaseModel):
    cards: list[CardPrediction] = Field(default_factory=list)


async def generate_tag_batch(prompt: str, llm_url: str, model_name: str) -> BatchPrediction:
    """Call an OpenAI-compatible endpoint via Outlines to obtain structured tag predictions."""

    client = AsyncOpenAI(api_key="not-needed", base_url=llm_url)
    async_model = models.AsyncOpenAI(client, model_name=model_name)
    schema = types.json_schema(BatchPrediction)
    generator = Generator(async_model, schema)

    raw_response = await generator(prompt)
    return _parse_batch_prediction(raw_response)


def _parse_batch_prediction(raw: Any) -> BatchPrediction:
    """Convert the OpenAI response into a BatchPrediction instance."""

    if isinstance(raw, BatchPrediction):
        return raw
    payload: dict[str, Any]
    if isinstance(raw, dict):
        payload = raw
    elif isinstance(raw, list):
        raw = _collapse_fragments(raw)
        payload = _loads_json(raw)
    elif isinstance(raw, str):
        payload = _loads_json(raw)
    else:
        raise TypeError(f"Unexpected LLM response type: {type(raw)!r}")

    sanitized = _sanitize_payload(payload)
    return BatchPrediction.model_validate(sanitized)


def _collapse_fragments(fragments: list[Any]) -> str:
    """Flatten OpenAI content fragments into a single JSON string."""

    parts: list[str] = []
    for fragment in fragments:
        if isinstance(fragment, str):
            parts.append(fragment)
        elif isinstance(fragment, dict):
            if "text" in fragment:
                parts.append(str(fragment["text"]))
            elif "content" in fragment:
                parts.append(str(fragment["content"]))
        else:
            parts.append(str(fragment))
    return "".join(parts)


def _loads_json(blob: str) -> dict[str, Any]:
    try:
        parsed = json.loads(blob)
    except json.JSONDecodeError as err:
        raise ValueError("LLM response is not valid JSON") from err
    if not isinstance(parsed, dict):
        raise TypeError("Structured response must decode to a JSON object")
    return parsed


def _sanitize_payload(payload: dict[str, Any]) -> dict[str, Any]:
    """Clamp invalid fields so Pydantic validation isn't tripped by bad generations."""

    cards = payload.get("cards", [])
    if not isinstance(cards, list):
        return {"cards": []}

    cleaned_cards: list[dict[str, Any]] = []
    mutated = False

    for card in cards:
        if not isinstance(card, dict):
            mutated = True
            continue

        idx_raw = card.get("card_index", 1)
        try:
            idx = int(idx_raw)
        except (TypeError, ValueError):
            idx = 1
        normalized_idx = max(1, idx)
        if normalized_idx != idx:
            mutated = True

        raw_tags = card.get("tags", [])
        if not isinstance(raw_tags, list):
            mutated = True
            raw_tags = []

        cleaned_tags: list[dict[str, Any]] = []
        for tag in raw_tags:
            if not isinstance(tag, dict):
                mutated = True
                continue
            tag_name = tag.get("tag")
            if not tag_name:
                mutated = True
                continue

            conf_raw = tag.get("confidence", 0.0)
            try:
                confidence = float(conf_raw)
            except (TypeError, ValueError):
                confidence = 0.0
            clamped_conf = min(1.0, max(0.0, confidence))
            if clamped_conf != confidence:
                mutated = True

            cleaned_tag = {
                **tag,
                "tag": str(tag_name),
                "confidence": clamped_conf,
            }
            cleaned_tags.append(cleaned_tag)

        cleaned_cards.append({"card_index": normalized_idx, "tags": cleaned_tags})

    if mutated:
        print("[warn] Sanitized invalid structured LLM response", file=sys.stderr)

    return {"cards": cleaned_cards}
