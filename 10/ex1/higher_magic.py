#!/usr/bin/env python3
from collections.abc import Callable


# This is called closure
def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        res1 = spell1(target, power)
        res2 = spell2(target, power)
        return (res1, res2)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amp(target: str, power: int) -> str:
        base_res = base_spell(target, power * multiplier)
        return base_res
    return amp


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cast_cond(target: str, power: int) -> str:
        return (
            spell(target, power) if condition(target, power)
            else "Spell fizzled"
        )
    return cast_cond


def spell_sequence(spells: list[Callable]) -> Callable:
    def cast_order(target: str, power: int) -> list[str]:
        res = []
        for spell in spells:
            res.append(spell(target, power))
        return res
    return cast_order


def spell(target: str, power: int) -> str:
    return f"{target} is affected by {power} points"


if __name__ == "__main__":
    powers = [24, 23, 18]
    targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    try:
        print("\nTesting spell combiner...")
        combiner = spell_combiner(
            spell, lambda t, p: f"and {t} is affected by {p} extra points"
        )
        print("Combined spell results: ", end="")
        print(*combiner(targets[0], powers[0]), sep=", ")

        print("\nTesting power amplifier...")
        amper = power_amplifier(spell, 3)
        print(
            f"Original: {spell(targets[1], powers[1])}, "
            f"Amplified: {amper(targets[1], powers[1])}"
        )

        print("\nTesting conditional_caster...")
        filter_cast = conditional_caster(lambda _, p: p > 6, spell)
        print(filter_cast(targets[3], 8))

        print("\nTesting spell sequence...")
        spell_seq = spell_sequence([
            lambda t, p: f"{t} obliterated by {p} fireball!",
            lambda t, p: f"{t} incinerated by {p} dragonfire!",
            lambda t, p: f"{t} nullified by {p} holy water!"
        ])
        for x in spell_seq("Wingardium Leviosa", 7):
            print(x)
    except Exception as e:
        print("Unexpected error! Good job finding it!!")
        print(f"{type(e).__name__}: {e}")
