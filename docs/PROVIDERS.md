# Providers

## Base
- Interface: `BaseProvider.fetch(topic: str, limit: int = 50) -> list[tuple[str, str]]`
- Returns list of `(url, title/annotation)`.

## SeedProvider (default)
- Loads packaged `auto_research_agent.data/seed_sources.json` (50 high-signal links: arXiv, blogs, docs, repos).
- Offline-only, no API keys required.

## SerperProvider (optional online)
- Uses Serper.dev Google-like search.
- Env: `SERPER_API_KEY` (or pass to constructor).
- Endpoint: `https://google.serper.dev/search`, POST `{ q, num }`.
- Gracefully falls back to empty list if no key or network failure.

## Adding other providers
1. Create `providers/<name>.py`, subclass `BaseProvider`, implement `fetch` calling your API (Tavily, Bing, GitHub, arXiv, etc.).
2. Read keys from env, handle missing keys gracefully (return []).
3. Register provider in `pipeline.gather_sources`.
4. Keep return shape `(url, title)`; include annotations in `title` for better ranking.

## Notes
- Deduping/reranking happens downstream; keep provider fetch simple.
- Respect API rate limits; consider caching if you extend.
