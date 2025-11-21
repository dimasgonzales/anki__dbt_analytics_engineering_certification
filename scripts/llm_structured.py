from __future__ import annotations

import json
import os
import sys
from typing import Any

from google import genai
from google.genai import types as genai_types
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


async def generate_tag_batch(prompt: str, model_name: str, api_key: str | None = None) -> BatchPrediction:
    """Call Google Gemini API to obtain structured tag predictions."""
    
    api_key = api_key or os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Gemini API key required")
    
    client = genai.Client(api_key=api_key)
    
    # Build the prompt with JSON schema instructions
    schema_prompt = prompt + "\n\nRespond ONLY with valid JSON matching this schema:\n" + json.dumps({
        "type": "object",
        "properties": {
            "cards": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "card_index": {"type": "integer", "minimum": 1},
                        "tags": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "tag": {"type": "string"},
                                    "confidence": {"type": "number", "minimum": 0, "maximum": 1},
                                    "reason": {"type": "string"}
                                },
                                "required": ["tag", "confidence", "reason"]
                            }
                        }
                    },
                    "required": ["card_index", "tags"]
                }
            }
        },
        "required": ["cards"]
    }, indent=2)
    
    contents = [
        genai_types.Content(
            role="user",
            parts=[genai_types.Part.from_text(text=schema_prompt)],
        ),
    ]
    
    config = genai_types.GenerateContentConfig(
        temperature=0.3,
        response_mime_type="application/json",
    )
    
    # Collect streaming response
    response_text = ""
    stream = await client.aio.models.generate_content_stream(
        model=model_name,
        contents=contents,
        config=config,
    )
    async for chunk in stream:
        if chunk.text:
            response_text += chunk.text
    
    return _parse_batch_prediction(response_text)


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
