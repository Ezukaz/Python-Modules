#!/usr/bin/env python3

class Plant:
    def __init__(self, plant="Rose", height=25, age=30):
        self.plant = plant
        self.height = height
        self.age = age

    def print_status(self):
        print(f"Created: {self.plant} ({self.height}cm, {self.age} days)")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    total = 0
    for i in range(5):
        if i == 0:
            plant = Plant("Rose", 25, 30)
        if i == 1:
            plant = Plant("Oak", 200, 365)
        if i == 2:
            plant = Plant("Cactus", 5, 90)
        if i == 3:
            plant = Plant("Sunflower", 80, 45)
        if i == 4:
            plant = Plant("Fern", 15, 120)
        plant.print_status()
        total += 1
    print(f"\nTotal plants created: {total}")
