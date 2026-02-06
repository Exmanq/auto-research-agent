from auto_research_agent.providers.seed import SeedProvider


def test_seed_provider_loads():
    p = SeedProvider()
    results = p.fetch("test", limit=5)
    assert len(results) == 5
    assert all(len(item) == 2 for item in results)
