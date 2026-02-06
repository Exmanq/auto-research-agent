import json
from importlib import resources

from .base import BaseProvider


class SeedProvider(BaseProvider):
    def __init__(self, seed_file: str | None = None):
        if seed_file is None:
            seed_file = resources.files("auto_research_agent.data").joinpath("seed_sources.json")
        self.seed_file = str(seed_file)
        self._cache = None

    def _load(self):
        if self._cache is None:
            with open(self.seed_file, encoding="utf-8") as f:
                self._cache = json.load(f)
        return self._cache

    def fetch(self, topic: str, limit: int = 50) -> list[tuple[str, str]]:
        seeds = self._load()
        return [(item["url"], item.get("title", "")) for item in seeds[:limit]]
