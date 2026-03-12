from typing import Dict, List
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """Concrete aggressive strategy - prioritizes damage."""

    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        """Execute aggressive turn - play low-cost cards, attack face."""
        cards_played = []
        mana_used = 0
        damage_dealt = 0

        # Sort by cost to play cheap cards first
        sorted_hand = sorted(hand, key=lambda c: c.cost if hasattr(c, 'cost') else 0)

        for card in sorted_hand:
            if hasattr(card, 'cost') and card.cost <= 5:
                cards_played.append(card.name if hasattr(card, 'name') else str(card))
                mana_used += card.cost
                if hasattr(card, 'attack_power'):
                    damage_dealt += card.attack_power
                elif hasattr(card, 'attack'):
                    damage_dealt += card.attack
                elif hasattr(card, 'cost'):
                    damage_dealt += card.cost

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": damage_dealt
        }

    def get_strategy_name(self) -> str:
        """Return strategy name."""
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List) -> List:
        """Prioritize enemy player over minions."""
        # Always go face (attack player directly)
        prioritized = []
        for target in available_targets:
            if "Player" in str(target):
                prioritized.insert(0, target)
            else:
                prioritized.append(target)
        return prioritized if prioritized else available_targets
