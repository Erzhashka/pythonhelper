from typing import Dict, List, Optional
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from ex0.Card import Card


class GameEngine:
    """Game orchestrator that combines factory and strategy patterns."""

    def __init__(self) -> None:
        self.factory: Optional[CardFactory] = None
        self.strategy: Optional[GameStrategy] = None
        self.hand: List[Card] = []
        self.battlefield: List[Card] = []
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        """Configure the engine with factory and strategy."""
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict:
        """Simulate a turn using configured strategy."""
        if not self.strategy or not self.factory:
            return {"error": "Engine not configured"}

        # Create some cards for the hand if empty
        if not self.hand:
            self.hand.append(self.factory.create_creature("dragon"))
            self.hand.append(self.factory.create_creature("goblin"))
            self.hand.append(self.factory.create_spell("fireball"))
            self.cards_created += 3

        # Execute turn
        result = self.strategy.execute_turn(self.hand, self.battlefield)
        self.turns_simulated += 1
        self.total_damage += result.get("damage_dealt", 0)

        return {
            "turn": self.turns_simulated,
            "strategy": self.strategy.get_strategy_name(),
            "actions": result
        }

    def get_engine_status(self) -> Dict:
        """Get current engine status."""
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name() if self.strategy else None,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
