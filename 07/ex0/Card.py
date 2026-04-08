#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.type = ""

    def _base_play_logic(self, game_state: dict, effect: str) -> dict:
        playable = self.is_playable(game_state['mana'])
        card_played = self.name if playable else None
        mana_used = self.cost if playable else 0
        if_effect = effect if playable else "Not enough mana"
        if playable:
            game_state['mana'] -= self.cost
            game_state['last_played'] = self
        return {
            'card_played': card_played,
            'mana_used': mana_used,
            'effect': if_effect,
        }

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        ...

    def get_card_info(self) -> dict:
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity,
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
