import functools
import time
from typing import Callable, Any

def spell_timer(func: Callable) -> Callable:

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed = round(end_time - start_time, 3)
        print(f"Spell completed in {elapsed} seconds")
        return result
    return wrapper

def power_validator(min_power: int) -> Callable:

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:

            if args:
                power = args[0]
            elif 'power' in kwargs:
                power = kwargs['power']
            else:
                power = 0

            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator

def retry_spell(max_attempts: int) -> Callable:

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying... (attempt {attempt}/{max_attempts})")
                    else:
                        return f"Spell casting failed after {max_attempts} attempts"
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator

class MageGuild:

    def __init__(self, guild_name: str) -> None:

        self.guild_name = guild_name

    @staticmethod
    def validate_mage_name(name: str) -> bool:

        if len(name) < 3:
            return False
        return all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:

        return f"Successfully cast {spell_name} with {power} power"

def main() -> None:

    print("=== Master's Tower ===")
    print()

    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")
    print()

    print("Testing power validator...")

    @power_validator(min_power=50)
    def mega_spell(power: int) -> str:
        return f"Mega spell cast with {power} power!"

    print(mega_spell(60))
    print(mega_spell(30))
    print()

    print("Testing retry spell...")

    fail_count = 0

    @retry_spell(max_attempts=3)
    def unreliable_spell() -> str:
        nonlocal fail_count
        fail_count += 1
        if fail_count < 3:
            raise Exception("Spell unstable!")
        return "Spell finally worked!"

    result = unreliable_spell()
    print(f"Result: {result}")
    print()

    fail_count = 0

    @retry_spell(max_attempts=2)
    def always_fails() -> str:
        raise Exception("Always fails!")

    print("Testing always-failing spell:")
    result = always_fails()
    print(f"Result: {result}")
    print()

    print("Testing MageGuild...")

    print(f"'Eldrin the Wise' valid: {MageGuild.validate_mage_name('Eldrin the Wise')}")
    print(f"'X1' valid: {MageGuild.validate_mage_name('X1')}")
    print(f"'AB' valid: {MageGuild.validate_mage_name('AB')}")
    print()

    guild = MageGuild("Arcane Order")

    print("Testing cast_spell with power validation:")

    @power_validator(min_power=10)
    def guild_cast(power: int, spell_name: str) -> str:
        return f"Successfully cast {spell_name} with {power} power"

    print(guild_cast(15, "Lightning"))
    print(guild_cast(5, "Spark"))
    print()

    print("Decorator mastery demonstrated!")

if __name__ == "__main__":
    main()
