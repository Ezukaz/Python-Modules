#!/usr/bin/env python3

def garden_operations() -> None:
    """ Garden operations with validation """

    try:
        int("abc")
        print()
        print("Testing ValueError...")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    else:
        print("Passed")

    try:
        10/0
        print()
        print("Testing ZeroDivisionError...")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    else:
        print("Passed")

    f = None
    try:
        f = open("missing.txt", "r")
        print()
        print("Testing FileNotFoundError...")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    else:
        print("Passed")
    finally:
        if f:
            f.close()

    try:
        garden = {"owner": "Alice"}
        print(garden["types"])
        print()
        print("Testing KeyError...")
    except KeyError as e:
        print(f"Caught KeyError: {e}")
    else:
        print("Passed")

    try:
        int("avc"/0)
        print()
        print("Testing multiple errors together...")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Caught an error, {e}, but program continues!")
    else:
        print("Passed")


def test_error_types() -> None:
    """ Check different Python error types with garden_operations() """
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
