#!/usr/bin/env python3

def check_plant_health(
        plant_name: str,
        water_level: int,
        sunlight_hours: int
) -> str:
    """ Validate plant health parameters and raise errors if invalid """
    if not plant_name or plant_name == "":
        raise ValueError("Plant name cannot be empty!")

    if water_level < 1 or water_level > 10:
        raise ValueError(
            f"Water level {water_level} "
            f"is too {'high' if water_level > 10 else 'low'} (max 10)"
        )

    if sunlight_hours < 2 or sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} "
            f"is too {'low' if sunlight_hours < 2 else 'high'} (min 2)"
        )

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    """ Test all plant health validation scenarios """
    print("=== Garden Plant Health Checker ===")
    print()

    # Good values
    print("Testing good values...")
    try:
        result = check_plant_health("tomato", 5, 8)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    print()

    # Bad plant name
    print("Testing empty plant name...")
    try:
        check_plant_health("", 5, 8)
    except ValueError as e:
        print(f"Error: {e}")
    print()

    # Bad water level
    print("Testing bad water level...")
    try:
        check_plant_health("lettuce", 15, 8)
    except ValueError as e:
        print(f"Error: {e}")
    print()

    # Bad sunlight hours
    print("Testing bad sunlight hours...")
    try:
        check_plant_health("carrots", 5, 0)
    except ValueError as e:
        print(f"Error: {e}")
    print()

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
