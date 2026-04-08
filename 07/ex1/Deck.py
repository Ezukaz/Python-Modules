#!/usr/bin/env python3

from ex0.Card import Card
from ex1.Consts import CREATURE, ARTIFACT, SPELL
import random


class Deck():
    def __init__(self) -> None:
        self._deck = []
        self._hand = []

    def add_card(self, card: Card) -> None:
        self._deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Remove card from deck

        Args:
            card_name (str): Card to remove

        Returns:
            bool: False if no card was found else True

        Raises:
            IndexError if list empty or index out of range. But i don't think
            it will ever trigger
        """
        for i, card in enumerate(self._deck):
            if card.name == card_name:
                self._deck.pop(i)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self._deck)

    def draw_card(self) -> Card:
        if not self._deck:
            raise ValueError("Deck is empty")
        return self._deck.pop(0)

    def get_deck_status(self) -> dict:
        total = len(self._deck)
        deck_cost = sum(card.cost for card in self._deck)
        return {
            'total_cards': total,
            'creatures': sum(1 for c in self._deck if c.type == CREATURE),
            'spells': sum(1 for c in self._deck if c.type == SPELL),
            'artifacts': sum(1 for c in self._deck if c.type == ARTIFACT),
            'avg_cost': round(deck_cost / total, 1) if total else 0.0,
        }
