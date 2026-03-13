#!/usr/bin/env python3

class Garden:
    def __init__(
        self,
        total_growth: int = 0,
        owner: str = "Noname",
        is_valid_height: bool = True,
    ) -> None:
        self._plants = {
            "regular": [None] * 10,
            "bloom": [None] * 10,
            "prize": [None] * 10
        }
        self._counts = {
            "regular": 0,
            "bloom": 0,
            "prize": 0
        }
        self._total_growth = total_growth
        self.owner = owner
        self._is_valid_height = is_valid_height

    def add_plant(self, plant: 'Plant', category: str) -> bool:
        self._is_valid_height = GardenManager.is_height(plant._height)
        if self._is_valid_height:
            self._plants[category][self._counts[category]] = plant
            self._counts[category] += 1
            print(f"Added {plant.name} to {self.owner}'s garden")
        else:
            print("Could not add null height plant")
        return self._is_valid_height

    def grow_all(self) -> None:
        print()
        print(f"{self.owner} is helping all plants to grow...")
        has_plant = 0
        for category in ["regular", "bloom", "prize"]:
            for plant in range(self._counts[category]):
                self._plants[category][plant].grow()
                self._plants[category][plant].print_growth()
                self._total_growth += 1
                has_plant = 1
        if not has_plant:
            print("but not today (T_T)")

    def print_report(self) -> None:
        total_score = (
            self._counts['regular'] +
            self._counts['bloom'] +
            self._counts['prize']
        )
        print()
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for category in ["regular", "bloom", "prize"]:
            for j in range(self._counts[category]):
                self._plants[category][j].print_status()
        print()
        print(
            f"Plants added: {total_score}, "
            f"Total growth: {self._total_growth}cm"
        )
        print(
            f"Plant types: {self._counts['regular']} regular, "
            f"{self._counts['bloom']} flowering, "
            f"{self._counts['prize']} prize flowers"
        )


class GardenManager:
    def __init__(self):
        self._gardens = [None] * 5
        self._garden_count = 0
        self._all_height_valid = True

    class GardenStats:
        @staticmethod
        def calc_score(garden: 'Garden') -> int:
            score = 0

            for category in ["regular", "bloom", "prize"]:
                for i in range(garden._counts[category]):
                    plant = garden._plants[category][i]
                    score += plant.get_height() + plant.prize_pts

            score += 10 * garden._total_growth
            return score

        @staticmethod
        def print_total_stats(manager: 'GardenManager'):
            score_str = ""
            total_sum = 0

            for i in range(manager._garden_count):
                garden = manager._gardens[i]
                garden_score = GardenManager.GardenStats.calc_score(garden)
                # Use library for calling methods that don't need instances
                # It tells that this rule is universal, a utility
                total_sum += garden_score

                if i != 0:
                    score_str += ", "
                score_str += f"{garden.owner}: {garden_score}"

            print()
            print(f"Height validation test: {manager._all_height_valid}")
            print(f"Garden scores - {score_str}")
            print(f"Total network score: {total_sum}")
            print(f"Total gardens managed: {manager._garden_count}")

    def add_garden(self, garden: Garden) -> None:
        idx = self._garden_count
        self._gardens[idx] = garden
        self._garden_count += 1

    @classmethod
    def create_garden_network(cls) -> 'GardenManager':
        manager = cls()

        alice_garden = Garden(owner="Alice")
        bob_garden = Garden(owner="Bob")
        manager.add_garden(alice_garden)
        manager.add_garden(bob_garden)

        oak = Plant()
        rose = FloweringPlant()
        sunflower = PrizeFlower()

        manager._all_height_valid &= alice_garden.add_plant(oak, "regular")
        manager._all_height_valid &= alice_garden.add_plant(rose, "bloom")
        manager._all_height_valid &= alice_garden.add_plant(sunflower, "prize")

        pine = Plant("Pine tree", 130)
        tulip = FloweringPlant("Tulip", 20, "pink", "not blooming")
        sakura = PrizeFlower("Sakura", 800, "dark pink", "half blooming", 50)

        manager._all_height_valid &= bob_garden.add_plant(pine, "regular")
        manager._all_height_valid &= bob_garden.add_plant(tulip, "bloom")
        manager._all_height_valid &= bob_garden.add_plant(sakura, "prize")

        return manager

    @staticmethod
    def is_height(height: int) -> bool:
        if height > 0:
            return True
        return False


class Plant:
    def __init__(self, name: str = "Oak tree", height: int = 100) -> None:
        self.name = name
        self._height = height
        self.prize_pts = 0

    def get_info(self) -> str:
        return f"- {self.name}: {self._height}cm"

    def get_height(self) -> int:
        return self._height

    def print_status(self) -> None:
        print(self.get_info())

    def grow(self) -> None:
        self._height += 1

    def print_growth(self) -> None:
        print(f"{self.name} grew 1cm")


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

    def get_prize_pts(self) -> int:
        return self.prize_pts

    def get_info(self) -> str:
        return f"{super().get_info()}, Prize points: {self.prize_pts}"


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print()
    network = GardenManager.create_garden_network()
    for i in range(network._garden_count):
        network._gardens[i].grow_all()
        network._gardens[i].print_report()
    network.GardenStats.print_total_stats(network)
