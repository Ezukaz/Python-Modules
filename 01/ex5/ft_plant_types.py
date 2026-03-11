#!/usr/bin/env python3

class Plant:
    def __init__(self, plant="Rose", height=25, age=30):
        self.plant = plant
        self.height = height
        self.age = age

    def get_produce(self):
        return ""

    def print_status(self):
        print()
        print(
            f"{self.plant} ({self.__class__.__name__}): "
            f"{self.height}cm, {self.age} days, {self.get_produce()}"
        )


class Flower(Plant):
    def __init__(self, plant="Rose", height=25, age=30, color="white"):
        super().__init__(plant, height, age)
        self.color = color

    def get_produce(self):
        return f"{self.color} color"

    def bloom(self):
        print(f"{self.plant} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, plant="Oak", height=500, age=1825, trunk_diameter=50):
        super().__init__(plant, height, age)
        self.trunk_diameter = trunk_diameter

    def get_produce(self):
        return f"{self.trunk_diameter}cm diameter"

    def produce_shade(self):
        print(
            f"{self.plant} provides {self.trunk_diameter * 1.56}"
            " square meters of shade"
        )


class Vegetable(Plant):
    def __init__(
        self, plant="Tomato", height=80, age=90,
        harvest_season="summer", nutritional_value="vitamin C"
    ):
        super().__init__(plant, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_produce(self):
        return f"{self.harvest_season} harvest"

    def nutrition(self):
        print(f"{self.plant} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    plant1 = Flower()
    plant2 = Tree()
    plant3 = Vegetable()
    print("=== Garden Plant Types ===")
    plant1.print_status()
    plant1.bloom()
    plant2.print_status()
    plant2.produce_shade()
    plant3.print_status()
    plant3.nutrition()
    plant4 = Flower("Tulip", 20, 20, "pink")
    plant5 = Tree("Pine", 400, 1476, 20)
    plant6 = Vegetable("Spinach", 30, 45, "autumn", "magnesium")
    plant4.print_status()
    plant4.bloom()
    plant5.print_status()
    plant5.produce_shade()
    plant6.print_status()
    plant6.nutrition()
