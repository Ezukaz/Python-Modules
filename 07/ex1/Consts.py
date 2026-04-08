#!/usr/bin/env python3

# from enum import Enum
# I wanted to do this but it seems like enums in python are not the same as C
# They are objects. And so I have a dilemma when I pass objects or compare
# strings. This idea was good but the structure of this assignment doesn't
# allow for me to adjust and therefore, I will switch to constants

# class CardType(Enum):
#     CREATURE = "Creature"
#     SPELL = "Spell"
#     ARTIFACT = "Artifact"


# class EffectType(Enum):
#     DAMAGE = "damage"
#     HEAL = "heal"
#     BUFF = "buff"
#     DEBUFF = "debuff"

CREATURE = "creature"
SPELL = "spell"
ARTIFACT = "artifact"
TOURNAMENT = "tournament"
DAMAGE = "damage"
HEAL = "heal"
BUFF = "buff"
DEBUFF = "debuff"
