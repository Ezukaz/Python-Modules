#!/usr/bin/env python3
from typing import Any
from collections.abc import Callable
import functools
import operator


# Reduces a list(check if max or min is the correct way)
def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    if operation.lower() == "add":
        return functools.reduce(operator.add, spells)
    elif operation.lower() == "multiply":
        return functools.reduce(operator.mul, spells)
    elif operation.lower() == "max":
        return functools.reduce(max, spells)
    elif operation.lower() == "min":
        return functools.reduce(min, spells)
    else:
        raise ValueError("Invalid operator passed")


# Remakes func without a redundant param
def partial_enhancer(base_enchantment: Callable) -> dict[str, Callable]:
    shortened = functools.partial(base_enchantment, 50, "fire")

    return {
        'goblin': shortened("goblin"),
        'death_eater': shortened("death_eater"),
        'wyvern': shortened("wyvern"),
    }


def base_enchant(power: int, element: str, target: str) -> str:
    """For the partial_enhancer()"""
    return (
        f"{element.capitalize()} element hits "
        f"{power} {target}{'s' if power != 1 else ''}"
    )


# Saves same input call to cache
@functools.lru_cache  # (maxsize=None)
def memorized_fibonacci(n: int) -> int:
    if not n:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    i = 0

    while i < n - 1:
        c = a + b
        a = b
        b = c
        i += 1
    return b


# Making an overloading function
def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def base_spell(inp: Any) -> str:
        res = (
            "***ERROR: Unknown spell type***\n"
            f"      Input type: {type(inp).__name__.capitalize()}"
        )
        return res

    @base_spell.register(int)
    def _(inp: int) -> str:
        return f"Damage spell: {inp} damage"

    @base_spell.register
    def _(inp: str) -> str:
        return f"Enchantment: {inp}"

    @base_spell.register
    def _(inp: list) -> str:
        list_len = len(inp)
        return f"Mult-cast: {list_len} spell{'s' if list_len != 1 else ''}"

    return base_spell


if __name__ == "__main__":
    spell_powers = [23, 29, 31, 31, 30, 26]
    operations = ['add', 'multiply', 'max', 'min']
    fibonacci_tests = [0, 1, 10, 15]
    dispatch_tests = [
        42,
        "fireball",
        [base_enchant, spell_reducer, memorized_fibonacci],
        {'steady': 2, 'ready': 1, 'go': 3},
    ]

    # For spell_reducer()
    print("\nTesting spell reducer...")
    for op in operations:
        print(f"{op.capitalize()}: {spell_reducer(spell_powers, op)}")
    # For memorizing_fibonacci()
    print("\nTesting memorized fibonacci...")
    for fib in fibonacci_tests:
        print(f"Fib({fib}): {memorized_fibonacci(fib)}")
        # print(memorized_fibonacci.cache_info())
    # For partial_enchanter()
    print("\nTesting partial enchanter...")
    for x in partial_enhancer(base_enchant).values():
        print(x)
    # For spell_dispatcher()
    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    for x in dispatch_tests:
        print(dispatch(x))
