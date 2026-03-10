#!/usr/bin/env python3

class Plant:
    def __init__(self, plant="Rose", height=25, age=30):
        self.plant = plant
        self.height = height
        self.age = age

    def print_status(self):
        print(f"{self.plant}: {self.height}cm, {self.age} days old")


class Growth:
    def __init__(self, start=1, end=7):
        self.start = start
        self.end = end
        self.passed = 0
        for i in range(start, end):
            self.passed += 1

    def age(self, plant):
        plant.height += self.passed
        plant.age += self.passed

    def print_grow(self):
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
