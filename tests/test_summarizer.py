from auto_research_agent.summarizer import extractive_summary, top_keywords


def test_extractive_summary_returns_sentences():
    topic = "agents"
    texts = ["Agents use tools. They plan tasks. Memory helps agents act."]
    result = extractive_summary(topic, texts, max_sentences=2)
    assert len(result) >= 1
    assert any("agents" in s.lower() for s in result)


def test_top_keywords_non_empty():
    texts = ["agents use tools and memory", "planning and evaluation for agents"]
    kws = top_keywords(texts, k=3)
    assert len(kws) == 3
