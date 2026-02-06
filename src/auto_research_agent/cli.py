from pathlib import Path

import typer
from rich.console import Console

from .pipeline import DEFAULT_TOPIC, run_pipeline

app = typer.Typer(help="Auto research agent CLI")
console = Console()


@app.command()
def main(
    topic: str = typer.Argument(DEFAULT_TOPIC, help="Research topic"),
    out: str = typer.Option("out", help="Output directory"),
):
    out_dir = Path(out)
    console.print(f"[bold]Running auto-research on:[/bold] {topic}")
    result = run_pipeline(topic, str(out_dir))
    console.print(f"Done. Files written to {out_dir.resolve()}")
    console.print(f"Sources: {len(result['sources'])}")


if __name__ == "__main__":
    app()
