#!/usr/bin/env python3

class Plant:
    """Make a plant instance and print status"""
    def __init__(
        self,
        plant: str = "Rose",
        height: int = 25,
        age: int = 30
    ) -> None:
        """Initialize plant with name, height (cm), and age (days)"""
        self.plant = plant
        self.height = height
        self.age = age

    def print_status(self) -> None:
        """Prints plant status"""
        print(f"{self.plant}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    plant1 = Plant()
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    plant1.print_status()
    plant2.print_status()
    plant3.print_status()
#   Use docstrings to describe classes/functions
#   Should come right below the declaration
#   Use __doc__ to access the docstring of class/function
#   help() is used to view all docstrings of an object
#   print(Plant.print_status.__doc__)
