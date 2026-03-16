#!/usr/bin/env python3
"""Exercise 2: Position Tracker - 3D coordinate system with tuples"""

import math
from typing import Tuple


def calculate_distance(
    p1: Tuple[float, float, float],
    p2: Tuple[float, float, float]
) -> float:
    """Calculate 3D Euclidean distance between two points."""
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    dz = p2[2] - p1[2]
    return math.sqrt(dx*dx + dy*dy + dz*dz)


def parse_coordinates(coord_str: str) -> Tuple[int, int, int]:
    """Parse 'x,y,z' string into 3D coordinate tuple."""
    coords = coord_str.split(',')
    if len(coords) != 3:
        raise ValueError("Invalid format - expected 'x,y,z'")
    try:
        return tuple(int(c.strip()) for c in coords)
    except ValueError as e:
        raise ValueError(str(e))


def demonstrate_coordinates() -> None:
    """Demonstrate 3D coordinates and tuple operations."""
    print("=== Game Coordinate System ===")
    # Create position
    pos = (10, 20, 5)
    print(f"Position created: {pos}")
    # Distance calculation
    origin = (0, 0, 0)
    dist = calculate_distance(origin, pos)
    print(f"Distance between (0, 0, 0) and (10, 20, 5): {dist:.2f}")
    # Parsing
    print('Parsing coordinates: "3,4,0"')
    try:
        parsed = parse_coordinates("3,4,0")
        print(f"Parsed position: {parsed}")
        print(
            f"Distance between (0, 0, 0) and {parsed}: "
            f"{calculate_distance(origin, parsed):.1f}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
    print('Parsing invalid coordinates: "abc,def,ghi"')
    try:
        parse_coordinates("abc,def,ghi")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
    # Unpacking
    print("Unpacking demonstration:")
    x, y, z = parsed
    print(f"Player at x={x}, y={y}, z={z}")
    print("Coordinates: X={}, Y={}, Z={}".format(x, y, z))


if __name__ == "__main__":
    demonstrate_coordinates()
