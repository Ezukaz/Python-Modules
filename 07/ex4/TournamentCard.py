#!/usr/bin/env python3

from ex1.Consts import TOURNAMENT
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    # Constructor
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        id: str,
        atk: int,
        hp: int,
        combat_type: str,
        rating: int = 1200
    ) -> None:
        super().__init__(name, cost, rarity)
        self.rating = rating
        self.record = "0-0"
        self.id = id
        self.type = TOURNAMENT
        self.atk = atk
        self.hp = hp
        self.combat_type = combat_type
        self.inflicted_damage = 0
        self.incurred_damage = 0
        self.wins = 0
        self.losses = 0

    # Inherit from Card
    def play(self, game_state: dict) -> dict:
        effect = f"{self.type.capitalize()} card summoned to arena"
        return self._base_play_logic(game_state, effect)

    # Inherit from Combatable
    def attack(self, target: str) -> dict:
        self.inflicted_damage += self.atk
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.atk,
            'combat_type': self.combat_type,
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_blocked = incoming_damage * 2 // 3
        damage = incoming_damage - damage_blocked
        self.incurred_damage += damage
        return {
            'defender': self.name,
            'damage_taken': damage,
            'damage_blocked': damage_blocked,
            'still_alive': damage < self.hp,
        }

    def get_combat_stats(self) -> dict:
        return {
            'damage_given': self.inflicted_damage,
            'damage_taken': self.incurred_damage,
        }

    # Inherit from Rankable
    def calculate_rating(self) -> int:
        win, loss = self.record.split("-")
        self.rating += (int(win) - int(loss)) * 16
        if self.rating < 0:
            self.rating = 0
        return self.rating

    def update_wins(self, wins: int) -> None:
        win, loss = self.record.split("-")
        win = str(wins)
        self.record = win + "-" + loss

    def update_losses(self, losses: int) -> None:
        win, loss = self.record.split("-")
        loss = str(losses)
        self.record = win + "-" + loss

    def get_rank_info(self) -> dict:
        return {
            'interfaces': ["Card", "Combatable", "Rankable"],
            'rating': self.rating,
            'record': self.record,
        }

    # Non-inherit methods
    def get_tournament_stats(self) -> dict:
        win, loss = self.record.split("-")
        return {
            'wins': win,
            'losses': loss,
        }
