#!/usr/bin/env python3

import alchemy
from alchemy.elements import create_earth, create_air


def healing_potion() -> str:
    return (
        f"Healing potion brewed with {alchemy.create_fire()} "
        f"and {alchemy.create_water()}"
    )


def strength_potion() -> str:
    return (
        f"Strength potion brewed with {create_earth()} "
        f"and {alchemy.create_fire()}"
    )


def invisibility_potion() -> str:
    return (
        f"Invisibility potion brewed with {create_air()} "
        f"and {alchemy.create_water()}"
    )


def wisdom_potion() -> str:
    elements = ", ".join([
        alchemy.create_fire(),
        alchemy.create_water(),
        create_earth(),
        create_air(),
        ])
    return (
        f"Wisdom potion brewed with all elements: {elements}")
