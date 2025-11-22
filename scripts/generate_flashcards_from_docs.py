#!/usr/bin/env python3
# /// script
# dependencies = [
#   "pyyaml>=6.0.1",
#   "google-genai>=0.1.0",
#   "pydantic>=2.7.0",
#   "tiktoken>=0.5.0",
#   "python-dotenv>=1.0.0",
# ]
# ///
"""
Generate flashcards from dbt documentation for Analytics Engineering Certification exam.

Processes markdown documentation files to extract key principles using LLM,
then generates 2 flashcards per principle for certification study.
"""

import argparse
import asyncio
import json
import sys
import time
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

try:
    from .doc_principle_extractor import extract_principles
    from .flashcard_generator import (
        generate_flashcards_from_principles,
        write_flashcard_to_deck,
    )
except ImportError:
    from doc_principle_extractor import extract_principles
    from flashcard_generator import (
        generate_flashcards_from_principles,
        write_flashcard_to_deck,
    )


class StateManager:
    """Manage processing state for resumable execution."""
    
    def __init__(self, state_file: Path):
        self.state_file = state_file
        self.state = self._load_state()
    
    def _load_state(self) -> dict[str, Any]:
        """Load state from JSON file."""
        if self.state_file.exists():
            try:
                with open(self.state_file) as f:
                    return json.load(f)
            except Exception as e:
                print(f"[warn] Failed to load state file: {e}", file=sys.stderr)
        
        return {
            'processed_files': [],
            'failed_files': {},
            'stats': {
                'total_documents': 0,
                'total_principles': 0,
                'total_flashcards': 0,
                'uuid_collisions': 0,
            }
        }
    
    def save_state(self):
        """Save state to JSON file."""
        try:
            with open(self.state_file, 'w') as f:
                json.dump(self.state, f, indent=2)
        except Exception as e:
            print(f"[error] Failed to save state file: {e}", file=sys.stderr)
    
    def is_processed(self, file_path: str) -> bool:
        """Check if file has been processed."""
        return file_path in self.state['processed_files']
    
    def mark_processed(self, file_path: str):
        """Mark file as successfully processed."""
        if file_path not in self.state['processed_files']:
            self.state['processed_files'].append(file_path)
    
    def mark_failed(self, file_path: str, error_msg: str):
        """Mark file as failed with error message."""
        self.state['failed_files'][file_path] = error_msg
    
    def update_stats(self, **kwargs):
        """Update statistics."""
        for key, value in kwargs.items():
            if key in self.state['stats']:
                self.state['stats'][key] += value


