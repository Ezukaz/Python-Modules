#!/usr/bin/env python3

from typing import List


def water_plants(plant_list: List[str | None] = ["corn", "bean"]) -> None:
    """ Water plants with guaranteed cleanup using finally block """
    print("Opening watering system")

    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
                # use raise for bad cases. In this case, None is a valid value
                # for ValueError so we raise it
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """ Test watering with normal and error cases """
    print("=== Garden Watering System ===")
    # Normal case
    print()
    print("Testing normal watering...")
    water_plants()
    print("Watering completed successfully!")
    # Error case
    print()
    print("Testing with error...")
    water_plants(["tomato", None])  # Will trigger error
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
