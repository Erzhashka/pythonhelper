#!/usr/bin/env python3
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===")
    print()

    # Create tournament
    platform = TournamentPlatform("Grand Championship")

    # Create tournament cards
    champion = TournamentCard("Grand Champion", 5, "Legendary", 8, 6, wins=5)
    knight = TournamentCard("Steel Knight", 3, "Rare", 5, 4, wins=2)
    scout = TournamentCard("Swift Scout", 2, "Common", 3, 2, wins=0)

    print("Registering participants...")
    print(platform.register_participant(champion))
    print(platform.register_participant(knight))
    print(platform.register_participant(scout))
    print()

    print("Rank Breakdowns:")
    for card in [champion, knight, scout]:
        print(f"{card.name}: {card.get_rank_breakdown()}")
    print()

    print("Running matches...")
    print(platform.run_match(champion, knight))
    print(platform.run_match(knight, scout))
    print(platform.run_match(champion, scout))
    print()

    print("Combat Demo:")
    attack_result = champion.attack(knight)
    print(f"Attack: {attack_result}")
    defend_result = knight.defend(8)
    print(f"Defense: {defend_result}")
    print()

    print("Final Rankings:")
    for ranking in platform.get_rankings():
        print(f"#{ranking['rank']}: {ranking['card']} (Score: {ranking['score']}, Record: {ranking['record']})")
    print()

    print("Tournament Summary:")
    print(platform.get_tournament_summary())
    print()

    print("Three-interface inheritance achieved: Card + Combatable + Rankable!")


if __name__ == "__main__":
    main()
