# Contributing

## How to work
- Fork and branch from `main`.
- Use conventional-ish commits (e.g., `feat: ...`, `fix: ...`, `docs: ...`).
- Keep changes small and covered by tests.

## Dev setup
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m pip install ruff pytest black isort
pre-commit install
```

## Commands
- `make format` — ruff --fix + black
- `make lint` — ruff
- `make test` — pytest
- `make run` — sample run on default topic

## Before PR
- `ruff check src tests`
- `pytest`
- `auto-research "test topic" --out out/`
- Update docs/README if UX changes

## Providers
- Subclass `BaseProvider`, implement `fetch(topic, limit)`, read API keys from env, return `(url, title)`.
- Register provider in `pipeline.gather_sources`.

## Style
- 100-char lines, typed functions, no secrets in repo, keep templates lightweight.
