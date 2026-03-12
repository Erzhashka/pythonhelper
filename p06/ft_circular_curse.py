#!/usr/bin/env python3
from alchemy.grimoire import validate_ingredients, record_spell


def main() -> None:
    print("\n=== Circular Curse Breaking ===")
    print()

    print("Testing ingredient validation:")
    print(f'validate_ingredients("fire air"): {validate_ingredients("fire air")}')
    print(f'validate_ingredients("dragon scales"): {validate_ingredients("dragon scales")}')
    print()

    print("Testing spell recording with validation:")
    print(f'record_spell("Fireball", "fire air"): {record_spell("Fireball", "fire air")}')
    print(f'record_spell("Dark Magic", "shadow"): {record_spell("Dark Magic", "shadow")}')
    print()

    print("Testing late import technique:")
    print(f'record_spell("Lightning", "air"): {record_spell("Lightning", "air")}')
    print()

    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
