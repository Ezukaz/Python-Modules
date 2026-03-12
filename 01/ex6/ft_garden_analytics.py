#!/usr/bin/env python3

class Garden:
    def __init__(
        self,
        plants: list = None,  # Never use mutatable default in parameter
        counts: list = None,
        total_growth: int = 0,
        owner: str = "Noname",
        is_valid_height: bool = True,
    ) -> None:
        self._plants = [[], [], []]
        self._counts = [0, 0, 0]
        self.total_growth = total_growth
        self.owner = owner
        self._is_valid_height = is_valid_height

    def add_plant(self, plant: Plant, type_index: int) -> None:
        self._is_valid_height = GardenManager.is_height(plant._height)
        if self._is_valid_height:
            self._plants[type_index][self._counts[type_index]] = plant
            self._counts[type_index] += 1
            print(f"Added {plant.name} to {self.owner}'s garden")
        else:
            print("Could not add null height plant")

    def grow_all(self) -> None:
        print()
        print(f"{self.owner} is helping all plants to grow...")
        has_plant = 0
        for i in range(3):
            for j in range(self._counts[i]):
                print(f"{self._plants[i][j].name} grew 1cm")
                self._plants[i][j]._height += 1
                self.total_growth += 1
                has_plant = 1
        if not has_plant:
            print("but not today (T_T)")

    def print_report(self) -> None:
        print()
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for i in range(3):
            for j in range(self._counts[i]):
                self._plants[i][j].print_status()
        print()
        print(
            "Plants added: "
            f"{self._counts[0] + self._counts[1] + self._counts[2]}, "
            f"Total growth: {self.total_growth}cm"
        )
        print(
            f"Plant types: {self._counts[0]} regular, "
            f"{self._counts[1]} flowering, "
            f"{self._counts[2]} prize flowers"
        )


class GardenManager:
    __garden_count = 0

    def __init__():

    class GardenStats:
        def calc_stats():

    def work_on_instance():

    @classmethod
    def create_garden_network():

    def some_print():
        print()
        print(f"Height validation test: {self._is_valid_height}")
        print(f"Garden scores - {}")
        print(f"Total gardens managed: {}")

    @staticmethod
    def is_height(height: int) -> bool:
        if height > 0:
            return True
        return False


class Plant:
    def __init__(self, name: str = "Oak tree", height: int = 100) -> None:
        self.name = name
        self._height = height

    def get_info(self) -> str:
        return f"- {self.name}: {self._height}cm"

    def print_status(self) -> None:
        print(self.get_info())

    def print_growth(self) -> None:
        print(f"{self.name} grew {}cm")  # Don't forget to fill missing value


class FloweringPlant(Plant):
    def __init__(
        self,
        name: str = "Rose",
        height: int = 25,
        color: str = "red",
        state: str = "blooming"
    ) -> None:
        super().__init__(name, height)
        self.color = color
        self.state = state

    def get_info(self) -> str:
        return f"{super().get_info()}, {self.color} flowers ({self.state})"


class PrizeFlower(FloweringPlant):
    def __init__(
        self,
        name: str = "Sunflower",
        height: int = 50,
        color: str = "yellow",
        state: str = "blooming",
        prize_pts: int = 10
    ) -> None:
        super().__init__(name, height, color, state)
        self.prize_pts = prize_pts

    def get_info(self) -> str:
        return f"{super().get_info()}, Prize points: {self.prize_pts}"
    

if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print()

    print()
    print("Alice is helping all plants grow...")
    print()
    print("=== Alice's Garden Report ===")
    print("Plants in garden:")