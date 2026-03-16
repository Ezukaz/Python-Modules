#!/usr/bin/env python3
"""Exercise 3: Achievement Hunter - Set-based achievement analytics"""

from typing import Set


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
    all_achievements = alice | bob | charlie
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}")
    common_all = alice & bob & charlie
    print(f"Common to all players: {common_all}")
    rares = {
        ach for player in (alice, bob, charlie)
        for ach in player
        if sum(1 for p in (alice, bob, charlie) if ach in p) == 1
    }
    print(f"Rare achievements (1 player): {rares}")
    alice_bob_common = alice & bob
    print(f"Alice vs Bob common: {alice_bob_common}")
    alice_unique = alice - bob
    print(f"Alice unique: {alice_unique}")
    bob_unique = bob - alice
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    demonstrate_achievements()
