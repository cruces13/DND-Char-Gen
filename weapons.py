from classes import Weapon
from functions import die

#Melee Simple
Club = Weapon(
    "Club",
    .01,
    die(1, 4),
    "Bludgeoning",
    None,
    2,
    ["light"]
)
Dagger = Weapon(
    "Dagger",
    2,
    die(1, 4),
    "Piercing",
    [20, 60],
    1,
    ["finesse", "light", "thrown"]
)
Greatclub = Weapon(
    "Greatclub",
    .02,
    die(1, 8),
    "Bludgeoning",
    None,
    10,
    ["two-handed"]
)
Handaxe = Weapon(
    "Handaxe",
    5,
    die(1, 6),
    "Slashing",
    [20, 60],
    2,
    ["light", "thrown"]
)
Javelin = Weapon(
    "Javelin",
    .05,
    die(1, 6),
    "Piercing",
    [30, 120],
    2,
    ["thrown"]
)
Light_Hammer = Weapon(
    "Light_Hammer",
    2,
    die(1, 4),
    "Bludgeoning",
    [20, 60],
    2,
   ["light", "thrown"] 
)
Mace = Weapon(
    "Mace",
    5,
    die(1, 6),
    "Bludgeoning",
    None,
    4,
    None
)
Quarterstaff = Weapon(
    "Quarterstaff",
    .02,
    die(1, 6),
    "Bludgeoning",
    None,
    4,
    ["versatile8"]
)
Sickle = Weapon(
    "Sickle",
    1,
    die(1, 4),
    "Slashing",
    None,
    2,
    ["light"]
)
Spear = Weapon(
    "Spear",
    1,
    die(1, 6),
    "Piercing",
    [20, 60],
    3,
    ["thrown", "versatile8"]
)

#Ranged Simple
Light_Crossbow = Weapon(
    "Light Crossbow",
    25,
    die(1, 8),
    "Piercing",
    [80, 320],
    5,
    ["ammunition", "loading", "two-handed"],
    melee = False
)
Dart = Weapon(
    "Dart",
    .005,
    die(1, 4),
    "Piercing",
    [20, 60],
    .25,
    ["finesse", "thrown"],
    melee = False 
)
Shortbow = Weapon(
    "Shortbow",
    25,
    die(1, 6),
    "Piercing",
    [80, 320],
    2,
    ["ammunition", "two-handed"],
    melee = False
)
Sling = Weapon(
    "Sling",
    .01,
    die(1, 4),
    "Bludgeoning",
    [30, 120],
    None,
    ["ammunition"],
    melee = False
)

#Melee Martial
Battleaxe = Weapon(
    "Battleaxe",
    10,
    die(1, 8),
    "Slashing",
    None,
    4,
    ["versatile10"]
)
Flail = Weapon(
    "Flail",
    10,
    die(1, 8),
    "Bludgeoning",
    None,
    2,
    None
)
Glaive = Weapon(
    "Glaive",
    20,
    die(1, 10),
    "Slashing",
    None,
    6,
    ["heavy", "reach", "two-handed"]
)
Greataxe = Weapon(
    "Greataxe",
    30,
    die(1, 12),
    "Slashing",
    None,
    7,
    ["heavy", "two-handed"]
)
Greatsword = Weapon(
    "Greatsword",
    50,
    die(2, 6),
    "Slashing",
    None,
    6,
    ["heavy", "two-handed"]
)
Halberd = Weapon(
    "Halberd",
    20,
    die(1, 10),
    "Slashing",
    None,
    6,
    ["heavy", "reach", "two-handed"]
)
# Lance = Weapon(
#     "Lance",
#     10,
#     die(1, 12),
#     "Piercing",
#     None,
#     6,
#     ["reach","special^1"]
# )
Longsword = Weapon(
    "Longsword",
    15,
    die(1, 8),
    "Slashing",
    None,
    3,
    ["versatile10"]
)
Maul = Weapon(
    "Maul",
    10,
    die(2, 6),
    "Bludgeoning",
    None,
    10,
    ["heavy", "two-handed"]
)
Morningstar = Weapon(
    "Morningstar",
    15,
    die(1, 8),
    "Piercing",
    None,
    4,
    None
)
Pike = Weapon(
    "Pike",
    5,
    die(1, 10),
    "Piercing",
    None,
    18,
    ["heavy", "reach", "two-handed"]
)
Rapier = Weapon(
    "Rapier",
    25,
    die(1, 8),
    "Piercing",
    None,
    2,
    ["finesse"]
)
Scimitar = Weapon(
    "Scimitar",
    25,
    die(1, 6),
    "Slashing",
    None,
    3,
    ["finesse", "light"]
)
Shortsword = Weapon(
    "Shortsword",
    10,
    die(1, 6),
    "Piercing",
    None,
    2,
    ["finesse", "light"]
)
Trident = Weapon(
    "Trident",
    5,
    die(1, 6),
    "Piercing",
    [20, 60],
    4,
    ["thrown", "versatile8"]
)
War_Pick = Weapon(
    "War Pick",
    5,
    die(1, 8),
    "Piercing",
    None,
    2,
    None
)
Warhammer = Weapon(
    "Warhammer",
    15,
    die(1, 8),
    "Bludgeoning",
    None,
    2,
    ["versatile10"]
)
Whip = Weapon(
    "Weapon",
    2,
    die(1, 4),
    "Slashing",
    None,
    3,
    ["finesse", "reach"]
)

#Ranged Martial
Blowgun = Weapon(
    "Blowgun",
    10,
    1,
    "Piercing",
    [25, 100],
    1,
    ["ammunition", "loading"],
    melee = False 
)
Crossbow_hand = Weapon(
    "Crossbow, hand",
    75,
    die(1, 6),
    "Piercing",
    [30, 120],
    3,
    ["ammuntion", "light", "loading"],
    melee = False
)
Crossbow_heavy = Weapon(
    "Crossbow, heavy",
    50,
    die(1, 10),
    "Piercing",
    [100, 400],
    18,
    ["ammunition", "heavy", "loading", "two-handed"],
    melee = False
)
Longbow = Weapon(
    "Longbow",
    50,
    die(1, 8),
    "Piercing",
    [150, 600],
    2,
    ["ammunition", "heavy", "two-handed"],
    melee = False
)
# Net = Weapon(
#     "Net",
#     1,
#     None,
#     None,
#     [5, 15],
#     3,
#     ["thrown", "special^2"],
#     melee = False
# )