async def process_document_with_retry(
    doc_path: Path,
    relative_path: str,
    output_dir: Path,
    existing_uuids: set[str],
    model_name: str,
    max_retries: int = 3,
) -> dict[str, Any]:
    """
    Process a single document with retry logic.
    
    Returns dict with:
        - success: bool
        - principles_count: int
        - flashcards_count: int
        - collisions: int
        - error: str (if failed)
    """
    for attempt in range(max_retries):
        try:
            # Read document
            content = doc_path.read_text()
            
            # Extract principles
            principle_extraction = await extract_principles(
                document_content=content,
                document_path=relative_path,
                model_name=model_name,
            )
            
            principles = principle_extraction.principles
            
            if not principles:
                return {
                    'success': True,
                    'principles_count': 0,
                    'flashcards_count': 0,
                    'collisions': 0,
                    'skipped': True,
                }
            
            # Generate flashcards in batches (3-5 principles per batch)
            batch_size = 5
            total_flashcards = 0
            total_collisions = 0
            
            for i in range(0, len(principles), batch_size):
                batch = principles[i:i+batch_size]
                
                # Convert to dict format for flashcard generation
                batch_dicts = [
                    {
                        'principle': p.principle,
                        'explanation': p.explanation,
                        'certification_relevance': p.certification_relevance,
                        'example': p.example,
                    }
                    for p in batch
                ]
                
                # Generate flashcards for batch
                flashcard_batch = await generate_flashcards_from_principles(
                    principles=batch_dicts,
                    model_name=model_name,
                )
                
                # Debug: Check flashcard generation result
                if not flashcard_batch.flashcards:
                    print(f"  [warn] No flashcards generated for batch of {len(batch)} principles", file=sys.stderr)
                
                # Write flashcards to deck
                for idx, flashcard in enumerate(flashcard_batch.flashcards):
                    # Determine which principle this flashcard belongs to
                    principle_idx = idx // 2  # 2 flashcards per principle
                    if principle_idx < len(batch):
                        principle = batch[principle_idx]
                        
                        _, collisions = write_flashcard_to_deck(
                            flashcard=flashcard,
                            source_file=relative_path,
                            output_dir=output_dir,
                            existing_uuids=existing_uuids,
                            principle_text=principle.principle,
                        )
                        
                        total_flashcards += 1
                        total_collisions += collisions
            
            return {
                'success': True,
                'principles_count': len(principles),
                'flashcards_count': total_flashcards,
                'collisions': total_collisions,
            }
        
        except Exception as e:
            if attempt < max_retries - 1:
                backoff = 2 ** attempt
                print(f"  [retry {attempt+1}/{max_retries}] Error: {e}. Retrying in {backoff}s...", file=sys.stderr)
                await asyncio.sleep(backoff)
            else:
                return {
                    'success': False,
                    'error': str(e),
                }
    
    return {
        'success': False,
        'error': 'Max retries exceeded',
    }


async def process_all_documents(
    input_dir: Path,
    output_dir: Path,
    state_manager: StateManager,
    model_name: str,
    rate_limit: float,
    limit: int | None = None,
    resume: bool = False,
    dry_run: bool = False,
):
    """Process all documentation files."""
    # Find all markdown files
    doc_files = sorted(input_dir.rglob('*.md'))
    
    if limit:
        doc_files = doc_files[:limit]
    
    print(f"Found {len(doc_files)} documentation files to process")
    
    if resume:
        already_processed = sum(1 for f in doc_files if state_manager.is_processed(str(f.relative_to(input_dir))))
        print(f"Resuming: {already_processed} files already processed, {len(doc_files) - already_processed} remaining")
    
    # Load existing UUIDs from deck
    existing_uuids = set()
    if output_dir.exists():
        for card_file in output_dir.glob('*.md'):
            # UUID is the filename without extension
            existing_uuids.add(card_file.stem)
    
    print(f"Loaded {len(existing_uuids)} existing UUIDs from deck")
    print()
    
    # Process each document
    for idx, doc_path in enumerate(doc_files, 1):
        relative_path = str(doc_path.relative_to(input_dir.parent))
        
        # Skip if already processed in resume mode
        if resume and state_manager.is_processed(relative_path):
            continue
        
        print(f"[{idx}/{len(doc_files)}] Processing {relative_path}...")
        
        if dry_run:
            print(f"  [DRY RUN] Would process this file")
            continue
        
        # Process document with retry
        result = await process_document_with_retry(
            doc_path=doc_path,
            relative_path=relative_path,
            output_dir=output_dir,
            existing_uuids=existing_uuids,
            model_name=model_name,
        )
        
        if result['success']:
            if result.get('skipped'):
                print(f"  No principles extracted (document may not be exam-relevant)")
            else:
                print(f"  Extracted {result['principles_count']} principles")
                print(f"  Generated {result['flashcards_count']} flashcards", end='')
                if result['collisions'] > 0:
                    print(f" ({result['collisions']} UUID collisions resolved)")
                else:
                    print()
                
                # Update stats
                state_manager.update_stats(
                    total_documents=1,
                    total_principles=result['principles_count'],
                    total_flashcards=result['flashcards_count'],
                    uuid_collisions=result['collisions'],
                )
            
            state_manager.mark_processed(relative_path)
        else:
            error_msg = result.get('error', 'Unknown error')
            print(f"  [FAILED] {error_msg}")
            state_manager.mark_failed(relative_path, error_msg)
        
        # Save state after each document
        state_manager.save_state()
        
        # Rate limiting
        if idx < len(doc_files):
            await asyncio.sleep(rate_limit)
    
    print()


