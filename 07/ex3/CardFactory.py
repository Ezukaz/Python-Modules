#!/usr/bin/env python3

from abc import ABC, abstractmethod
from ex0.Card import Card
from ex1.Deck import Deck


class CardFactory(ABC, Deck):
    def __init__(self) -> None:
        Deck.__init__(self)

    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        ...

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        ...

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        ...

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        ...

    @abstractmethod
    def get_supported_types(self) -> dict:
        ...

    @abstractmethod
    def get_factory_name(self) -> str:
        ...
