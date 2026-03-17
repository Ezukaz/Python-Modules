#!/usr/bin/env python3
"""Exercise 3: Achievement Hunter - Set-based achievement analytics"""

from typing import Set


# | Union - everything from both
# ^ Symmetric difference - what they don't share
# Opposites
# & Intersection - only what both share
# - Difference - what left has that right does not
# __dunder__ double underscore methods are special methods that Python calls
# behind the scenes. + is actually __add__ so that is why the + sign is so
# powerful in python. The set operators are the same. Normally, those signs
# are bit-wise operators but under the hood in sets those operators are
# converted by the dunder methods. Dunder methods are customizable. Dream big
def demonstrate_achievements() -> None:
    """Demonstrate set operations for achievement tracking."""
    print("=== Achievement Tracker System ===")
    alice: Set[str] = {
        'first_kill',
        'level_10',
        'treasure_hunter',
        'speed_demon'
    }
    bob: Set[str] = {
        'first_kill',
        'level_10',
        'boss_slayer',
        'collector'
    }
    charlie: Set[str] = {
        'level_10',
        'treasure_hunter',
        'boss_slayer',
        'speed_demon',
        'perfectionist'
    }
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")
    print("\n=== Achievement Analytics ===")
    all_achievements = alice | bob | charlie  # Union combines unique elements
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}")
    common_all = alice & bob & charlie  # Intersection operator
    print()
    print(f"Common to all players: {common_all}")
    rares = {
        ach for player in (alice, bob, charlie)
        for ach in player
        if sum(1 for p in (alice, bob, charlie) if ach in p) == 1
    }
    # Achievement is 1 when found in player, sum all 1s and if the sum is 1,
    # that ach is a rare
    # If there are only two players to compare then ^ would suffice. But
    # finding the unique out of three is different as what is unique in the
    # two would not necessarily mean unique out of the three
    # A value before the for means what to produce. It is the equivalent of
    # rare.add(ach)
    """
    [ach for ach in player]  # list  — square brackets
    {ach for ach in player}  # set   — curly brackets
    (ach for ach in player)  # generator — round brackets (lazy, doesn't store)
    {ach: 1 for ach in player} # dict — curly with colon
    """
    print(f"Rare achievements (1 player): {rares}")
    alice_bob_common = alice & bob
    print()
    print(f"Alice vs Bob common: {alice_bob_common}")
    alice_unique = alice - bob
    print(f"Alice unique: {alice_unique}")
    bob_unique = bob - alice
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    demonstrate_achievements()
