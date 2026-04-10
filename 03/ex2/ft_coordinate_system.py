#!/usr/bin/env python3

import math
import sys


def calculate_distance(
    p1: tuple[float, float, float],
    p2: tuple[float, float, float]
) -> float:
    """Calculate 3D Euclidean distance between two points."""
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    dz = p2[2] - p1[2]
    return math.sqrt(dx*dx + dy*dy + dz*dz)


def parse_coordinates(coord_str: str) -> tuple[int, int, int]:
    """Parse 'x,y,z' string into 3D coordinate tuple."""
    coords = coord_str.split(',')
    if len(coords) != 3:
        raise ValueError("Invalid format - expected 'x,y,z'")
    return tuple(int(c) for c in coords)


def demonstrate_coordinates(args: list[str]) -> None:
    """Demonstrate 3D coordinates and tuple operations."""
    print("=== Game Coordinate System ===")
    print()

    # Create position
    pos = (10, 20, 5)
    print(f"Position created: {pos}")
    # Distance calculation
    origin = (0, 0, 0)
    dist = calculate_distance(origin, pos)
    print(f"Distance between {origin} and {pos}: {dist:.2f}")
    print()

    # Parsing
    argc = len(args)
    if argc > 1:
        parsed = None
        for arg in args[1:]:
            try:
                print(f'Parsing coordinates: "{arg}"')
                parsed = parse_coordinates(arg)
                print(f"Parsed position: {parsed}")
                print(
                    f"Distance between {origin} and {parsed}: "
                    f"{calculate_distance(origin, parsed):.1f}")
            except ValueError as e:
                print(f"Parsing invalid coordinates: {arg}")
                print(f"Error parsing coordinates: {e}")
                print(
                    f"Error details - Type: {e.__class__.__name__}, "
                    f"Args: {e.args}"
                    )
            print()

        # Unpacking
        if parsed:
            print("Unpacking demonstration:")
            x, y, z = parsed
            print(f"Player at x={x}, y={y}, z={z}")
            print(f"Coordinates: X={x}, Y={y}, Z={z}")
    print(f"You have input {argc - 1} argument{'s' if argc - 1 != 1 else ''}")


if __name__ == "__main__":
    demonstrate_coordinates(sys.argv)
