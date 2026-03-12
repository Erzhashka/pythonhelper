from abc import ABC, abstractmethod
from typing import Dict


class Card(ABC):
    """Abstract base class for all cards in DataDeck."""

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: Dict) -> Dict:
        """Play this card. Must be implemented by subclasses."""
        pass

    def get_card_info(self) -> Dict:
        """Return card information as dictionary."""
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.__class__.__name__.replace("Card", "")
        }

    def is_playable(self, available_mana: int) -> bool:
        """Check if card can be played with available mana."""
        return available_mana >= self.cost
