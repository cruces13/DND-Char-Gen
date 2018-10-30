from blueprints import Race
from random import choice
from constants import LANGUAGES

#Race objects
Dwarf = Race(
    "Dwarf",
    {
    "Strength":     0,
    "Dexterity":    0,
    "Constitution": 2,
    "Charisma":     0,
    "Intelligence": 0,
    "Wisdom":       0
    },
    [],
    "Medium",
    25,
    ["Common", "Dwarvish"]
)
Human = Race(
    "Human",
    {
    "Strength":     1,
    "Dexterity":    1,
    "Constitution": 1,
    "Charisma":     1,
    "Intelligence": 1,
    "Wisdom":       1
    },
    [],
    "Medium",
    30,
    ["Common", "Any"]
)
