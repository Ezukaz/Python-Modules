#!/usr/bin/env python3

class my_status:
    def __init__(self, plant="Rose", height=25, age=30):
        self.plant = plant
        self.height = height
        self.age = age

    def print_status(self):
        print("Plant: ", self.plant)
        print(f"Height: {self.height}cm")
        print(f"Age: {self.age} days\n")

if __name__ == "__main__":
    print("=== Welcome to My Garden ===")
    plant1 = my_status()
    plant1.print_status()
    print("=== End of Program ===")
