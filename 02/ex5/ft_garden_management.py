#!/usr/bin/env python3

from typing import Dict, Any


class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    """ Garden management system with error handling """
    def __init__(self) -> None:
        self.plants: Dict[str, Dict[str, Any]] = {}

    def add_plant(
            self,
            name: str = None,
            water: int = 5,
            sun: int = 8
    ) -> None:
        """ Add plant if name is valid. Default sun & water are 8 & 5"""
        try:
            if not name or name == "":
                raise PlantError("Plant name cannot be empty!")
            else:
                self.plants[name] = {"water": water, "sun": sun}
                print(f"Added {name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self) -> None:
        """ Water all plants and cleanup after """
        print("Opening watering system")
        try:
            if not self.plants:
                raise WaterError(" because there are no plants")
            for name in self.plants:
                print(f"Watering {name} - success")
        except WaterError as e:
            print(f"Watering interrupted{e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self, name: str = None) -> None:
        """ Check health of plant """
        try:
            plant = self.plants[name]
            water = plant["water"]
            sun = plant["sun"]
            error_msg = ""
            if water > 10 or water < 1:
                error_msg += (
                    f"\nWater level {water} is too "
                    f"{'high' if water > 10 else 'low'} "
                    f"({'max 10' if water > 10 else 'min 1'})"
                )
            if sun < 2 or sun > 12:
                error_msg += (
                    f"\nSunlight hours {sun} is too "
                    f"{'low' if sun < 2 else 'high'} "
                    f"({'min 2' if sun < 2 else 'max 12'})"
                )
            if error_msg:
                raise PlantError(error_msg)
            print(
                f"{name}: healthy "
                f"(water: {plant['water']}, sun: {plant['sun']})"
            )
        except KeyError:
            print(f"Error: Plant '{name}' not found")
        except PlantError as e:
            print(f"Error checking {name}: {e}")

    @staticmethod
    def test_water_tank(water_level: int = 0) -> None:
        """ Simulate water tank failure. Default water level is 0 """
        if (water_level < 1):
            raise WaterError("Not enough water in tank")


def test_garden_management() -> None:
    """Comprehensive garden management test."""
    print("=== Garden Management System ===")
    print()
    manager = GardenManager()

    print("Adding plants to garden...")
    manager.add_plant("")
    manager.add_plant()
    manager.add_plant("")  # Should fail
    print()

    print("Watering plants...")
    manager.water_plants()
    print()

    print("Checking plant health...")
    manager.check_health()
    manager.check_health("lettuce")  # Will have bad water level
    print()

    print("Testing error recovery...")
    try:
        manager.test_water_tank()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")
        print()

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
