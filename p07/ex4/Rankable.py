from abc import ABC, abstractmethod
from typing import Dict


class Rankable(ABC):
    """Abstract interface for ranking functionality."""

    @abstractmethod
    def get_rank_score(self) -> int:
        """Calculate and return rank score."""
        pass

    @abstractmethod
    def compare_rank(self, other: "Rankable") -> int:
        """Compare rank with another rankable. Returns -1, 0, or 1."""
        pass

    @abstractmethod
    def get_rank_breakdown(self) -> Dict:
        """Return detailed breakdown of rank components."""
        pass
