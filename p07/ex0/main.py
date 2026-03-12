#!/usr/bin/env python3
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===")
    print()

    print("Testing Abstract Base Class Design:")
    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    goblin = CreatureCard("Goblin Warrior", 2, "Common", 2, 2)

    print("CreatureCard Info:")
    print(dragon.get_card_info())
    print()

    print("Playing Fire Dragon with 6 mana available:")
    print(f"Playable: {dragon.is_playable(6)}")
    game_state = {"mana": 6, "battlefield": []}
    print(f"Play result: {dragon.play(game_state)}")
    print()

    print("Fire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {dragon.attack_target(goblin)}")
    print()

    print("Testing insufficient mana (3 available):")
    print(f"Playable: {dragon.is_playable(3)}")
    print()

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
