from __future__ import annotations

import os
from typing import Any

import requests

from .base import BaseProvider

SERPER_ENDPOINT = "https://google.serper.dev/search"


class SerperProvider(BaseProvider):
    """Google-like search via Serper.dev."""

    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or os.getenv("SERPER_API_KEY")

    def fetch(self, topic: str, limit: int = 20) -> list[tuple[str, str]]:
        if not self.api_key:
            return []
        headers = {"X-API-KEY": self.api_key, "Content-Type": "application/json"}
        payload: dict[str, Any] = {"q": topic, "num": min(limit, 20)}
        try:
            resp = requests.post(SERPER_ENDPOINT, headers=headers, json=payload, timeout=15)
            resp.raise_for_status()
            data = resp.json()
        except Exception:
            return []
        results: list[tuple[str, str]] = []
        for item in data.get("organic", [])[:limit]:
            url = item.get("link")
            title = item.get("title") or item.get("snippet") or ""
            if url:
                results.append((url, title))
        return results
