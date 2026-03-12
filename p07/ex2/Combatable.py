from abc import ABC, abstractmethod
from typing import Dict


class Combatable(ABC):
    """Abstract interface for combat capabilities."""

    @abstractmethod
    def attack(self, target) -> Dict:
        """Attack a target."""
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict:
        """Defend against incoming damage."""
        pass

    @abstractmethod
    def get_combat_stats(self) -> Dict:
        """Get combat statistics."""
        pass
