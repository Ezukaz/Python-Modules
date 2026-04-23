#!/usr/bin/env python3

from ex0.Card import Card
from ex1.Consts import SPELL
from typing import Any


class SpellCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        effect_type: str
    ) -> None:
        """
        Args:
            effect_type (str): Use damage, heal, buff, or debuff
        """
        super().__init__(name, cost, rarity)
        self.attack = cost
        self.effect_type = effect_type
        self.type = SPELL

    def play(self, game_state: dict[str, Any]) -> dict[str, str | int | None]:
        effect = f"Deal {self.attack} {self.effect_type} to target"
        return self._base_play_logic(game_state, effect)

    def resolve_effect(self, targets: list[Any]) -> dict[str, Any]:
        return {
            'spell': self.name,
            'effect': self.effect_type,
            'mana_used': self.cost,
            'fx_summary': f"Dealt {self.effect_type} to {', '.join(targets)}",
        }

    def get_card_info(self) -> dict[str, Any]:
        spell_info = super().get_card_info()
        spell_info['type'] = self.type
        spell_info['effect_type'] = self.effect_type
        return spell_info
