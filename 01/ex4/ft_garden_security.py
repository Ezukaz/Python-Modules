#!/usr/bin/env python3

class Plant:
    def __init__(self, plant="Rose", height=25, age=30):
        self.plant = plant
        self.__height = height
        self.__age = age

    def print_status(self):
        print(
            f"Current plant: {self.plant} "
            f"({self.__height}cm, {self.__age} days)"
        )


class SecurePlant(Plant):
    @staticmethod
    def print_err(err_type, val, unit):
        print(
            "Invalid operation attempted: "
            f"{err_type} {val}{unit} [REJECTED]"
        )
        print(f"Security: Negative {err_type} rejected")
        print()

    def print_success(self):
        print(f"Plant created: {self.plant}")
        print(f"Height updated: {self.get_height()}cm [OK]")
        print(f"Age updated: {self.get_age()} days [OK]")
        print()

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def set_height_age(self, height, age):
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
    secure_ok = SecurePlant.set_height_age(plant, 25, 30)
    if secure_ok:
        SecurePlant.print_success(plant)
    secure_ok = SecurePlant.set_height_age(plant, -5, 75)
    if secure_ok:
        SecurePlant.print_success(plant)
    plant.print_status()
