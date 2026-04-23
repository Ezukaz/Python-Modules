#!/usr/bin/env python3

from ex0.Card import Card
from ex1.Consts import ARTIFACT
from typing import Any


class ArtifactCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        durability: int,
        effect: str
    ) -> None:
        """
        Args:
            durability (int): How many turns effect lasts
            effect (str): Effect of artifact. E.g., +1 mana, +2 damange for all
            allies, or -1 hp for opponent
        """
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.type = ARTIFACT

    def play(self, game_state: dict[str, Any]) -> dict[str, str | int | None]:
        self.activate_ability()
        effect_turns = (
            "Permanent" if self.durability <= 0
            else f"For {self.durability} turns"
        )
        effect = f"{effect_turns}: {self.effect} per turn"
        return self._base_play_logic(game_state, effect)

    def activate_ability(self) -> dict[str, Any]:
        return {
            'artifact': self.name,
            'effect': self.effect,
            'mana_used': self.cost,
            'effect_summary': self.effect,
            'durability': self.durability
        }

    def get_card_info(self) -> dict[str, Any]:
        artifact_info = super().get_card_info()
        artifact_info['type'] = self.type
        artifact_info['durability'] = self.durability
        artifact_info['effect'] = self.effect
        return artifact_info