def print_summary(state_manager: StateManager):
    """Print final summary statistics."""
    stats = state_manager.state['stats']
    failed_count = len(state_manager.state['failed_files'])
    processed_count = len(state_manager.state['processed_files'])
    
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Documents processed: {processed_count}")
    print(f"Documents failed: {failed_count}")
    print(f"Total principles extracted: {stats['total_principles']}")
    print(f"Total flashcards generated: {stats['total_flashcards']}")
    print(f"UUID collisions resolved: {stats['uuid_collisions']}")
    
    if failed_count > 0:
        print(f"\nFailed files:")
        for file_path, error in state_manager.state['failed_files'].items():
            print(f"  - {file_path}: {error}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate flashcards from dbt documentation for certification exam"
    )
    parser.add_argument(
        '--input-dir',
        type=Path,
        default=Path('docs/cleaned_docs'),
        help='Input directory containing documentation (default: docs/cleaned_docs/)'
    )
    parser.add_argument(
        '--output-dir',
        type=Path,
        default=Path('deck'),
        help='Output directory for flashcards (default: deck/)'
    )
    parser.add_argument(
        '--model',
        type=str,
        default='gemini-flash-latest',
        help='Gemini model name (default: gemini-flash-latest)'
    )
    parser.add_argument(
        '--rate-limit',
        type=float,
        default=1.5,
        help='Seconds to wait between document processing (default: 1.5)'
    )
    parser.add_argument(
        '--state-file',
        type=Path,
        default=Path('.flashcard_generation_state.json'),
        help='State file for resumable execution (default: .flashcard_generation_state.json)'
    )
    parser.add_argument(
        '--limit',
        type=int,
        help='Process only first N files (for testing)'
    )
    parser.add_argument(
        '--resume',
        action='store_true',
        help='Skip already processed files'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview processing without generating flashcards'
    )
    
    args = parser.parse_args()
    
    # Validate directories
    if not args.input_dir.exists():
        print(f"Error: Input directory not found: {args.input_dir}", file=sys.stderr)
        return 1
    
    if not args.output_dir.exists():
        print(f"Error: Output directory not found: {args.output_dir}", file=sys.stderr)
        return 1
    
    # Initialize state manager
    state_manager = StateManager(args.state_file)
    
    print("=" * 60)
    print("DBT FLASHCARD GENERATOR")
    print("=" * 60)
    print(f"Input directory: {args.input_dir}")
    print(f"Output directory: {args.output_dir}")
    print(f"Gemini model: {args.model}")
    print(f"Rate limit: {args.rate_limit}s between documents")
    print(f"State file: {args.state_file}")
    if args.limit:
        print(f"Limit: Processing first {args.limit} files")
    if args.resume:
        print(f"Resume mode: Skipping already processed files")
    if args.dry_run:
        print(f"DRY RUN: No flashcards will be generated")
    print()
    
    # Process documents
    start_time = time.time()
    
    try:
        asyncio.run(process_all_documents(
            input_dir=args.input_dir,
            output_dir=args.output_dir,
            state_manager=state_manager,
            model_name=args.model,
            rate_limit=args.rate_limit,
            limit=args.limit,
            resume=args.resume,
            dry_run=args.dry_run,
        ))
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Progress has been saved.")
        state_manager.save_state()
        return 130
    
    elapsed = time.time() - start_time
    
    # Print summary
    print_summary(state_manager)
    print(f"\nTotal time: {elapsed:.1f}s")
    
    if args.dry_run:
        print("\n[DRY RUN] No files were modified. Run without --dry-run to generate flashcards.")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
