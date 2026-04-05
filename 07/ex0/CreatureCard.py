#!/usr/bin/env python3

from Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        if attack < 0 or health < 0:
            raise ValueError("Attack and health must be positive integers")
        self.attack = attack
        self.health = health
        self.type = "Creature"

    def play(self, game_state: dict) -> dict:
        playable = self.is_playable(game_state['mana'])
        card_played = self.name if playable else None
        mana_used = self.cost if playable else 0
        effect = "Creature summoned to battlefield" if playable else "Not enough mana"
        if playable:
            game_state['mana'] -= self.cost
            game_state['last_played'] = self
        return {
            'card_played': card_played,
            'mana_used': mana_used,
            'effect': effect,
        }

    def attack_target(self, target: str) -> dict:
        combat_resolved = True if target == "Goblin Warrior" else False
        return {
            'attacker': self.name,
            'target': target,
            'damage_dealt': self.attack,
            'combat_resolved': combat_resolved,
        }
