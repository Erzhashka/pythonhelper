from typing import Dict
from ex0.Card import Card


class ArtifactCard(Card):
    """Concrete card type representing permanent artifacts."""

    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.is_active = True

    def play(self, game_state: Dict) -> Dict:
        """Place artifact on the battlefield (permanent)."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}"
        }

    def get_card_info(self) -> Dict:
        """Return artifact card information."""
        info = super().get_card_info()
        info["type"] = "Artifact"
        info["durability"] = self.durability
        info["effect"] = self.effect
        return info

    def activate_ability(self) -> Dict:
        """Activate the artifact's ongoing effect."""
        if not self.is_active:
            return {"activated": False, "reason": "Artifact destroyed"}
        self.durability -= 1
        if self.durability <= 0:
            self.is_active = False
        return {
            "artifact": self.name,
            "effect": self.effect,
            "durability_remaining": self.durability,
            "activated": True
        }
