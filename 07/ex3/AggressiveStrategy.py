#!/usr/bin/env python3

from ex3.GameStrategy import GameStrategy
from ex0.Card import Card
from typing import Any


class AggressiveStrategy(GameStrategy):
    """Prioritizes attacking player -> high threat -> low threat enemies.
    Plays low cost creatures first.
    """
    def execute_turn(
        self,
        hand: list[Card],
        battlefield: list[tuple[str, int]]
    ) -> dict[str, Any]:
        """Plays all cards in hand from lowest cost to highest
        Args:
            hand (list): Contains Card objects
            battlefield (list): Contains tuples which has the card name and hp
        Returns:
            dict: Description of what was executed
        """
        prioritize = self.prioritize_targets(battlefield)
        low_cost_sort = sorted(hand, key=lambda c: c.cost)
        played = [c.name for c in low_cost_sort]
        mana_used = sum(c.cost for c in low_cost_sort)
        attacked = [name for name, _ in prioritize[:len(played)]]
        damage = sum(hp for _, hp in prioritize[:len(played)])
        return {
            'cards_played': played,
            'mana_used': mana_used,
            'targets_attacked': attacked,
            'damage_dealt': damage,
        }

    def get_strategy_name(self) -> str:
        return self.__class__.__name__

    def prioritize_targets(
        self,
        available_targets: list[tuple[str, int]]
    ) -> list[tuple[str, int]]:
        """_summary_
        Args:
            available_targets (list): List of target names
        Returns:
            list: Sorted list from highest to lowest priority target
        """
        player = [(t, _) for t, _ in available_targets if "player" in t]
        high = [(t, hp) for t, hp in available_targets if hp < 2]
        med = [(t, hp) for t, hp in available_targets if hp >= 2 and hp <= 5]
        low = [(t, hp) for t, hp in available_targets if hp > 5]
        return player + high + med + low
