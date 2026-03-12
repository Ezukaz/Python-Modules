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
        """Print plant status"""
        print(f"{self.plant}: {self.height}cm, {self.age} days old")


class Growth:
    """Make a growth instance, update growth stats, and print the growth"""
    def __init__(self, start: int = 1, end: int = 7) -> None:
        self.start = start
        self.end = end
        self.passed: int = 0
        for i in range(start, end):
            self.passed += 1

    def age(self, plant: Plant) -> None:  # If Plant not defined then 'Plant'
        """"Add value to height & age to express time"""
        plant.height += self.passed
        plant.age += self.passed

    def print_grow(self) -> None:
        """Print growth stat"""
        print(f"Growth this week: +{self.passed}cm")


if __name__ == "__main__":
    plant = Plant()
    week = Growth()
    print(f"=== Day {week.start} ===")
    plant.print_status()
    print(f"=== Day {week.end} ===")
    week.age(plant)
    plant.print_status()
    week.print_grow()
