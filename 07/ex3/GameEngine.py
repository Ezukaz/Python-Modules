#!/usr/bin/env python3

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from typing import Any


class GameEngine():
    def __init__(self) -> None:
        self.strategy: GameStrategy | None = None
        self.factory: CardFactory | None = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0
        self.battlefield = [
            ("Enemy Player 1", 8),
            ("Enemy Player 2", 1),
            ("Enemy Player 3", 5)
        ]

    def configure_engine(
        self,
        factory: CardFactory,
        strategy: GameStrategy
    ) -> None:
        """Sets strategy and factory to self.
        From deck built by factory, 5 random cards will be added to engine deck
        which is your hand
        """
        self.strategy = strategy
        self.factory = factory
        self.factory.create_themed_deck(10)
        self.cards_created += len(factory._deck)

    def simulate_turn(self) -> dict[str, Any]:
        self.turns_simulated += 1
        execute = {}
        if self.strategy and self.factory:
            execute = (
                self.strategy.execute_turn(
                    self.factory._hand,
                    self.battlefield
                )
            )
        self.total_damage += execute['damage_dealt']
        return execute

    def get_engine_status(self) -> dict[str, Any]:
        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': self.strategy.__class__.__name__,
            'total_damage': self.total_damage,
            'cards_created': self.cards_created,
            'card_pack': self.factory.__class__.__name__
        }
