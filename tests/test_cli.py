import subprocess
import sys


def test_cli_runs(tmp_path):
    out_dir = tmp_path / "o"
    cmd = [sys.executable, "-m", "auto_research_agent.cli", "test topic", "--out", str(out_dir)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    assert result.returncode == 0
    assert (out_dir / "sources.md").exists()
