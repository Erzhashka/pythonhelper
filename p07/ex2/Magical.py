from abc import ABC, abstractmethod
from typing import Dict, List


class Magical(ABC):
    """Abstract interface for magical capabilities."""

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        """Cast a spell on targets."""
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict:
        """Channel mana for magical abilities."""
        pass

    @abstractmethod
    def get_magic_stats(self) -> Dict:
        """Get magical statistics."""
        pass
