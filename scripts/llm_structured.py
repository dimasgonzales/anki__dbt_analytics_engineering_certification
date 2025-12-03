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
    principle_ref: str | None = Field(None, description="The specific principle this card tests (if applicable)")


class CardPrediction(BaseModel):
    card_index: int = Field(..., ge=1, description="1-based index of the card in the batch")
    tags: list[TagResult] = Field(default_factory=list)


class BatchPrediction(BaseModel):
    cards: list[CardPrediction] = Field(default_factory=list)


class CardClassification(BaseModel):
    card_index: int = Field(..., ge=1, description="1-based index of the card in the batch")
    card_type: str = Field(..., description="Type of card: 'Factual' or 'Scenario'")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score between 0 and 1")
    reason: str = Field(..., min_length=1, description="Short explanation for the classification")


class ClassificationBatch(BaseModel):
    cards: list[CardClassification] = Field(default_factory=list)


async def generate_tag_batch(prompt: str, model_name: str, api_key: str | None = None) -> BatchPrediction:
    """Call DeepSeek API to obtain structured tag predictions."""
    
    api_key = api_key or os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError("DeepSeek API key required")
    
    from openai import AsyncOpenAI
    client = AsyncOpenAI(api_key=api_key, base_url="https://api.deepseek.com", timeout=60.0)
    
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
                                    "reason": {"type": "string"},
                                    "principle_ref": {"type": "string"}
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
    
    response = await client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "user", "content": schema_prompt}
        ],
        response_format={"type": "json_object"},
        temperature=0.3
    )
    
    response_text = response.choices[0].message.content
    return _parse_batch_prediction(response_text)


async def classify_card_batch(prompt: str, model_name: str, api_key: str | None = None) -> ClassificationBatch:
    """Call DeepSeek API to obtain structured card classifications."""
    
    api_key = api_key or os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError("DeepSeek API key required")
    
    from openai import AsyncOpenAI
    client = AsyncOpenAI(api_key=api_key, base_url="https://api.deepseek.com", timeout=60.0)
    
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
                        "card_type": {"type": "string", "enum": ["Factual", "Scenario"]},
                        "confidence": {"type": "number", "minimum": 0, "maximum": 1},
                        "reason": {"type": "string"}
                    },
                    "required": ["card_index", "card_type", "confidence", "reason"]
                }
            }
        },
        "required": ["cards"]
    }, indent=2)
    
    response = await client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "user", "content": schema_prompt}
        ],
        response_format={"type": "json_object"},
        temperature=0.3
    )
    
    response_text = response.choices[0].message.content
    return _parse_classification_batch(response_text)


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


def _parse_classification_batch(raw: Any) -> ClassificationBatch:
    """Convert the OpenAI response into a ClassificationBatch instance."""

    if isinstance(raw, ClassificationBatch):
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

    sanitized = _sanitize_classification_payload(payload)
    return ClassificationBatch.model_validate(sanitized)


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
            if "principle_ref" in tag and tag["principle_ref"]:
                 cleaned_tag["principle_ref"] = str(tag["principle_ref"])
            
            cleaned_tags.append(cleaned_tag)

        cleaned_card = {"card_index": normalized_idx, "tags": cleaned_tags}
            
        cleaned_cards.append(cleaned_card)

    if mutated:
        print("[warn] Sanitized invalid structured LLM response", file=sys.stderr)

    return {"cards": cleaned_cards}


def _sanitize_classification_payload(payload: dict[str, Any]) -> dict[str, Any]:
    """Clamp invalid fields for classification."""

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

        card_type = card.get("card_type")
        if card_type not in ("Factual", "Scenario"):
            # Default to Factual if invalid, or skip? Let's skip to be safe, or maybe default.
            # But the schema requires it. Let's pick Factual as safe default if missing/invalid, 
            # but actually let's just drop the card if it's garbage.
            mutated = True
            continue

        conf_raw = card.get("confidence", 0.0)
        try:
            confidence = float(conf_raw)
        except (TypeError, ValueError):
            confidence = 0.0
        clamped_conf = min(1.0, max(0.0, confidence))

        reason = str(card.get("reason", "No reason provided"))

        cleaned_cards.append({
            "card_index": normalized_idx,
            "card_type": card_type,
            "confidence": clamped_conf,
            "reason": reason
        })

    if mutated:
        print("[warn] Sanitized invalid structured LLM classification response", file=sys.stderr)

    return {"cards": cleaned_cards}
