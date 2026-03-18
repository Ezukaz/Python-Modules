#!/usr/bin/env python3

# Use pass for empty classes. There is purpose in the name of empty classes
# In this case we are inheriting everything from Exception class and not adding
# anything to it. We want to differenciate the error type by giving it a name
class GardenError(Exception):
    """ Base exception for all garden-related problems """
    pass


class PlantError(GardenError):
    """ Exception for plant-specific problems """
    pass


class WaterError(GardenError):
    """ Exception for watering system problems """
    pass


def check_plant_status(plant: str = "tomato") -> None:
    """ Check plant and raise PlantError if wilting """
    if plant == "tomato":
        raise PlantError(f"The {plant} plant is wilting!")
    # 'raise' is specifically for classes that inherit from BaseException.
    # It creates an instance of an exception class and throws it.
    # Raising a class without calling it possible but is more common to call it
    # with a message


def check_water_tank(water_level: int = 0) -> None:
    """ Check water tank and raise WaterError if empty """
    if water_level < 1:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors(inputs: list[str] = ["corn", "bean", "tomato"]) -> None:
    print("=== Custom Garden Errors Demo ===")
    print()

    # Plant test
    print("Testing PlantError...")
    empty_input = 0
    for input in inputs:
        try:
            check_plant_status(input)
            if input != "":
                print(f"Plant {input} looks healthy")
            else:
                empty_input += 1
        except PlantError as e:
            print(f"Caught PlantError: {e}")
            has_error = True
    if empty_input == 3:
        print("No plants?!")
    print()

    # Water test
    print("Testing WaterError...")
    water_level = 0
    try:
        check_water_tank(water_level)
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    else:
        print("Water is working wonderfully!")
    print()

    # Garden test
    print("Testing catching all garden errors...")
    has_error = False
    for input in inputs:
        try:
            check_plant_status(input)
        except PlantError as e:
            print(f"Caught PlantError: {e}")
            has_error = True
    try:
        check_water_tank(water_level)
    except WaterError as e:
        print(f"Caught WaterError: {e}")
        has_error = True
    try:
        if empty_input == 3:
            raise GardenError("There are no plants in garden!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        has_error = True
    if not has_error:
        print("Garden is beautiful!")
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    plants = [input(), input(), input()]
    test_custom_errors(plants)
