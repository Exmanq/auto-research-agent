# Providers

## Base
- Interface: `BaseProvider.fetch(topic: str, limit: int = 50) -> list[tuple[str, str]]`
- Returns list of `(url, title/annotation)`.

## SeedProvider (default)
- Loads packaged `auto_research_agent.data/seed_sources.json` (50 high-signal links: arXiv, blogs, docs, repos).
- Offline-only, no API keys required.

## Adding real search
1. Create `providers/<name>.py`, subclass `BaseProvider`, implement `fetch` calling your API (Serper, Tavily, Bing, GitHub, arXiv, etc.).
2. Read keys from env (e.g., `SERPER_API_KEY`), handle missing keys gracefully (fallback to empty list).
3. Register provider in `pipeline.gather_sources` list.
4. Keep return shape `(url, title)`; include annotations in `title` for better ranking.

## Notes
- Deduping/reranking is handled downstream; keep provider fetch simple.
- Respect API rate limits; consider caching if you extend.
