import os

from auto_research_agent.pipeline import load_template


def test_load_template():
    path = os.path.join(os.path.dirname(__file__), "../src/auto_research_agent/templates/base.md")
    tmpl = load_template(os.path.abspath(path))
    rendered = tmpl.render(title="Test", body=["one", "two"])
    assert "one" in rendered and "two" in rendered
