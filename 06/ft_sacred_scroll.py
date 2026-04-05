#!/usr/bin/env python3

import alchemy


print("\n=== Sacred Scroll Mastery ===")
print("\nTesting direct module access:")
print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
print(f"alchemy.elements.create_water(): {alchemy.elements.create_water()}")
print(f"alchemy.elements.create_earth(): {alchemy.elements.create_earth()}")
print(f"alchemy.elements.create_air(): {alchemy.elements.create_air()}")
print("\nTesting package-level access (controlled by __init__.py):")
print(f"alchemy.create-fire(): {alchemy.create_fire()}")
print(f"alchemy.create_water(): {alchemy.create_water()}")
print("alchemy.create_earth():", end=" ")
try:
    print(f"{alchemy.create_earth()}")
except AttributeError:
    print("AttributeError - not exposed")
print("alchemy.create_air():", end=" ")
try:
    print(f"{alchemy.create_air()}")
except AttributeError:
    print("AttributeError - not exposed")
print("\nPackage metadata:")
print(f"Version: {alchemy.__version__}")
print(f"Author: {alchemy.__author__}")
