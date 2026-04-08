#!/usr/bin/env python3

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        atk: int,
        hp: int,
        combat_type: str
    ) -> None:
        super().__init__(name, cost, rarity)
        self.atk = atk
        self.hp = hp
        self.combat_type = combat_type
        self.spell = None
        self.spell_cost = None

    def play(self, game_state: dict) -> dict:
        effect = "Elite abstract whisp summoned to battlefield"
        return self._base_play_logic(game_state, effect)

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        cost = len(spell_name)
        self.spell = spell_name
        self.spell_cost = cost
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': cost,
        }

    def channel_mana(self, amount: int) -> dict:
        channel = amount - self.cost if amount > self.cost else 0
        return {
            'channeled': channel,
            'total_mana': amount,
        }

    def get_magic_stats(self) -> dict:
        return {
            'caster': self.name,
            'spell': self.spell,
            'spell_cost': self.spell_cost,
        }

    def attack(self, target: str) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.atk,
            'combat_type': self.combat_type,
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_blocked = incoming_damage * 2 // 3
        damage = incoming_damage - damage_blocked
        return {
            'defender': self.name,
            'damage_taken': damage,
            'damage_blocked': damage_blocked,
            'still_alive': damage < self.hp,
        }

    def get_combat_stats(self) -> dict:
        return {
            'attack_pwr': self.atk,
            'hp': self.hp,
            'combat_type': self.combat_type,
        }
