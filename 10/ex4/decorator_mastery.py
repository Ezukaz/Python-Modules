#!/usr/bin/env python3
from collections.abc import Callable
from functools import wraps
from time import perf_counter


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = perf_counter()
        result = func(*args, **kwargs)
        elapsed = perf_counter() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(power: int, *args, **kwargs) -> str:
            if power < min_power:
                return "Insufficient power for this spell"
            return func(power, *args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper()


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:


    def cast_spell(self, spell_name: str, power: int) -> str:

