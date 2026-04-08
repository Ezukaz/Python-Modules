#!/usr/bin/env python3

from ex0.Card import Card
from ex1.Consts import CREATURE


class CreatureCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int
    ) -> None:
        """Adds attack and health attributes

        Args:
            attack (int): Needs to be positive integer
            health (int): Needs to be positive integer

        Raises:
            ValueError: If negative integer was passed
        """
        super().__init__(name, cost, rarity)
        if attack < 0 or health < 0:
            raise ValueError("Attack and health must be positive integers")
        self.attack = attack
        self.health = health
        self.type = CREATURE

    def play(self, game_state: dict) -> dict:
        effect = f"{self.type.capitalize()} summoned to battlefield"
        return self._base_play_logic(game_state, effect)

    def attack_target(self, target: str) -> dict:
        combat_resolved = self.health > 0
        return {
            'attacker': self.name,
            'target': target,
            'damage_dealt': self.attack,
            'combat_resolved': combat_resolved,
        }

    def get_card_info(self) -> dict:
        creature_info = super().get_card_info()
        creature_info['type'] = self.type
        creature_info['attack'] = self.attack
        creature_info['health'] = self.health
        return creature_info
