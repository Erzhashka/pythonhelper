from abc import ABC, abstractmethod
from typing import Dict, List


class GameStrategy(ABC):
    """Abstract interface for game strategies."""

    @abstractmethod
    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        """Execute a turn based on strategy."""
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Return the strategy name."""
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: List) -> List:
        """Prioritize targets for attacks."""
        pass
