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
        self.__height = height
        self.__age = age

    def print_status(self) -> None:
        """Print plant status"""
        print(
            f"Current plant: {self.plant} "
            f"({self.__height}cm, {self.__age} days)"
        )


class SecurePlant(Plant):
    """Secures plant stats by encapsulating/validating height & age."""
    @staticmethod
    def print_err(err_type: str, val: int, unit: int) -> None:
        """Print validation error message"""
        print(
            "Invalid operation attempted: "
            f"{err_type} {val}{unit} [REJECTED]"
        )
        print(f"Security: Negative {err_type} rejected")
        print()

    def print_success(self) -> None:
        """Print validation success message"""
        print(f"Plant created: {self.plant}")
        print(f"Height updated: {SecurePlant.get_height(self)}cm [OK]")
        print(f"Age updated: {SecurePlant.get_age(self)} days [OK]")
        print()

    def get_height(self) -> None:
        """Get encapsulated height attribute"""
        return self.__height

    def get_age(self) -> None:
        """Get encapsulated age attribute"""
        return self.__age

    def set_height_age(self, height: int, age: int) -> bool:
        if height < 0 or age < 0:
            if height < 0:
                SecurePlant.print_err("height", height, "cm")
            if age < 0:
                SecurePlant.print_err("age", age, " days")
            return False
        self.__height = height
        self.__age = age
        return True


if __name__ == "__main__":
    plant = Plant()
    print("=== Garden Security System ===")
    secure_ok = SecurePlant.set_height_age(plant, -25, 30)
    if secure_ok:
        SecurePlant.print_success(plant)
    secure_ok = SecurePlant.set_height_age(plant, -5, -75)
    if secure_ok:
        SecurePlant.print_success(plant)
    plant.print_status()
