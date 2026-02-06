.PHONY: format lint test run

format:
	ruff check --fix src tests
	black src tests

lint:
	ruff check src tests

test:
	pytest

run:
	python -m pip install -e .
	auto-research "LLM Agents: tool use, memory, planning, evals (2024-2026)" --out out/
