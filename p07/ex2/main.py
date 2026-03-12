#!/usr/bin/env python3
from ex2.EliteCard import EliteCard


def main() -> None:
    print("=== DataDeck Ability System ===")
    print()

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")
    print()

    warrior = EliteCard("Arcane Warrior", 6, "Legendary", 5, 8, 10)
    enemy = EliteCard("Enemy", 3, "Common", 3, 5, 5)

    print("Playing Arcane Warrior (Elite Card):")
    game_state = {"mana": 10}
    print(warrior.play(game_state))
    print()

    print("Combat phase:")
    print(f"Attack result: {warrior.attack(enemy)}")
    print(f"Defense result: {warrior.defend(5)}")
    print()

    print("Magic phase:")
    print(f"Spell cast: {warrior.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {warrior.channel_mana(3)}")
    print()

    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
