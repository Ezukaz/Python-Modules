#!/usr/bin/env python3

from ex1.ft_garden_data import my_status

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
    plant = my_status()
    week = Growth()
    print(f"=== Day {week.start} ===")
    plant.print_status()
    print(f"=== Day {week.end} ===")
    week.age(plant)
    plant.print_status()
    week.print_grow()

