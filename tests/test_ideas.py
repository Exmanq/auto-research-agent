from auto_research_agent.pipeline import generate_ideas


def test_generate_ideas_count_and_fields():
    ideas = generate_ideas("topic", ["agents", "tools"], count=10)
    required = {"name", "problem", "solution", "mvp", "risks"}
    assert len(ideas) == 10
    assert all(required.issubset(idea.keys()) for idea in ideas)
