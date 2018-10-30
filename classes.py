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
    None, None, None, None   #This line is the pausing point, script runs
)
