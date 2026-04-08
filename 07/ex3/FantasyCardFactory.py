#!/usr/bin/env python3

from ex0.Card import Card
from ex1.Consts import DAMAGE, CREATURE, SPELL, ARTIFACT
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory
import random


class FantasyCardFactory(CardFactory, CreatureCard, SpellCard, ArtifactCard):
    def __init__(self) -> None:
        CardFactory.__init__(self)
        self._supported_types = {}

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        default_name = "Dragon"
        default_power = 5
        name = default_name
        power = default_power

        if isinstance(name_or_power, str):
            name = name_or_power
        if isinstance(name_or_power, int):
            power = name_or_power

        return CreatureCard(name, 5, "Yeah, rare", power, 50)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        default_name = "Fireball"
        default_power = 5
        name = default_name
        power = default_power

        if isinstance(name_or_power, str):
            name = name_or_power
        if isinstance(name_or_power, int):
            power = name_or_power

        return SpellCard(name, 5, "Yeah, rare", power, DAMAGE)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        default_name = "Holy grail"
        default_duration = 5000
        name = default_name
        duration = default_duration

        if isinstance(name_or_power, str):
            name = name_or_power
        if isinstance(name_or_power, int):
            duration = name_or_power

        return ArtifactCard(name, 5, "Yeah, rare", duration, "+3 damage")

    def create_themed_deck(self, size: int) -> dict:
        deck = {
            CREATURE: [],
            SPELL: [],
            ARTIFACT: [],
        }
        create_types = [
            self.create_creature(),
            self.create_spell(),
            self.create_artifact()
        ]
        for _ in range(size):
            card = random.choice(create_types)
            self.add_card(card)
            deck[card.type].append(card.name)
        for card in create_types:
            self.add_type(card.type, deck[card.type])
        self.draw_hand(size // 5 + 1)
        return deck

    def add_type(self, category: str, names: list) -> None:
        """Register a type if none exists and add names to type

        Args:
            category (str): Type to register
            names (list): Names to add to type(duplicates will be erased)
        """
        if category not in self._supported_types:
            self._supported_types[category] = set()
        self._supported_types[category].update(names)

    def draw_hand(self, draw_amount: int) -> None:
        cards_in_deck = len(self._deck)
        if draw_amount > cards_in_deck:
            raise ValueError(
                f"Currently {cards_in_deck} cards in deck: "
                f"need at least {draw_amount}"
            )
        self.shuffle()
        for _ in range(draw_amount):
            card = self.draw_card()
            self._hand.append((card.name, card.cost))

    def get_supported_types(self) -> dict:
        return {k + "s": list(v) for k, v in self._supported_types.items()}

    def get_factory_name(self) -> str:
        return self.__class__.__name__


# if __name__ == "__main__":
#     # types = {
#     #     'creatures': [],
#     #     'spells': [],
#     #     'artifacts': [],
#     #     'amulet': ["Azvaldt", "Terra Finis", "Dragonsong Flute", "Azvaldt"]
#     # }
#     factory = FantasyCardFactory()
#     factory.create_themed_deck(10)
#     # for card in factory._deck:
#     #     types[card.type + "s"].append(card.name)
#     # for k, v in types.items():
#     #     factory.add_type(k, v)
#     print(factory.get_supported_types())
