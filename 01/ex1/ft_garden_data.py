#!/usr/bin/env python3

class Plant:
    def __init__(self, plant="Rose", height=25, age=30):
        self.plant = plant
        self.height = height
        self.age = age

    def print_status(self):
        print(f"{self.plant}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    plant1 = Plant()
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    plant1.print_status()
    plant2.print_status()
    plant3.print_status()
