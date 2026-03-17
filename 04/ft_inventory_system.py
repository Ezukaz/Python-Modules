#!/usr/bin/env python3
"""Exercise 4: Inventory Master - Dictionary-based inventory system"""

import sys
from typing import Dict, List


def analyze_inventory(inventory_args: List[str]) -> None:
    """Analyze game inventory using dictionaries"""
    print("=== Inventory System Analysis ===")

    inventory: Dict[str, int] = {}
    for arg in inventory_args[1:]:
        try:
            item, qty = arg.split(':')
            inventory[item] = int(qty)
        except (ValueError, KeyError):
            print(f"Invalid item '{arg}' - skipping")
            continue

    if not inventory:
        print("No valid inventory items found.")
        return

    total_items = sum(inventory.values())
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")

    print("\n=== Current Inventory ===")
    sorted_items = sorted(inventory.items(), key=lambda x: x[1], reverse=True)
    for item, qty in sorted_items:
        percentage = (qty / total_items) * 100
        print(f"{item}: {qty} units ({percentage:.1f}%)")

    print("\n=== Inventory Statistics ===")
    most_abundant = max(inventory, key=inventory.get)
    least_abundant = min(inventory, key=inventory.get)
    print(f"Most abundant: {most_abundant} ({inventory[most_abundant]} units)")
    print(
        f"Least abundant: {least_abundant} ({inventory[least_abundant]}"
        f"unit{'s' if inventory[least_abundant] > 1 else ''})"
    )

    print("\n=== Item Categories ===")
    moderate = {k: v for k, v in inventory.items() if v >= 5}
    scarce = {k: v for k, v in inventory.items() if v < 5}
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

    print("\n=== Management Suggestions ===")
    restock = [item for item, qty in inventory.items() if qty <= 1]
    if restock:
        print(f"Restock needed: {', '.join(restock)}")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {', '.join(inventory.keys())}")
    print(f"Dictionary values: {', '.join(map(str, inventory.values()))}")
    print(f"Sample lookup - '{most_abundant}' in inventory: True")


if __name__ == "__main__":
    analyze_inventory(sys.argv)
