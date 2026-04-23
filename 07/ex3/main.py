#!/usr/bin/env python3

from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


if __name__ == "__main__":
    try:
        engine = GameEngine()
        engine.configure_engine(FantasyCardFactory(), AggressiveStrategy())
        assert engine.factory is not None
        assert engine.strategy is not None
        print("\n=== DataDeck Game Engine ===")

        print("\nConfiguring Fantasy Card Game...")
        print(f"Factory: {engine.factory.get_factory_name()}")
        print(f"Strategy: {engine.strategy.get_strategy_name()}")
        print(f"Available types: {engine.factory.get_supported_types()}")

        print("\nSimulating aggressive turn...")
        format_dup = [f"{c.name} ({c.cost})" for c in engine.factory._hand]
        print(f"Hand: [{', '.join(format_dup)}]")

        print("\nTurn execution:")
        print(f"Strategy: {engine.strategy.get_strategy_name()}")
        print(f"Actions: {engine.simulate_turn()}")

        status = engine.get_engine_status()
        print("\nGame Report:")
        print(f"{status}")

        print(
            "\nAbstract Factory + Strategy Pattern: "
            "Maximum flexibility achieved!"
        )
    except Exception as e:
        print("Error:", e)
