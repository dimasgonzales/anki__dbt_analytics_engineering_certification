# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "openai",
#     "pydantic",
#     "python-dotenv",
#     "pyyaml",
# ]
# ///

import csv
import os
import argparse
import sys
import json
import hashlib
import asyncio
import yaml
import re
from typing import Optional, Any, List, Dict, Set
from openai import AsyncOpenAI
from pydantic import BaseModel, Field, field_validator
from dotenv import load_dotenv
import logging

load_dotenv()

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

# Configuration
DEFAULT_SIMILARITY_FILE = "similarity_scores.csv"
DEFAULT_DECK_DIR = "deck"
CACHE_FILE = ".llm_cache.json"
BATCH_SIZE = 10
# DEFAULT_MODEL = "gemini-2.0-flash-exp"
DEFAULT_MODEL = "deepseek-chat"
DEFAULT_CONCURRENCY = 1

# --- Pydantic Models ---

class JudgeResult(BaseModel):
    pair_id: str = Field(..., description="The unique identifier for the pair (e.g., 'card1.md|card2.md').")
    is_same_question: bool = Field(..., description="True if the cards are essentially the same question, False otherwise.")
    reason: str = Field(..., description="Reasoning for the decision.")
    best_card_index: Optional[int] = Field(None, description="1 for card_1, 2 for card_2. Required if is_same_question is True.")

class BatchJudgeResult(BaseModel):
    results: List[JudgeResult]

class RewriteResult(BaseModel):
    card_1_new_content: str | dict = Field(..., description="Rewritten content for card 1.")
    card_2_new_content: str | dict = Field(..., description="Rewritten content for card 2.")
    reason: str = Field(..., description="Explanation of how they were made distinct.")

    @field_validator('card_1_new_content', 'card_2_new_content', mode='before')
    @classmethod
    def handle_dict_content(cls, v):
        if isinstance(v, dict):
            # Attempt to reconstruct if it has front/back
            if 'front' in v and 'back' in v:
                return f"<front>\n{v['front']}\n</front>\n\n---\n\n<back>\n{v['back']}\n</back>"
            # Fallback for other dicts? just dump json?
            return json.dumps(v)
        return v

# --- Cache Helpers ---

class LLMCache:
    def __init__(self, cache_file=CACHE_FILE):
        self.cache_file = cache_file
        self.cache = {}
        self.load()

    def load(self):
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, 'r') as f:
                    self.cache = json.load(f)
            except Exception as e:
                logger.warning(f"Could not load cache: {e}")
                self.cache = {}

    def save(self):
        try:
            with open(self.cache_file, 'w') as f:
                json.dump(self.cache, f, indent=2)
        except Exception as e:
            logger.warning(f"Could not save cache: {e}")

    def get(self, key):
        return self.cache.get(key)

    def set(self, key, value):
        self.cache[key] = value
        # self.save() # Optimization: Don't save on every set

    def flush(self):
        self.save()

    @staticmethod
    def generate_key(content: str) -> str:
        return hashlib.sha256(content.encode('utf-8')).hexdigest()

# --- LLM Helpers ---

def get_api_key():
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        logger.error("DEEPSEEK_API_KEY environment variable not set.")
        sys.exit(1)
    return api_key

def _clean_json_response(text: str) -> str:
    """Clean markdown code blocks from JSON response."""
    text = text.strip()
    if text.startswith("```json"):
        text = text[7:]
    if text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    return text.strip()

# --- Rate Limiter ---



