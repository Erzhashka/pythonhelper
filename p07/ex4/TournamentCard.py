from typing import Any, Dict
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """Tournament-legal card with combat and ranking abilities."""

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, defense: int, wins: int = 0) -> None:
        super().__init__(name, cost, rarity)
        self._attack = attack
        self._defense = defense
        self._wins = wins
        self._losses = 0

    # Card abstract method
    def play(self) -> Dict:
        """Play this tournament card."""
        return {
            "action": "play",
            "card": self.name,
            "tournament_legal": True,
            "stats": self.get_combat_stats()
        }

    # Combatable interface
    def attack(self, target: Any) -> Dict:
        """Attack a target."""
        damage = self._attack
        target_name = target.name if hasattr(target, 'name') else str(target)
        return {
            "attacker": self.name,
            "target": target_name,
            "damage_dealt": damage
        }

    def defend(self, damage: int) -> Dict:
        """Defend against incoming damage."""
        mitigated = min(damage, self._defense)
        damage_taken = damage - mitigated
        return {
            "defender": self.name,
            "damage_mitigated": mitigated,
            "damage_taken": damage_taken
        }

    def get_combat_stats(self) -> Dict:
        """Return combat statistics."""
        return {
            "attack": self._attack,
            "defense": self._defense,
            "power_level": self._attack + self._defense
        }

    # Rankable interface
    def get_rank_score(self) -> int:
        """Calculate rank score based on stats and wins."""
        base_score = self._attack + self._defense
        rarity_bonus = {"Common": 0, "Uncommon": 5, "Rare": 10, "Legendary": 20}
        return base_score + rarity_bonus.get(self.rarity, 0) + (self._wins * 3)

    def compare_rank(self, other: "Rankable") -> int:
        """Compare rank with another card."""
        my_score = self.get_rank_score()
        other_score = other.get_rank_score()
        if my_score > other_score:
            return 1
        elif my_score < other_score:
            return -1
        return 0

    def get_rank_breakdown(self) -> Dict:
        """Return detailed rank breakdown."""
        base = self._attack + self._defense
        rarity_bonus = {"Common": 0, "Uncommon": 5, "Rare": 10, "Legendary": 20}
        return {
            "base_stats": base,
            "rarity_bonus": rarity_bonus.get(self.rarity, 0),
            "win_bonus": self._wins * 3,
            "total_score": self.get_rank_score()
        }

    def record_match(self, won: bool) -> None:
        """Record a match result."""
        if won:
            self._wins += 1
        else:
            self._losses += 1

    def get_record(self) -> Dict:
        """Get win/loss record."""
        return {"wins": self._wins, "losses": self._losses}
