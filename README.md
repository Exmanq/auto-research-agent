# auto-research-agent

> Automated research CLI: collect sources, summarize, find trends/controversies, and propose project ideas in minutes.

![CI](https://github.com/Exmanq/auto-research-agent/actions/workflows/ci.yml/badge.svg) ![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg) ![Python](https://img.shields.io/badge/Python-3.11+-blue)

## Why
- Быстро получить ориентир по теме без ручного сбора ссылок.
- Работает офлайн из коробки на seed-датасете (50 источников).
- Подключаемые провайдеры для реального поиска, если нужны API ключи.

## Features
- `auto-research "TOPIC" --out out/` генерирует:
  - sources.md, tldr.md, deep_summary.md, trends.md, controversies.md, ideas.md, roadmap.md
- Сид-источники высокого качества (arXiv, блоги, репозитории, документация)
- Простое TF-IDF ранжирование и экстрактивное суммирование
- Лёгкое расширение провайдерами поиска и шаблонами Markdown

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
auto-research "LLM Agents: tool use, memory, planning, evals (2024-2026)" --out out/
```

## Example Output
TL;DR (фрагмент из `examples/out/tldr.md`):
- [Evals for Tool Agents](https://arxiv.org/abs/2312.XXXX) — relevance 0.31
- [Memory for AI Agents](https://lilianweng.github.io/posts/2024-01-12-memory/) — relevance 0.26
- [Evals for Tool-Using Agents](https://arxiv.org/abs/2403.05432) — relevance 0.25

Идея (из `examples/out/ideas.md`):
- **Agents Lab #1** — Проблема: Hard to benchmark agents systems consistently. Решение: Auto pipeline to gather data, run evals, and report agents metrics. MVP: CLI + seed datasets + simple scoring. Риски: Data quality, noisy signals, drift.

Больше примеров в `examples/out/`.

## How it works
- Провайдеры собирают ссылки (по умолчанию SeedProvider из `data/seed_sources.json`).
- `rank_sources`: TF-IDF + косинус по topic vs (title+url).
- `summarize_sources`: экстрактивные предложения + ключевые слова => тренды/споры.
- `generate_ideas` и `generate_roadmap`: синтетика на основе keywords.
- Рендеринг через Jinja-шаблоны в Markdown.

## Configuration
- Без ключей: используется seed-датасет (50 ссылок).
- С ключами: добавьте провайдер в `providers/`, читайте ключи из env (`SERPER_API_KEY`, `TAVILY_API_KEY`, `BING_API_KEY`, `GITHUB_TOKEN`, др.), зарегистрируйте в `pipeline.gather_sources`.
- Параметры: `--out` для директории вывода; топик — аргумент CLI.

## FAQ
**Нужен ли интернет?** Нет, сид-режим работает офлайн. Подключаемые провайдеры потребуют сеть и ключи.

**Можно ли поменять формат отчётов?** Да, правьте шаблоны в `src/auto_research_agent/templates/`.

**Где добавить новый провайдер?** Создайте в `providers/` класс от `BaseProvider` и подключите в `pipeline.gather_sources`.

**Что с зависимостями?** Python 3.11+, `pip install -e .` ставит всё необходимое.

## Contributing
- `make format` → ruff --fix + black
- `make lint` → ruff
- `make test` → pytest
- `make run` → пример запуска на дефолтной теме

PR: следуйте шаблону, добавляйте тесты и обновляйте docs/ при изменениях логики.
