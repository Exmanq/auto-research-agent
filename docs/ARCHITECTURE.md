# Architecture

## Overview
- **CLI (Typer)**: entrypoint `auto-research` -> `cli.py`.
- **Pipeline**: `pipeline.run_pipeline` orchestrates providers -> ranking -> summaries -> renders templates to Markdown.
- **Providers**: pluggable source fetchers implementing `BaseProvider.fetch(topic, limit)`.
- **Ranking**: TF-IDF on topic vs (title+URL), cosine similarity.
- **Summaries**: extractive sentence scoring + keyword mining for trends/controversies, templated Markdown for outputs.
- **Templates**: Markdown Jinja templates for deep summary and ideas.
- **Data**: packaged seed dataset (`auto_research_agent.data.seed_sources.json`).

## Flow
1) CLI parses args (`topic`, `--out`).
2) Providers fetch raw (url, title) items (seed-only by default).
3) `rank_sources` scores sources by TF-IDF similarity to topic.
4) `summarize_sources` builds annotations, keywords, simple trend/controversy lists.
5) `generate_ideas` and `generate_roadmap` synthesize ideas/plan.
6) Markdown writers render to `out/` files.

## Extensibility
- Add provider: subclass `BaseProvider`, implement `fetch`, register in `pipeline.gather_sources`.
- Replace ranking: swap TF-IDF with BM25/rerankers; keep signature.
- Replace summarizer: plug LLM-based summarization; keep interface `extractive_summary` + `top_keywords`.
- Templates: edit/add under `templates/` to change output formatting.
