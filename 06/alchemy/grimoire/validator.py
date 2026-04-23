#!/usr/bin/env python3


def validate_ingredients(ingredients: str) -> str:
    is_valid = "VALID" if any(
        x in ingredients for x in ["fire", "water", "earth", "air"]
    ) else "INVALID"
    return f"{ingredients} - {is_valid}"
