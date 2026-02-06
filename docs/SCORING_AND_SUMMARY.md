# Scoring and Summary

## Ranking
- Uses `TfidfVectorizer(stop_words="english")` over `[topic] + [title+url]`.
- Cosine similarity topic vector vs doc vectors.
- Sorted descending, top_k=50 by default.

## Summaries
- Extractive: splits titles into pseudo-sentences by period, filters len>20, scores with TF-IDF against topic.
- Keywords: TF-IDF term sums across titles; top 12 used to synthesize trends/controversies/ideas seeds.
- Trends: first 5 keywords -> "Growing focus"; declines: next keywords; controversies: debate lines.

## Ideas & Roadmap
- Ideas: 12 items, seeded by keywords (fallback to agents/tools/memory/evals/planning); fields: name, problem, solution, MVP, risks.
- Roadmap: fixed 4-week study plan; adjust in `generate_roadmap` as needed.

## Extending
- Replace `rank_sources` with BM25 + rerankers (cross-encoder) for better signal.
- Replace `extractive_summary` with LLM summarization or TextRank; keep interface.
- Enrich keywords by chunking full content when real providers supply bodies.
