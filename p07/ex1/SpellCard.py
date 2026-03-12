from typing import Dict, List
from ex0.Card import Card


class SpellCard(Card):
    """Concrete card type representing instant spells."""

    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type  # damage, heal, buff, debuff

    def play(self, game_state: Dict) -> Dict:
        """Cast the spell (one-time use)."""
        effect_messages = {
            "damage": f"Deal {self.cost} damage to target",
            "heal": f"Restore {self.cost * 2} health",
            "buff": "Increase target stats",
            "debuff": "Decrease enemy stats"
        }
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect_messages.get(self.effect_type, "Spell cast")
        }

    def get_card_info(self) -> Dict:
        """Return spell card information."""
        info = super().get_card_info()
        info["type"] = "Spell"
        info["effect_type"] = self.effect_type
        return info

    def resolve_effect(self, targets: List) -> Dict:
        """Resolve the spell effect on targets."""
        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets_affected": len(targets),
            "resolved": True
        }
