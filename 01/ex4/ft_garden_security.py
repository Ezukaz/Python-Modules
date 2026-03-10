#!/usr/bin/env python3

class Plant:
    def __init__(self, plant="Rose", height=25, age=30):
        self.plant = plant
        self.__height = height
        self.__age = age

    def print_status(self):
        print(f"Current plant: {self.plant} ({self.height}cm, {self.age} days)")


class SecurePlant(Plant, age, height):
    def print_err(err_type, val, unit):
        print(f"Invalid operation attempted: {err_type} {val}{unit} [REJECTED]")
        print(f"Negative {err_type} rejected")
        print()

    def print_success(Plant):
        print(f"Plant created: {Plant.plant}")
        print(f"Height updated: {Plant.height}cm [Ok]")
        print(f"Age updated: {Plant.age} days [OK]")
        print()

    def get_height(Plant):
        return Plant.__height

    def get_age(Plant):
        return Plant.__age

    def set_height(Plant, height):
        if height < 0:
            print_err("height", height, "cm")
        else:
            Plant.__height = height
            height_success = 1

    def set_age(Plant, age):
        if age < 0:
            print_err("age", age, " days")
        else:
            Plant.__age = age
            age_success = 1


if __name__ == "__main__":
    plant = Plant()
    height = Plant.get_height()
    age = Plant.get_age()
    print("=== Garden Security System ===")
