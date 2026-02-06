# Contributing

Thanks for contributing! Quick guide:

- Fork and branch from `main`.
- Run `make format && make lint && make test` before pushing.
- Keep functions small and add tests for new logic.
- For providers: inherit from `BaseProvider`, implement `fetch(topic, limit)`.
- For templates: keep Markdown simple, no heavy formatting.
- Open a PR with a concise summary and checklist of changes.
