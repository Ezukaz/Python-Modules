#!/usr/bin/env python3

from ex0.CreatureCard import CreatureCard


if __name__ == "__main__":
    game_state = {
        'mana': 6,
        'last_played': None,
    }

    print("\n=== DataDeck Card Foundation ===")

    print("\nTesting Abstract Base Class Design:")

    creature = None
    try:
        creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    except ValueError as e:
        print(e)
    if creature:
        print("\nCreatureCard Info:")
        print(creature.get_card_info())

        print(
            f"\nPlaying {creature.name} with "
            f"{game_state['mana']} mana available:"
        )
        print(f"Playable: {creature.is_playable(game_state['mana'])}")
        print(f"Play result: {creature.play(game_state)}")

        target = "Goblin Warrior"
        print(f"\n{creature.name} attacks {target}:")
        print(f"Attack result: {creature.attack_target(target)}")

        insufficient_mana = 3
        insufficient_mana = (
            insufficient_mana if insufficient_mana < creature.cost else 0
        )
        print(f"\nTesting insufficient mana ({insufficient_mana} available):")
        print(f"Playable: {creature.is_playable(insufficient_mana)}")

        print("\nAbstract pattern successfully demonstrated!")
    else:
        print("\nAbstract pattern unsuccessfully demonstrated!")
