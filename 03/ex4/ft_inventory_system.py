#!/usr/bin/env python3

import sys
from typing import Dict, List


class NoItemError(BaseException):
    pass


def analyze_inventory(arg_inputs: List[str]) -> None:
    """ Check and print all analytics from a list """
    inventory: Dict[str, int] = {}
    for arg in arg_inputs[1:]:
        try:
            item, qty = arg.split(':')
            conv_str = int(qty)
            inventory[item] = conv_str
            if conv_str < 1:
                raise NoItemError()
        except (KeyError, ValueError, NoItemError):
            print(f"Invalid item {arg} - skipping")

    if not inventory:
        print("No valid items were found")
        return

    sorted_items = sorted(inventory.items(), key=lambda x: x[1], reverse=True)
    total_items = sum(inventory.values())
    types = len(inventory)
    max_item = [max(inventory, key=inventory.get), max(inventory.values())]
    min_item = [min(inventory, key=inventory.get), min(inventory.values())]
    qty_categories = {}
    for name, condition in [
        ('abundant', lambda v: v > 10),
        ('moderate', lambda v: 5 <= v <= 10),
        ('scarce', lambda v: v < 5)
    ]:
        items = {k: v for k, v in inventory.items() if condition(v)}
        if items:
            qty_categories[name] = items
    restock = {k: v for k, v in inventory.items() if v < 2}

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {types}")
    print()

    print("=== Current Inventory ===")
    for k, v in sorted_items:
        print(
            f"{k}: {v} {'units' if v > 1 else 'unit'} "
            f"({(v / total_items) * 100:.1f}%)"
        )
    print()

    print("=== Inventory Statisitcs ===")
    print(
        f"Most abundant: {max_item[0]} ({max_item[1]} "
        f"{'units' if max_item[1] > 1 else 'unit'})"
    )
    print(
        f"Least abundant: {min_item[0]} ({min_item[1]} "
        f"{'units' if min_item[1] > 1 else 'unit'})"
    )
    print()

    print("=== Item Categories ===")
    for category in qty_categories:
        print(f"{category}: {qty_categories[category]}")
    print()

    print("=== Management Suggestions ===")
    print(f"Restock needed: {', '.join(restock)}")
    print()

    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {', '.join(list(inventory.keys()))}")
    print(f"Dictionary : {', '.join(map(str, list(inventory.values())))}")
    print(
        "Sample lookup - 'sword' in inventory: "
        f"{bool(inventory.get('sword', 0))}"
    )


if __name__ == "__main__":
    analyze_inventory(sys.argv)
