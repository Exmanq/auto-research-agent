from auto_research_agent.providers.serper import SerperProvider


def test_serper_provider_no_key_returns_empty(monkeypatch):
    monkeypatch.delenv("SERPER_API_KEY", raising=False)
    p = SerperProvider(api_key=None)
    results = p.fetch("test", limit=5)
    assert results == []
