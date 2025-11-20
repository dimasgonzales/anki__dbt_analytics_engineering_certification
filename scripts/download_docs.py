# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "aiohttp",
#     "playwright",
#     "markdownify",
#     "python-dotenv",
# ]
# ///

import os
import json
import asyncio
import aiohttp
import sys
import subprocess
from playwright.async_api import async_playwright
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
SEARXNG_URL = "https://search.colobus-pike.ts.net/search"
PROXY_SERVER = os.getenv("PROXY_SERVER")
PROXY_USERNAME = os.getenv("PROXY_USERNAME")
PROXY_PASSWORD = os.getenv("PROXY_PASSWORD")
OUTPUT_BASE = "docs/site_docs.getdbt.com"
TAGS_FILE = "tags.json"
CONCURRENCY_LIMIT = 4

async def check_playwright():
    """Checks if Playwright browsers are installed, installs if missing."""
    print("Checking Playwright availability...")
    try:
        async with async_playwright() as p:
            await p.chromium.launch(headless=True)
            print("✅ Playwright browsers are available.")
    except Exception as e:
        print(f"⚠️ Playwright check failed: {e}")
        print("Attempting to install browsers via script environment...")
        try:
            subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"], check=True)
            print("✅ Browser installation complete.")
        except Exception as install_e:
            print(f"❌ Failed to install browsers: {install_e}")
            sys.exit(1)

async def search_searxng(session, query):
    """Searches SearXNG for the given query asynchronously."""
    params = {
        "q": query,
        "format": "json",
    }
    try:
        async with session.get(SEARXNG_URL, params=params, timeout=10) as response:
            response.raise_for_status()
            data = await response.json()
            return data.get("results", [])
    except Exception as e:
        print(f"Error searching for '{query}': {e}")
        return []

async def process_page(browser, url, output_dir, filename_base):
    """Downloads page, takes screenshot, and saves markdown."""
    page = None
    context = None
    try:
        # Configure proxy for the browser context
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            proxy={
                "server": PROXY_SERVER,
                "username": PROXY_USERNAME,
                "password": PROXY_PASSWORD
            }
        )
        page = await context.new_page()
        # print(f"Navigating to {url}...")
        
        # Go to page
        await page.goto(url, timeout=60000, wait_until="domcontentloaded")
        
        # Smart wait: wait for network to be idle, but max 5 seconds
        try:
            await page.wait_for_load_state("networkidle", timeout=5000)
        except Exception:
            pass # Proceed anyway if it doesn't settle

        # Create output directory
        os.makedirs(output_dir, exist_ok=True)

        # 1. Save Screenshot
        screenshot_path = os.path.join(output_dir, f"{filename_base}.png")
        await page.screenshot(path=screenshot_path, full_page=True)
        # print(f"Saved screenshot to {screenshot_path}")

        # 2. Save Markdown
        from markdownify import markdownify as md
        
        content = await page.content()
        # markdownify is sync, but fast enough to run here
        markdown = md(content)
        markdown_path = os.path.join(output_dir, f"{filename_base}.md")
        
        with open(markdown_path, "w", encoding="utf-8") as f:
            f.write(f"# Source: {url}\n\n")
            f.write(markdown)
        
        return True

    except Exception as e:
        print(f"Error processing {url}: {e}")
        return False
    finally:
        if page:
            await page.close()
        if context:
            await context.close()

async def process_tag(sem, session, browser, tag, index, total, seen_urls, url_index):
    async with sem:
        child_tag = tag.get("child_tag")
        keywords = tag.get("keywords", [])
        
        if not child_tag:
            return

        search_term = f"site:docs.getdbt.com {child_tag}"
        if keywords:
            search_term += f" {keywords[0]}"
        
        print(f"[{index+1}/{total}] Searching: {search_term}")
        results = await search_searxng(session, search_term)

        if not results:
            print(f"[{index+1}/{total}] ❌ No results for {child_tag}")
            return

        # Process top 10 results
        top_results = results[:10]
        print(f"[{index+1}/{total}] Found {len(top_results)} results for {child_tag}")

        for rank, result in enumerate(top_results):
            url = result.get("url")
            
            if not url:
                continue
            
            # Normalize URL to avoid duplicates with trailing slashes
            normalized_url = url.rstrip('/')
            
            # Track tags for this URL
            if normalized_url not in url_index:
                url_index[normalized_url] = []
            url_index[normalized_url].append(child_tag)

            if normalized_url in seen_urls:
                # print(f"[{index+1}/{total}] ⏭️  Skipping duplicate: {url}")
                continue
            
            # Determine output path
            output_dir = os.path.join(OUTPUT_BASE, child_tag)
            filename_base = f"rank_{rank+1}"
            local_path = os.path.join(output_dir, f"{filename_base}.md")

            # Mark as seen with local path
            seen_urls[normalized_url] = local_path
            
            success = await process_page(browser, url, output_dir, filename_base)
            if success:
                # print(f"[{index+1}/{total}] ✅ Saved {child_tag} #{rank+1}")
                pass
            else:
                print(f"[{index+1}/{total}] ❌ Failed {child_tag} #{rank+1}")
        
        print(f"[{index+1}/{total}] ✅ Completed {child_tag}")

async def main():
    await check_playwright()

    if not os.path.exists(TAGS_FILE):
        print(f"Tags file not found: {TAGS_FILE}")
        return

    with open(TAGS_FILE, "r") as f:
        tags = json.load(f)

    print(f"Loaded {len(tags)} tags. Starting async download process (Concurrency: {CONCURRENCY_LIMIT})...")

    # Shared structures
    seen_urls = {} # URL -> local_path
    url_index = {} # URL -> [tags]

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        async with aiohttp.ClientSession() as session:
            sem = asyncio.Semaphore(CONCURRENCY_LIMIT)
            tasks = []
            for i, tag in enumerate(tags):
                tasks.append(process_tag(sem, session, browser, tag, i, len(tags), seen_urls, url_index))
            
            await asyncio.gather(*tasks)
        
        await browser.close()
    
    # Save index
    print("Saving index...")
    final_index = []
    for url, tags in url_index.items():
        local_path = seen_urls.get(url)
        if local_path:
            final_index.append({
                "url": url,
                "local_path": local_path,
                "tags": list(set(tags)) # Deduplicate tags
            })
            
    index_path = os.path.join(OUTPUT_BASE, "index.json")
    with open(index_path, "w") as f:
        json.dump(final_index, f, indent=2)
    print(f"Index saved to {index_path}")

    print("\nDone!")

if __name__ == "__main__":
    asyncio.run(main())
