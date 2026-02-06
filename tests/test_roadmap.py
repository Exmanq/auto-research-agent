from auto_research_agent.pipeline import generate_roadmap


def test_generate_roadmap_length():
    roadmap = generate_roadmap("topic")
    assert len(roadmap) >= 4
