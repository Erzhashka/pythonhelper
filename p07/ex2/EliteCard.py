from typing import Dict, List
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """Elite card with both combat and magical abilities."""

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, mana_pool: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.health = health
        self.max_health = health
        self.mana_pool = mana_pool
        self.armor = 3

    def play(self, game_state: Dict) -> Dict:
        """Play the elite card."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite warrior summoned with combat and magic abilities"
        }

    def get_card_info(self) -> Dict:
        """Return elite card information."""
        info = super().get_card_info()
        info["type"] = "Elite"
        info["attack"] = self.attack_power
        info["health"] = self.health
        info["mana_pool"] = self.mana_pool
        return info

    # Combatable methods
    def attack(self, target) -> Dict:
        """Attack a target."""
        target_name = target.name if hasattr(target, "name") else str(target)
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_power,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> Dict:
        """Defend against incoming damage."""
        blocked = min(incoming_damage, self.armor)
        actual_damage = incoming_damage - blocked
        self.health -= actual_damage
        return {
            "defender": self.name,
            "damage_taken": actual_damage,
            "damage_blocked": blocked,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> Dict:
        """Get combat statistics."""
        return {
            "attack": self.attack_power,
            "health": self.health,
            "armor": self.armor
        }

    # Magical methods
    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        """Cast a spell on targets."""
        mana_cost = 4
        if self.mana_pool >= mana_cost:
            self.mana_pool -= mana_cost
            return {
                "caster": self.name,
                "spell": spell_name,
                "targets": targets,
                "mana_used": mana_cost
            }
        return {"error": "Insufficient mana"}

    def channel_mana(self, amount: int) -> Dict:
        """Channel additional mana."""
        self.mana_pool += amount
        return {
            "channeled": amount,
            "total_mana": self.mana_pool
        }

    def get_magic_stats(self) -> Dict:
        """Get magical statistics."""
        return {
            "mana_pool": self.mana_pool,
            "spells_available": ["Fireball", "Ice Shard", "Lightning"]
        }
