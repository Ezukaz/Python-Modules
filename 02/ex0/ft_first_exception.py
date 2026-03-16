#!/usr/bin/env python3
# from typing import Union  # This is needed for Union[float, None]
# Not needed in current version

def check_temperature(temp_str: str) -> int | None:  # Union[float, None]
    """Check if temperature string is valid and within safe range (0-40°C)."""
    try:
        temp = int(temp_str)
        if temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
            return None
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
            return None
        return temp
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None


def test_temperature_input() -> None:
    """Check temperature validation with good/bad inputs"""
    print("=== Garden Temperature Checker ===")
    print()
    # Good input
    print("Testing temperature: 25")
    result = check_temperature("25")
    if result is not None:
        print(f"Temperature {result}°C is perfect for plants!")
    print()
    # Bad input (not a number)
    print("Testing temperature: abc")
    check_temperature("abc")
    print()
    # Extreme values
    print("Testing temperature: 100")
    check_temperature("100")
    print()
    print("Testing temperature: -50")
    check_temperature("-50")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
