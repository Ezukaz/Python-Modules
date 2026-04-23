#!/usr/bin/env python3
from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    count1 = 0
    count2 = 0

    def counter(is_first: bool) -> int:
        if is_first:
            nonlocal count1
            count1 += 1
            return count1
        else:
            nonlocal count2
            count2 += 1
            return count2

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def acumulator(buff: int) -> int:
        nonlocal power
        power += buff
        return power

    return acumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(name: str) -> str:
        return f"{enchantment_type.capitalize()} {name.capitalize()}"

    return enchant


def memory_vault() -> dict[str, Callable]:
    vault = {}

    def store(key: str, value: Any) -> None:
        nonlocal vault
        vault.update({key: value})

    def recall(key: str) -> Any | str:
        nonlocal vault
        return vault.get(key, "Memory not found")

    return {
        'store': store,
        'recall': recall,
    }


if __name__ == "__main__":
    try:
        print("\nTesting mage counter...")
        counter = mage_counter()
        print(f"counter_a {counter(True)} calls")
        print(f"counter_a {counter(True)} calls")
        print(f"counter_b {counter(False)} calls")

        print("\nTesting spell accumulator...")
        base = 100
        add = 20
        accumulator = spell_accumulator(base)
        print(f"Base {base}, add {add}: {accumulator(add)}")
        add = 30
        print(f"Base {base}, add {add}: {accumulator(add)}")

        print("\nTesting enchantment factory...")
        burn = enchantment_factory("flaming")
        print(burn("sword"))
        freeze = enchantment_factory("frozen")
        print(freeze("shield"))

        print("\nTesting memory vault...")
        vault = memory_vault()
        key1 = "secret"
        val = 42
        vault['store'](key1, val)
        print(f"Store {repr(key1)} = {val}")
        print(f"Recall {repr(key1)}: {vault['recall'](key1)}")
        key2 = "unknown"
        print(f"Recall {repr(key2)}: {vault['recall'](key2)}")
    except Exception as e:
        print("Unexpected error! Good job finding it!!")
        print(f"{type(e).__name__}: {e}")
