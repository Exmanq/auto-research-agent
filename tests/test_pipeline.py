from auto_research_agent.pipeline import DEFAULT_TOPIC, run_pipeline


def test_run_pipeline_creates_files(tmp_path):
    out_dir = tmp_path / "out"
    run_pipeline(DEFAULT_TOPIC, str(out_dir))
    expected = [
        "sources.md",
        "tldr.md",
        "deep_summary.md",
        "trends.md",
        "controversies.md",
        "ideas.md",
        "roadmap.md",
    ]
    for fname in expected:
        assert (out_dir / fname).exists()
