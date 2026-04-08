#!/usr/bin/env python3

from ex0.Card import Card
from ex1.Consts import SPELL


class SpellCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        effect_type: str
    ) -> None:
        """
        Args:
            effect_type (str): Use damage, heal, buff, or debuff
        """
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.effect_type = effect_type
        self.type = SPELL

    def play(self, game_state: dict) -> dict:
        effect = f"Deal {self.attack} {self.effect_type} to target"
        return self._base_play_logic(game_state, effect)

    def resolve_effect(self, targets: list) -> dict:
        return {
            'spell': self.name,
            'effect': self.effect_type,
            'mana_used': self.cost,
            'fx_summary': f"Dealt {self.effect_type} to {', '.join(targets)}",
        }

    def get_card_info(self) -> dict:
        spell_info = super().get_card_info()
        spell_info['type'] = self.type
        spell_info['effect_type'] = self.effect_type
        return spell_info
