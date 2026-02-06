from __future__ import annotations

from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """Abstract provider interface."""

    @abstractmethod
    def fetch(self, topic: str, limit: int = 50) -> list[tuple[str, str]]:
        """
        Return list of (url, title/annotation) tuples.
        Should be pure (no side effects) beyond network access.
        """
        raise NotImplementedError