async def call_llm_judge_batch(pairs: List[Dict], cache: LLMCache, model_name: str) -> List[JudgeResult]:
    """
    Process a batch of pairs.
    pairs: List of dicts with keys 'card_1', 'card_2', 'c1_content', 'c2_content'
    """
    api_key = get_api_key()
    client = AsyncOpenAI(api_key=api_key, base_url="https://api.deepseek.com")
    
    # Check cache first
    uncached_pairs = []
    cached_results = []
    
    prompt_parts = []
    
    for p in pairs:
        pair_id = f"{p['card_1']}|{p['card_2']}"
        cache_key = LLMCache.generate_key(f"JUDGE|{p['c1_content']}|{p['c2_content']}")
        
        cached_val = cache.get(cache_key)
        if cached_val:
            try:
                cached_results.append(JudgeResult(**cached_val))
                continue
            except:
                pass # Invalid cache, re-fetch
        
        uncached_pairs.append(p)
        prompt_parts.append(f"""
        Pair ID: {pair_id}
        Card 1:
        ---
        {p['c1_content']}
        ---
        Card 2:
        ---
        {p['c2_content']}
        ---
        """)

    if not uncached_pairs:
        return cached_results

    system_prompt = """
    You are an expert flashcard judge. Compare the following pairs of flashcards.
    For EACH pair, determine if they are essentially asking the same question and testing the same knowledge.
    
    Respond ONLY with valid JSON matching this schema:
    {
        "results": [
            {
                "pair_id": string (MUST match the provided Pair ID),
                "is_same_question": boolean,
                "reason": string,
                "best_card_index": integer (1 or 2, or null if not same)
            }
        ]
    }
    """

    user_prompt = f"""
    Pairs to judge:
    {''.join(prompt_parts)}
    """
    
    try:
        # Simple backoff for rate limits
        response = None
        for attempt in range(5): # Increased retries
            try:
                response = await client.chat.completions.create(
                    model=model_name,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    stream=False
                )
                break
            except Exception as e:
                if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                    wait_time = (2**attempt) + 5 # Add base buffer
                    logger.warning(f"Rate limit hit (Judge), waiting {wait_time}s...")
                    await asyncio.sleep(wait_time)
                else:
                    raise e
        
        if not response:
            raise Exception("Failed after retries")

        text = response.choices[0].message.content
        text = _clean_json_response(text)
        data = json.loads(text, strict=False)
        batch_result = BatchJudgeResult(**data)
        
        # Update cache
        for res in batch_result.results:
            original_pair = next((p for p in uncached_pairs if f"{p['card_1']}|{p['card_2']}" == res.pair_id), None)
            if original_pair:
                cache_key = LLMCache.generate_key(f"JUDGE|{original_pair['c1_content']}|{original_pair['c2_content']}")
                cache.set(cache_key, res.model_dump())
        
        return cached_results + batch_result.results
        
    except Exception as e:
        logger.error(f"LLM Batch Judge failed: {e}")
        return cached_results

async def call_rewrite_routine(card1_content: str, card2_content: str, cache: LLMCache, model_name: str) -> RewriteResult:
    cache_key = LLMCache.generate_key(f"REWRITE|{card1_content}|{card2_content}")
    cached_val = cache.get(cache_key)
    if cached_val:
        try:
            return RewriteResult(**cached_val)
        except:
            pass

    api_key = get_api_key()
    client = AsyncOpenAI(api_key=api_key, base_url="https://api.deepseek.com")
    
    system_prompt = """
    You are an expert flashcard editor. These two flashcards are similar but not identical. 
    Rewrite them to be CLEARER and DISTINCT from each other. Ensure they test different specific angles or details if possible.
    
    Respond ONLY with valid JSON matching this schema:
    {
        "card_1_new_content": string (The FULL raw markdown content of the card),
        "card_2_new_content": string (The FULL raw markdown content of the card),
        "reason": string
    }
    """

    user_prompt = f"""
    Card 1:
    ---
    {card1_content}
    ---
    
    Card 2:
    ---
    {card2_content}
    ---
    """
    
    try:
        response = None
        for attempt in range(5):
            try:
                response = await client.chat.completions.create(
                    model=model_name,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    stream=False
                )
                break
            except Exception as e:
                if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                    wait_time = (2**attempt) + 5
                    logger.warning(f"Rate limit hit (Rewrite), waiting {wait_time}s...")
                    await asyncio.sleep(wait_time)
                else:
                    raise e
        
        if not response:
             raise Exception("Failed after retries")

        text = response.choices[0].message.content
        text = _clean_json_response(text)
        data = json.loads(text, strict=False)
        result = RewriteResult(**data)
        
        cache.set(cache_key, result.model_dump())
        return result
    except Exception as e:
        logger.error(f"LLM Rewrite failed: {e}")
        return RewriteResult(card_1_new_content=card1_content, card_2_new_content=card2_content, reason=f"LLM Error: {e}")

# --- Main Logic ---

def read_card_content(deck_path, filename):
    path = os.path.join(deck_path, filename)
    if not os.path.exists(path):
        return None
    with open(path, 'r') as f:
        return f.read()

