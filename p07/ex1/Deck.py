from typing import Dict, List, Optional
import random
from ex0.Card import Card


class Deck:
    """Deck management system for DataDeck."""

    def __init__(self) -> None:
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        """Add a card to the deck."""
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Remove a card by name. Returns True if found and removed."""
        for i, card in enumerate(self.cards):
            if card.name == card_name:
                self.cards.pop(i)
                return True
        return False

    def shuffle(self) -> None:
        """Shuffle the deck randomly."""
        random.shuffle(self.cards)

    def draw_card(self) -> Optional[Card]:
        """Draw a card from the top of the deck."""
        if self.cards:
            return self.cards.pop(0)
        return None

    def get_deck_stats(self) -> Dict:
        """Return deck statistics."""
        creatures = sum(1 for c in self.cards
                        if c.__class__.__name__ == "CreatureCard")
        spells = sum(1 for c in self.cards
                     if c.__class__.__name__ == "SpellCard")
        artifacts = sum(1 for c in self.cards
                        if c.__class__.__name__ == "ArtifactCard")
        total = len(self.cards)
        avg_cost = sum(c.cost for c in self.cards) / total if total > 0 else 0

        return {
            "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": round(avg_cost, 1)
        }
