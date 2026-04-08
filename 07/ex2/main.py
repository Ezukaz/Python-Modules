#!/usr/bin/env python3

from ex2.EliteCard import EliteCard


if __name__ == "__main__":

    print("\n=== DataDeck Ability System ===")

    print("\nEliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    elite_card = EliteCard("Arcane Warrior", 4, "Ultra rare", 5, 100, "melee")
    print(f"\nPlaying {elite_card.name} ({elite_card.__class__.__name__}):")
    print("\nCombat phase:")
    print(f"Attack result: {elite_card.attack('Enemy')}")
    print(f"Defense result: {elite_card.defend(5)}")

    print("\nMagic phase:")
    print(
        "Spell cast: "
        f"{elite_card.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}"
    )
    print(f"Mana channel: {elite_card.channel_mana(7)}")

    print("\nMultiple interface implementation successful!")
