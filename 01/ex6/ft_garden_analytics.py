#!/usr/bin/env python3

class GardenManager:
    class GardenStats:
        def calc_stats():

    def __init__():

    def work_on_instance():

    @classmethod
    def create_garden_network():

    @staticmethod
    def utils():


class Plant:
    def __init__(self, plant="Oak tree", height=100):
        self.plant = plant
        self.height = height
        print(f"Added {self.plant} to Alice's garden")

    def get_info():
        return f"- {self.plant}: {self.height}cm"

    def print_status(self):
        print(self.get_info())

    def print_growth():
        print(f"{self.plant} grew {}cm")


class FloweringPlant(Plant):
    def __init__(
        self, plant="Rose", height=25, color="red", state="blooming"
    ):
        super().__init__(plant, height):
        self.color = color
        self.state = state

    def get_info(self):
        return f"{super().get_info()}, {self.color} flowers ({self.state})"


class PrizeFlower(FloweringPlant):
    def __init__(
        self, plant="Sunflower", height=50,
        color="yellow", state="blooming", prize_pts=10
    ):
        super().__init__(plant, height, color, state, prize_pts)
        self.prize_pts = prize_pts

    def get_info(self):
        return f"{super().get_info()}, Prize points: {self.prize_pts}"
    

if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print()

    print()
    print("Alice is helping all plants grow...")
    print()
    print("=== Alice's Garden Report ===")
    print("Plants in garden:")