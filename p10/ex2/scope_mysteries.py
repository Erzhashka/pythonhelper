from typing import Callable, Any

def mage_counter() -> Callable[[], int]:

    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter

def spell_accumulator(initial_power: int) -> Callable[[int], int]:

    total_power = initial_power

    def accumulate(amount: int) -> int:
        nonlocal total_power
        total_power += amount
        return total_power

    return accumulate

def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:

    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant

def memory_vault() -> dict[str, Callable]:

    memories: dict[str, Any] = {}

    def store(key: str, value: Any) -> str:
        memories[key] = value
        return f"Memory '{key}' stored"

    def recall(key: str) -> Any:
        if key in memories:
            return memories[key]
        return "Memory not found"

    return {'store': store, 'recall': recall}

def main() -> None:

    print("=== Memory Depths ===")
    print()

    print("Testing mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")

    counter2 = mage_counter()
    print(f"New counter, Call 1: {counter2()}")
    print()

    print("Testing spell accumulator...")
    power = spell_accumulator(100)
    print(f"Initial: 100")
    print(f"Add 25: {power(25)}")
    print(f"Add 50: {power(50)}")
    print(f"Add 10: {power(10)}")
    print()

    print("Testing enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    electric = enchantment_factory("Electric")

    print(flaming("Sword"))
    print(frozen("Shield"))
    print(electric("Staff"))
    print()

    print("Testing memory vault...")
    vault = memory_vault()

    print(vault['store']('secret_spell', 'Fireball'))
    print(vault['store']('power_level', 9001))

    print(f"Recall 'secret_spell': {vault['recall']('secret_spell')}")
    print(f"Recall 'power_level': {vault['recall']('power_level')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")
    print()

    print("Closure and scoping mastery demonstrated!")

if __name__ == "__main__":
    main()
