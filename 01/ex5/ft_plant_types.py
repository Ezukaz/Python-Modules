#!/usr/bin/env python3

class Plant:
    """Make plant instance and print status"""
    def __init__(
        self,
        plant: str = "Rose",
        height: int = 25,
        age: int = 30
    ) -> None:
        """Initialize plant with name, height (cm), and age (days)"""
        self.plant = plant
        self.height = height
        self.age = age

    def get_produce(self) -> str:
        """Gets the correct output string for each plant type"""
        return ""  # This is for polymorphism. For the case of no type given

    def get_produce_action(self) -> str:
        """Flower object's specific action"""
        return ""

    def print_status(self) -> None:
        """Print plant status"""
        print()
        print(
            f"{self.plant} ({self.__class__.__name__}): "
            # Class's name attribute as a str ↑↑↑
            f"{self.height}cm, {self.age} days, {self.get_produce()}"
        )
        print(f"{self.get_produce_action()}")


class Flower(Plant):
    """Make flower type instance and print action"""
    def __init__(
        self,
        plant: str = "Rose",
        height: int = 25,
        age: int = 30,
        color: str = "white"
    ) -> None:
        """Initialize flower with name, height (cm), age (days), and color"""
        super().__init__(plant, height, age)
        self.color = color

    def get_produce(self) -> str:
        """Polymorphism of get_produce() of parent"""
        return f"{self.color} color"

    def get_produce_action(self) -> str:
        """Flower object's specific action"""
        return f"{self.plant} is blooming beautifully!"


class Tree(Plant):
    """Make tree type instance and print action"""
    def __init__(
        self,
        plant: str = "Oak",
        height: int = 500,
        age: int = 1825,
        trunk_diameter: int = 50
    ) -> None:
        """Initialize tree with name, height (cm), age (days), and diameter"""
        super().__init__(plant, height, age)
        self.trunk_diameter = trunk_diameter

    def get_produce(self) -> str:
        """Polymorphism of get_produce() of parent"""
        return f"{self.trunk_diameter}cm diameter"

    def get_produce_action(self) -> str:
        """Tree object's specific action"""
        return (f"{self.plant} provides {self.trunk_diameter * 1.56}"
                " square meters of shade")


class Vegetable(Plant):
    """Make vegetable type instance and print action"""
    def __init__(
        self,
        plant: str = "Tomato",
        height: int = 80,
        age: int = 90,
        harvest_season: str = "summer",
        nutritional_value: str = "vitamin C"
    ) -> None:
        """Init vegetable with name, height, age, season and nutrition"""
        super().__init__(plant, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_produce(self) -> str:
        """Polymorphism of get_produce() of parent"""
        return f"{self.harvest_season} harvest"

    def get_produce_action(self) -> str:
        """Vegetable object's specific action"""
        return f"{self.plant} is rich in {self.nutritional_value}"


if __name__ == "__main__":
    plant1 = Flower()
    plant2 = Tree()
    plant3 = Vegetable()
    plant4 = Flower("Tulip", 20, 20, "pink")
    plant5 = Tree("Pine", 400, 1476, 20)
    plant6 = Vegetable("Spinach", 30, 45, "autumn", "magnesium")
    plants = [plant1, plant2, plant3, plant4, plant5, plant6]
    print("=== Garden Plant Types ===")
    for plant in plants:
        plant.print_status()
