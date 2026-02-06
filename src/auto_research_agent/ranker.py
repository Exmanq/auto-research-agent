from __future__ import annotations

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def rank_sources(
    topic: str, sources: list[tuple[str, str]], top_k: int = 50
) -> list[tuple[str, str, float]]:
    """Rank sources by TF-IDF similarity between topic and title/URL."""
    if not sources:
        return []
    texts = [f"{title} {url}" for url, title in sources]
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf = vectorizer.fit_transform([topic] + texts)
    topic_vec = tfidf[0]
    doc_vecs = tfidf[1:]
    sims = cosine_similarity(topic_vec, doc_vecs).flatten()
    ranked = sorted(zip(sources, sims, strict=False), key=lambda x: x[1], reverse=True)
    return [(url, title, float(score)) for (url, title), score in ranked[:top_k]]
