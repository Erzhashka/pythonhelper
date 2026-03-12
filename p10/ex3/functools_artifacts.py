import functools
import operator
from typing import Callable, Any

def spell_reducer(spells: list[int], operation: str) -> int:

    if not spells:
        return 0

    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")

    op_func = operations[operation]

    if operation in ("max", "min"):
        return functools.reduce(lambda a, b: op_func(a, b), spells)

    return functools.reduce(op_func, spells)

def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:

    return {
        'fire_enchant': functools.partial(base_enchantment, 50, 'fire'),
        'ice_enchant': functools.partial(base_enchantment, 50, 'ice'),
        'lightning_enchant': functools.partial(base_enchantment, 50, 'lightning')
    }

@functools.lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:

    if n < 0:
        raise ValueError("Fibonacci not defined for negative numbers")
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)

def spell_dispatcher() -> Callable:

    @functools.singledispatch
    def cast_spell(arg: Any) -> str:
        return f"Unknown spell type: {type(arg).__name__}"

    @cast_spell.register(int)
    def _(power: int) -> str:
        return f"Damage spell deals {power} damage!"

    @cast_spell.register(str)
    def _(enchantment: str) -> str:
        return f"Enchantment activated: {enchantment}"

    @cast_spell.register(list)
    def _(spells: list) -> str:
        return f"Multi-cast: {len(spells)} spells combined!"

    return cast_spell

def main() -> None:

    print("=== Ancient Library ===")
    print()

    print("Testing spell reducer...")
    powers = [10, 20, 30, 40]
    print(f"Spell powers: {powers}")
    print(f"Sum: {spell_reducer(powers, 'add')}")
    print(f"Product: {spell_reducer(powers, 'multiply')}")
    print(f"Max: {spell_reducer(powers, 'max')}")
    print(f"Min: {spell_reducer(powers, 'min')}")
    print()

    print("Testing partial enchanter...")

    def base_enchant(power: int, element: str, target: str) -> str:
        return f"{element.title()} enchantment ({power} power) applied to {target}"

    enchanters = partial_enchanter(base_enchant)
    print(enchanters['fire_enchant']('Sword'))
    print(enchanters['ice_enchant']('Shield'))
    print(enchanters['lightning_enchant']('Staff'))
    print()

    print("Testing memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(f"Fib(20): {memoized_fibonacci(20)}")

    cache_info = memoized_fibonacci.cache_info()
    print(f"Cache hits: {cache_info.hits}, misses: {cache_info.misses}")
    print()

    print("Testing spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(50))
    print(dispatcher("Flaming"))
    print(dispatcher([1, 2, 3, 4]))
    print(dispatcher(3.14))
    print()

    print("Functools mastery demonstrated!")

if __name__ == "__main__":
    main()
