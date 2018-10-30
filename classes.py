from blueprints import Class
from random import choice

Barbarian = Class(
    12,
    12,
    ["light armor", "medium armor", "shields"],
    ["simple", "martial"],
    None,
    ["strength", "constitution"],
    ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"],
    [
        ["Greataxe", "Any Martial"],
        ["2 Handaxes", "Any Simple"],
        ["Explorer's Pack", "4 Javelins"]
    ],
    ["Rage", "Unarmored Defense"],
    None,
    None
)
