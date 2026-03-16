#!/usr/bin/env python3

def garden_operations() -> None:
    """ Garden operation that test errors """

    try:
        print()
        print("Testing ValueError...")
        int("0")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    else:
        print("Passed")

    try:
        print()
        print("Testing ZeroDivisionError...")
        10/1
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    else:
        print("Passed")

    # f is assigned None because finally will always execute. If f wasn't
    # assigned then it will crash when f is accessed.
    f = None
    try:
        print()
        print("Testing FileNotFoundError...")
        f = open("missing.txt", "r")
        # "r" for read, "w" for write, "a" for append, and "x" for exclusive
        # create. "x" will throw an error if there already exist that file.
        # Use it for files that you don't want to overwrite. The flags are for
        # permissions for that file that you open. If no flag is given then
        # it defaults to "r" which is a read-only permission.
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    else:
        print("Passed")
    finally:
        # finally can be replaced with the "with" command. It automatically
        # closes files that are opened. It is used for any object that has an
        # __enter__ & __exit__. If you use with there is no need for the
        # f = None guard as it never __enter__
        if f:
            f.close()  # we can .close as most things are objects in python.
            # open() makes an object that has methods. close() is one of them.
            # A close() function does not exist in python but the method does

    garden = {"owner": "Alice"}
    try:
        print()
        print("Testing KeyError...")
        print(garden["owner"])
    except KeyError as e:
        print(f"Caught KeyError: {e}")
    else:
        print("Passed")

    try:
        print()
        print("Testing multiple errors together...")
        # 10/0
        # int("avc")
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
