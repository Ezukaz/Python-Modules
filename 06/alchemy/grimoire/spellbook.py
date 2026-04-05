#!/usr/bin/env python3


def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    if "INVALID" in validate_ingredients(ingredients):
        record_reject = "rejected"
    else:
        record_reject = "recorded"
    return f"Spell {record_reject}: {spell_name} ({validate_ingredients(ingredients)})"
