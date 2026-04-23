#!/usr/bin/env python3

from typing import List, Any
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck
from ex1.Consts import DAMAGE


def card_factory() -> List[Card]:
    Card1 = SpellCard("Lightning Bolt", 3, "Kind of rare", DAMAGE)
    Card2 = ArtifactCard("Mana Crystal", 2, "Pretty", 0, "+1 mana per turn")
    Card3 = CreatureCard("Fire Dragon", 5, "Super rare!!!", 50000, 2000000)
    return [Card1, Card2, Card3]


if __name__ == "__main__":
    game_state: dict[str, Any] = {
        'mana': 50,
        'last_played': None,
    }
    cards = card_factory()
    deck = Deck()
    for card in cards:
        deck.add_card(card)
    print("\n=== DataDeck Deck Builder ===")

    print("\nBuilding deck with different card types...")
    print(f"Deck stats: {deck.get_deck_stats()}")

    print("\nDrawing and playing cards:")

    for _ in range(3):
        draw = deck.draw_card()
        print(f"\nDrew: {draw.name} ({draw.type.capitalize()})")
        print(f"Play result: {draw.play(game_state)}")

    print(
        "\nPolymorphism in action: Same interface, different card behaviors!"
    )
