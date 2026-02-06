# auto-research-agent

CLI-инструмент, который по теме автоматически собирает источники, ранжирует, делает структурированные резюме, выделяет тренды/спорные вопросы и предлагает идеи проектов.

- Без ключей работает из коробки на сид-сборке качественных ссылок.
- Поддерживает подключаемые провайдеры поиска (см. `providers/`).
- Генерирует отчёты в Markdown.

## Установка

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

## Использование

```bash
auto-research "LLM Agents: tool use, memory, planning, evals (2024-2026)" --out out/
```

Выходные файлы (создаются в `--out`):
- `sources.md` — список ссылок + аннотации
- `tldr.md` — короткое резюме
- `deep_summary.md` — подробный обзор по секциям
- `trends.md` — тренды (растёт/падает)
- `controversies.md` — спорные вопросы
- `ideas.md` — 10–20 идей проектов с мини-ТЗ
- `roadmap.md` — план изучения на 2–4 недели

## Подключение реального поиска

По умолчанию используется сид-датасет `data/seed_sources.json` и ранжирование по ключевым словам.
Чтобы подключить реальный поиск:
- добавьте новый провайдер в `src/auto_research_agent/providers/` (наследник `BaseProvider`),
- реализуйте метод `fetch(topic, limit)` с вызовами внешних API (Serper, Tavily, Bing, GitHub, arXiv и т.п.),
- зарегистрируйте провайдер в `pipeline.py` (в списке `providers`).

Предлагаемые ключи окружения для внешних API:
- `SERPER_API_KEY`, `TAVILY_API_KEY`, `BING_API_KEY`, `GITHUB_TOKEN` — используйте то, что доступно.

Если ключей нет, код продолжает работать на seed.

## Архитектура

```
src/auto_research_agent/
  cli.py            # CLI на Typer
  pipeline.py       # оркестратор: собирает источники, ранжирует, генерит отчёты
  ranker.py         # простое TF-IDF/ключевые слова для сортировки
  summarizer.py     # extractive-суммаризация по ключевым предложениям
  providers/
    base.py         # интерфейс провайдера
    seed.py         # провайдер сид-источников
  templates/        # markdown-шаблоны
  ...
data/seed_sources.json
```

## Команды разработчика

```bash
make format     # black + ruff --fix
make lint       # ruff
make test       # pytest
make run        # пример запуска на дефолтной теме
```

## Пример запуска

```bash
make run
cat out/tldr.md
```

## Тесты

Запуск:
```bash
pytest
```

## Лицензия

MIT

## Проверка

Команды, которые должны проходить:

```bash
python -m pip install -e . --break-system-packages  # или в venv без флага
ruff check src tests
pytest
auto-research "test topic" --out out/
```
