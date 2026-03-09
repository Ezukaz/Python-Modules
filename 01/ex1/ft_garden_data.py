#!/usr/bin/env python3

class my_status:
    def __init__(self, plant="Rose", height=25, age=30):
        self.plant = plant
        self.height = height
        self.age = age

    def print_status(self):
        print(f"{self.plant}: {self.height}cm, {self.age} days old")

if __name__ == "__main__":
    plant1 = my_status()
    plant2 = my_status("Sunflower", 80, 45)
    plant3 = my_status("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    plant1.print_status()
    plant2.print_status()
    plant3.print_status()
