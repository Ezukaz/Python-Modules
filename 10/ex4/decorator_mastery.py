#!/usr/bin/env python3
from typing import Any
from collections.abc import Callable
from functools import wraps
from time import sleep, perf_counter


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: list, **kwargs: dict) -> str:
        print(f"Casting {args[0]}...")
        start = perf_counter()
        sleep(0.1)
        result = func(*args, **kwargs)
        elapsed = perf_counter() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(power: int, *args: list, **kwargs: dict) -> Any:
            if power < min_power:
                return "Insufficient power for this spell"
            return func(power, *args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: list, **kwargs: dict) -> Any:
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        "Spell failed, retrying... "
                        f"(attempt {attempt + 1}/{max_attempts})"
                    )
            print(f"Spell casting failed after {max_attempts} attempts")
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        only_letters_spaces = all(c.isalpha() or c.isspace() for c in name)
        return len(name) >= 3 and only_letters_spaces

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
            return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    test_powers = [14, 28, 7, 17]
    spell_names = ['lightning', 'blizzard', 'flash', 'freeze']
    mage_names = ['Rowan', 'Jordan', 'Phoenix', 'Casey', 'Alex', 'Luna']
    invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']

    guild = MageGuild()

    @spell_timer
    def cast(spell: str) -> str:
        return f"{spell.capitalize()} cast!"

    @retry_spell(max_attempts=3)
    def test_spell() -> None:
        int("test")
        print(f"Spell succeeded!")

    # SleepTimer Test
    print("\nTesting spell timer...")
    for spell in spell_names:
        print(f"Result: {cast(spell)}")

    # RetrySpell Test
    print("\nTesting retrying_spell...")
    test_spell()
    print(f"{test_spell.__name__.capitalize()} spelled!")

    # MageGuild Test
    print("\nTesting MageGuild...")
    print(guild.validate_mage_name("Klingon"))
    print(guild.validate_mage_name("Kwaigon8"))
    for p, n in zip(test_powers, spell_names):
        print(guild.cast_spell(p, power=n))
