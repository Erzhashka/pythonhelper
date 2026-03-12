from typing import Dict, List, Union
import random
from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):
    """Concrete factory for fantasy-themed cards."""

    def __init__(self) -> None:
        self.creature_templates = {
            "dragon": {"cost": 5, "attack": 7, "health": 5, "rarity": "Legendary"},
            "goblin": {"cost": 2, "attack": 2, "health": 2, "rarity": "Common"}
        }
        self.spell_templates = {
            "fireball": {"cost": 3, "effect": "damage", "rarity": "Common"}
        }
        self.artifact_templates = {
            "mana_ring": {"cost": 2, "durability": 5, "effect": "+1 mana", "rarity": "Rare"}
        }

    def create_creature(self, name_or_power: Union[str, int, None] = None) -> Card:
        """Create a fantasy creature."""
        if isinstance(name_or_power, str) and name_or_power.lower() in self.creature_templates:
            template = self.creature_templates[name_or_power.lower()]
            name = name_or_power.title()
        else:
            template = self.creature_templates["dragon"]
            name = "Fire Dragon"

        return CreatureCard(
            name, template["cost"], template["rarity"],
            template["attack"], template["health"]
        )

    def create_spell(self, name_or_power: Union[str, int, None] = None) -> Card:
        """Create a fantasy spell."""
        if isinstance(name_or_power, str) and name_or_power.lower() in self.spell_templates:
            template = self.spell_templates[name_or_power.lower()]
            name = name_or_power.title()
        else:
            template = self.spell_templates["fireball"]
            name = "Fireball"

        return SpellCard(name, template["cost"], template["rarity"], template["effect"])

    def create_artifact(self, name_or_power: Union[str, int, None] = None) -> Card:
        """Create a fantasy artifact."""
        if isinstance(name_or_power, str) and name_or_power.lower().replace(" ", "_") in self.artifact_templates:
            key = name_or_power.lower().replace(" ", "_")
            template = self.artifact_templates[key]
            name = name_or_power.title()
        else:
            template = self.artifact_templates["mana_ring"]
            name = "Mana Ring"

        return ArtifactCard(
            name, template["cost"], template["rarity"],
            template["durability"], template["effect"]
        )

    def create_themed_deck(self, size: int) -> Dict:
        """Create a themed deck."""
        cards: List[Card] = []
        for i in range(size):
            card_type = random.choice(["creature", "spell", "artifact"])
            if card_type == "creature":
                cards.append(self.create_creature())
            elif card_type == "spell":
                cards.append(self.create_spell())
            else:
                cards.append(self.create_artifact())

        return {
            "cards": cards,
            "size": len(cards),
            "theme": "Fantasy"
        }

    def get_supported_types(self) -> Dict:
        """Return supported card types."""
        return {
            "creatures": list(self.creature_templates.keys()),
            "spells": list(self.spell_templates.keys()),
            "artifacts": list(self.artifact_templates.keys())
        }
