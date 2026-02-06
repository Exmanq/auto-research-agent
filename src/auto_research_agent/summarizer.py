from __future__ import annotations

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


def extractive_summary(topic: str, texts: list[str], max_sentences: int = 8) -> list[str]:
    """Simple TF-IDF based sentence scoring."""
    if not texts:
        return []
    sentences: list[str] = []
    for text in texts:
        for sent in text.split("."):
            s = sent.strip()
            if len(s) > 20:
                sentences.append(s)
    if not sentences:
        return []
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf = vectorizer.fit_transform([topic] + sentences)
    topic_vec = tfidf[0]
    sent_vecs = tfidf[1:]
    scores = (sent_vecs @ topic_vec.T).toarray().flatten()
    ranked = [
        sent
        for _, sent in sorted(
            zip(scores, sentences, strict=False), key=lambda x: x[0], reverse=True
        )
    ]
    return ranked[:max_sentences]


def top_keywords(texts: list[str], k: int = 10) -> list[str]:
    if not texts:
        return []
    vectorizer = TfidfVectorizer(stop_words="english", max_features=1000)
    tfidf = vectorizer.fit_transform(texts)
    scores = np.asarray(tfidf.sum(axis=0)).ravel()
    terms = vectorizer.get_feature_names_out()
    ranked = sorted(zip(terms, scores, strict=False), key=lambda x: x[1], reverse=True)
    return [t for t, _ in ranked[:k]]
