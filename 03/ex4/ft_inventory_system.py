#!/usr/bin/env python3

import sys


class NoItemError(BaseException):
    pass


def plural(v: int) -> str:
    return "s" if v != 1 else ""


def analyze_inventory(arg_inputs: list[str]) -> None:
    """ Check and print all analytics from a list """
    inventory: dict[str, dict[str, str | int]] = {}
    for i, arg in enumerate(arg_inputs[1:]):
        try:
            item, qty = arg.split(":")
            str_to_int = int(qty)
            inventory[item] = {
                'name': item,
                'type': item,
                'quantity': str_to_int,
                'value': 100 + i
            }
            if str_to_int < 1:
                raise NoItemError()
        except (KeyError, ValueError, NoItemError):
            print(f"Invalid item {arg} - skipping")

    if not inventory:
        print("No valid items were found")
        return

    total_items = sum(item['quantity'] for item in inventory.values())
    types = len(inventory)
    # “Where a higher‑order function takes a function pointer, and that
    # function is short and throwaway” → that’s the classic lambda sweet spot.
    sorted_dict = dict(
        sorted(inventory.items(), key=lambda x: x[1]["quantity"], reverse=True)
    )
    max_key = max(inventory, key=lambda k: inventory[k]['quantity'])
    min_key = min(inventory, key=lambda k: inventory[k]['quantity'])
    qty_categories = {}
    for state, condition in [
        ("Abundant", lambda v: v['quantity'] > 10),
        ("Moderate", lambda v: 5 <= v['quantity'] <= 10),
        ("Scarce", lambda v: v['quantity'] < 5)
    ]:
        items = {
            k: v['quantity'] for k, v in inventory.items() if condition(v)
        }
        if items:
            qty_categories[state] = items
    restock = [k for k, v in inventory.items() if v['quantity'] < 2]

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {types}")
    print()

    print("=== Current Inventory ===")
    for k, v in sorted_dict.items():
        print(
            f"{k}: {v['quantity']} unit{plural(v['quantity'])} "
            f"({(v['quantity'] / total_items) * 100:.1f}%)"
        )
    print()

    print("=== Inventory Statisitcs ===")
    print(
        f"Most abundant: {max_key} ({inventory[max_key]['quantity']} "
        f"unit{plural(inventory[max_key]['quantity'])})"
    )
    print(
        f"Least abundant: {min_key} ({inventory[min_key]['quantity']} "
        f"unit{plural(inventory[min_key]['quantity'])})"
    )
    print()

    print("=== Item Categories ===")
    for category, category_dict in qty_categories.items():
        print(f"{category}: {category_dict}")
    print()

    print("=== Management Suggestions ===")
    print(f"Restock needed: {', '.join(restock)}")
    print()

    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {', '.join(list(inventory.keys()))}")
    print("Dictionary values: ", end="")
    print(f"{', '.join(list(str(d['quantity']) for d in inventory.values()))}")
    print(
        "Sample lookup - 'sword' in inventory: "
        f"{bool(inventory.get('sword', 0))}"
    )


if __name__ == "__main__":
    analyze_inventory(sys.argv)
