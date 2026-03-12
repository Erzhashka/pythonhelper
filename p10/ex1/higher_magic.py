from typing import Callable, Any, Tuple

def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:

    def combined(*args: Any, **kwargs: Any) -> Tuple[Any, Any]:
        result1 = spell1(*args, **kwargs)
        result2 = spell2(*args, **kwargs)
        return (result1, result2)
    return combined

def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:

    def amplified(*args: Any, **kwargs: Any) -> Any:
        result = base_spell(*args, **kwargs)
        return result * multiplier
    return amplified

def conditional_caster(condition: Callable, spell: Callable) -> Callable:

    def conditional(*args: Any, **kwargs: Any) -> Any:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return conditional

def spell_sequence(spells: list[Callable]) -> Callable:

    def sequence(*args: Any, **kwargs: Any) -> list[Any]:
        return [spell(*args, **kwargs) for spell in spells]
    return sequence

def main() -> None:

    print("=== Higher Realm ===")
    print()

    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    def damage_spell(power: int) -> int:
        return power

    def is_powerful(power: int) -> bool:
        return power >= 50

    def lightning(target: str) -> str:
        return f"Lightning strikes {target}"

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon")
    print(f"Combined spell result: {result[0]}, {result[1]}")
    print()

    print("Testing power amplifier...")
    mega_damage = power_amplifier(damage_spell, 3)
    original = damage_spell(10)
    amplified = mega_damage(10)
    print(f"Original: {original}, Amplified: {amplified}")
    print()

    print("Testing conditional caster...")
    safe_spell = conditional_caster(is_powerful, damage_spell)
    result1 = safe_spell(60)
    result2 = safe_spell(30)
    print(f"Power 60: {result1}")
    print(f"Power 30: {result2}")
    print()

    print("Testing spell sequence...")
    multi_cast = spell_sequence([fireball, heal, lightning])
    results = multi_cast("Goblin")
    for r in results:
        print(f"  - {r}")
    print()

    print("Higher-order function mastery demonstrated!")

if __name__ == "__main__":
    main()
