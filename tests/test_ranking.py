from auto_research_agent.ranker import rank_sources


def test_rank_sources_orders_by_score():
    topic = "llm agents"
    sources = [("a", "llm agents"), ("b", "cooking"), ("c", "agents llm tools")]
    ranked = rank_sources(topic, sources, top_k=3)
    assert ranked[0][0] in {"a", "c"}
    assert len(ranked) == 3