def write_card_content(deck_path, filename, content):
    path = os.path.join(deck_path, filename)
    with open(path, 'w') as f:
        f.write(content)

async def process_batch(batch: List[Dict], cache: LLMCache, model_name: str, deck_path: str, dry_run: bool, deleted_cards: Set[str], processed_count: List[int], pairs_processed: List[int], total_pairs: int):
    """
    Process a single batch of pairs.
    """
    # Filter batch for liveness before processing
    valid_batch = []
    
    # Lazy Load Content Here
    for p in batch:
        if p['card_1'] in deleted_cards or p['card_2'] in deleted_cards:
            continue
        
        # Read content if not already present
        if 'c1_content' not in p:
            c1 = read_card_content(deck_path, p['card_1'])
            c2 = read_card_content(deck_path, p['card_2'])
            if c1 and c2:
                p['c1_content'] = c1
                p['c2_content'] = c2
                valid_batch.append(p)
        else:
            valid_batch.append(p)
    
    # Update processed pairs count (we count the whole batch as processed even if skipped/filtered)
    pairs_processed[0] += len(batch)
    progress_pct = (pairs_processed[0] / total_pairs) * 100
    logger.info(f"Progress: {pairs_processed[0]}/{total_pairs} pairs ({progress_pct:.1f}%)")
    
    if not valid_batch:
        return

    logger.info(f"Judging batch of {len(valid_batch)} pairs...")
    results = await call_llm_judge_batch(valid_batch, cache, model_name)
    
    rewrite_tasks = []
    rewrite_pairs_info = []

    for res in results:
        # Find original pair info
        p = next((x for x in valid_batch if f"{x['card_1']}|{x['card_2']}" == res.pair_id), None)
        if not p:
            continue
            
        c1_name = p['card_1']
        c2_name = p['card_2']
        
        # Strict liveness check before action
        if c1_name in deleted_cards or c2_name in deleted_cards:
            continue
            
        if res.is_same_question:
            best_idx = res.best_card_index
            if best_idx == 2:
                to_delete = c1_name
                kept = c2_name
            else:
                to_delete = c2_name
                kept = c1_name
            
            deleted_cards.add(to_delete)
            processed_count[0] += 1
            
            if dry_run:
                logger.info(f"[Dry Run] Would delete {to_delete} (LLM Judged Same: {res.reason})")
            else:
                file_path = os.path.join(deck_path, to_delete)
                try:
                    if os.path.exists(file_path):
                        os.remove(file_path)
                        logger.info(f"Deleted {to_delete} (LLM Judged Same: {res.reason})")
                except Exception as e:
                    logger.error(f"Could not delete {to_delete}: {e}")
        else:
            # Queue for Rewrite
            rewrite_tasks.append(call_rewrite_routine(p['c1_content'], p['c2_content'], cache, model_name))
            rewrite_pairs_info.append((c1_name, c2_name))

    # Execute all rewrites in parallel
    if rewrite_tasks:
        logger.info(f"Executing {len(rewrite_tasks)} rewrites in parallel...")
        rewrite_results = await asyncio.gather(*rewrite_tasks)
        
        for (c1_name, c2_name), rewrite_result in zip(rewrite_pairs_info, rewrite_results):
            if dry_run:
                logger.info(f"[Dry Run] Would rewrite {c1_name} and {c2_name}")
                logger.info(f"  Reason: {rewrite_result.reason}")
            else:
                try:
                    c1_new = rewrite_result.card_1_new_content
                    c2_new = rewrite_result.card_2_new_content
                    
                    if isinstance(c1_new, dict): c1_new = json.dumps(c1_new)
                    if isinstance(c2_new, dict): c2_new = json.dumps(c2_new)

                    write_card_content(deck_path, c1_name, c1_new)
                    write_card_content(deck_path, c2_name, c2_new)
                    logger.info(f"Rewrote {c1_name} and {c2_name}")
                except Exception as e:
                    logger.error(f"Could not rewrite files: {e}")

def read_card_metadata(deck_path, filename):
    path = os.path.join(deck_path, filename)
    if not os.path.exists(path): return None
    try:
        with open(path, 'r') as f:
            content = f.read()
        match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        if match:
            return yaml.safe_load(match.group(1))
    except Exception as e:
        logger.warning(f"Failed to read metadata for {filename}: {e}")
    return {}

