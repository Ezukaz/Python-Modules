#!/usr/bin/env python3

from abc import ABC, abstractmethod
from ex0.Card import Card
from ex1.Deck import Deck
from typing import Any


class CardFactory(ABC, Deck):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_supported_types(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_factory_name(self) -> str:
        pass