async def balance_deck(deck_dir: str, similarity_file: str, dry_run: bool):
    logger.info("Starting Deck Balancing...")
    
    # Load all cards
    cards = {} # filename -> metadata
    if not os.path.exists(deck_dir):
        logger.error(f"Deck directory not found: {deck_dir}")
        return

    for f in os.listdir(deck_dir):
        if f.endswith(".md"):
            meta = read_card_metadata(deck_dir, f)
            if meta:
                cards[f] = meta
    
    logger.info(f"Loaded metadata for {len(cards)} cards.")
    
    # Group by Principle
    by_principle = {}
    for fname, meta in cards.items():
        p_ref = meta.get('principle_ref')
        if p_ref:
            if p_ref not in by_principle: by_principle[p_ref] = []
            by_principle[p_ref].append((fname, meta))
            
    # Load similarity scores for tie-breaking
    similarity_map = {} # (c1, c2) -> score
    if os.path.exists(similarity_file):
        with open(similarity_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                k = tuple(sorted((row['card_1'], row['card_2'])))
                similarity_map[k] = float(row['similarity_score'])
                
    # Process each principle
    deleted_count = 0
    for p_ref, group in by_principle.items():
        # factuals = [x for x in group if x[1].get('card_type') == 'Factual']
        scenarios = [x for x in group if x[1].get('card_type') == 'Scenario']
        
        # Target: 1 Factual, 2 Scenarios
        # We only prune Scenarios for now as per plan
        if len(scenarios) > 2:
            to_prune_count = len(scenarios) - 2
            logger.info(f"Principle '{p_ref[:50]}...': Found {len(scenarios)} scenarios, need to prune {to_prune_count}.")
            
            # Find most similar pair within scenarios
            candidates = [x[0] for x in scenarios]
            
            while to_prune_count > 0 and len(candidates) > 2:
                best_pair = None
                best_score = -1.0
                
                # Check all pairs in candidates
                import itertools
                for c1, c2 in itertools.combinations(candidates, 2):
                    k = tuple(sorted((c1, c2)))
                    score = similarity_map.get(k, 0.0)
                    if score > best_score:
                        best_score = score
                        best_pair = (c1, c2)
                
                if best_pair and best_score > 0.5: # Only prune if somewhat similar
                    # Prune one of them (the one with less other connections? or just random?)
                    # For now, prune c2
                    to_delete = best_pair[1]
                    
                    if dry_run:
                        logger.info(f"[Dry Run] Would prune {to_delete} (Scenario excess, similarity {best_score:.2f} with {best_pair[0]})")
                    else:
                        file_path = os.path.join(deck_dir, to_delete)
                        try:
                            os.remove(file_path)
                            logger.info(f"Pruned {to_delete} (Scenario excess, similarity {best_score:.2f})")
                        except Exception as e:
                            logger.error(f"Failed to delete {to_delete}: {e}")
                            
                    candidates.remove(to_delete)
                    to_prune_count -= 1
                    deleted_count += 1
                else:
                    logger.info(f"  No similar pairs found (max score {best_score:.2f}), keeping remaining {len(candidates)} scenarios.")
                    break
                    
    logger.info(f"Balancing complete. Pruned {deleted_count} cards.")

async def auto_prune_async(similarity_file, deck_dir, dry_run, model_name, concurrency):
    # Determine paths
    base_dir = os.getcwd()
    if os.path.basename(base_dir) == "scripts":
        base_dir = os.path.dirname(base_dir)
    
    similarity_path = os.path.join(base_dir, similarity_file)
    deck_path = os.path.join(base_dir, deck_dir)
    cache_path = os.path.join(base_dir, CACHE_FILE)
    
    if not os.path.exists(similarity_path):
        logger.error(f"Similarity file not found: {similarity_path}")
        return

    logger.info("Starting Auto Prune (Async)")
    logger.info(f"Similarity File: {similarity_path}")
    logger.info(f"Deck Directory: {deck_path}")
    logger.info(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}")
    logger.info(f"Model: {model_name}")
    logger.info(f"Concurrency: {concurrency}")
    
    cache = LLMCache(cache_path)
    
    pairs = []
    with open(similarity_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            pairs.append({
                "card_1": row['card_1'],
                "card_2": row['card_2'],
                "score": float(row['similarity_score'])
            })
    
    # Sort by score descending
    pairs.sort(key=lambda x: x['score'], reverse=True)
    
    deleted_cards = set()
    # Use a list for mutable int reference
    processed_count = [0]
    
    # Separate pairs into High, Mid, Low
    high_sim_pairs = []
    mid_sim_pairs = []
    
    for p in pairs:
        if p['score'] >= 0.90:
            high_sim_pairs.append(p)
        elif p['score'] >= 0.60:
            mid_sim_pairs.append(p)
            
    logger.info(f"Found {len(high_sim_pairs)} high similarity pairs (>= 0.90)")
    logger.info(f"Found {len(mid_sim_pairs)} mid similarity pairs (0.60 <= score < 0.90)")
    
    # Process High Similarity (Sequential is fine/fast)
    logger.info("Processing High Similarity Pairs...")
    for p in high_sim_pairs:
        c1_name = p['card_1']
        c2_name = p['card_2']
        
        if c1_name in deleted_cards or c2_name in deleted_cards:
            continue
            
        to_delete = c2_name
        deleted_cards.add(to_delete)
        processed_count[0] += 1
        
        if dry_run:
            logger.info(f"[Dry Run] Would delete {to_delete} (Score: {p['score']:.4f} >= 0.90)")
        else:
            file_path = os.path.join(deck_path, to_delete)
            try:
                if os.path.exists(file_path):
                    os.remove(file_path)
                    logger.info(f"Deleted {to_delete} (Score: {p['score']:.4f} >= 0.90)")
            except Exception as e:
                logger.error(f"Could not delete {to_delete}: {e}")

    # Process Mid Similarity (Async Batch)
    logger.info("Processing Mid Similarity Pairs...")
    
    # Prepare all batches
    batches = []
    current_batch = []
    
    for p in mid_sim_pairs:
        if p['card_1'] in deleted_cards or p['card_2'] in deleted_cards:
            continue
        
        # Optimization: Don't read content here. Just pass metadata.
        # Content will be read inside process_batch
        current_batch.append(p)
            
        if len(current_batch) >= BATCH_SIZE:
            batches.append(current_batch)
            current_batch = []
    
    if current_batch:
        batches.append(current_batch)
        
    logger.info(f"Created {len(batches)} batches for processing.")
    
    total_mid_sim_pairs = sum(len(b) for b in batches)
    pairs_processed = [0]

    # Semaphore for concurrency
    sem = asyncio.Semaphore(concurrency)
    
    async def run_batch(batch):
        async with sem:
            await process_batch(batch, cache, model_name, deck_path, dry_run, deleted_cards, processed_count, pairs_processed, total_mid_sim_pairs)

    try:
        tasks = [run_batch(b) for b in batches]
        await asyncio.gather(*tasks)
    finally:
        logger.info("Flushing cache to disk...")
        cache.flush()

    logger.info("-" * 40)
    logger.info(f"Total actions processed: {processed_count[0]}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Auto-prune flashcards based on similarity score.")
    parser.add_argument("--apply", action="store_true", dest="no_dry_run", help="Execute actual deletions/rewrites. Default is dry-run.")
    parser.add_argument("--balance", action="store_true", help="Run in Balance mode (prune excess scenarios based on principles).")
    parser.add_argument("--similarity-file", default=DEFAULT_SIMILARITY_FILE, help="Path to similarity scores CSV.")
    parser.add_argument("--deck-dir", default=DEFAULT_DECK_DIR, help="Directory containing flashcards.")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Gemini model to use. Default: {DEFAULT_MODEL}")
    parser.add_argument("--concurrency", type=int, default=DEFAULT_CONCURRENCY, help=f"Number of concurrent batches. Default: {DEFAULT_CONCURRENCY}")
    
    args = parser.parse_args()
    
    is_dry_run = not args.no_dry_run
    
    if args.balance:
        asyncio.run(balance_deck(
            deck_dir=args.deck_dir,
            similarity_file=args.similarity_file,
            dry_run=is_dry_run
        ))
    else:
        asyncio.run(auto_prune_async(
            similarity_file=args.similarity_file, 
            deck_dir=args.deck_dir, 
            dry_run=is_dry_run,
            model_name=args.model,
            concurrency=args.concurrency
        ))
