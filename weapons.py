
class Weapon():
    def __init__(self, name, cost, damage, damage_type, distance, weight, properties, melee = True):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.damage_type = damage_type
        self.distance = distance
        self.weight = weight
        self.properties = properties
        self.melee = melee

#Melee Simple
Club = Weapon(
    "Club",
    .01,
    (1, 4),
    "bludgeoning",
    None,
    2,
    ["light"]
)
Dagger = Weapon(
    "Dagger",
    2,
    (1, 4),
    "piercing",
    [20, 60],
    1,
    ["finesse", "light", "thrown"]
)
Greatclub = Weapon(
    "Greatclub",
    .02,
    (1, 8),
    "bludgeoning",
    None,
    10,
    ["two-handed"]
)
Handaxe = Weapon(
    "Handaxe",
    5,
    (1, 6),
    "slashing",
    [20, 60],
    2,
    ["light", "thrown"]
)
Javelin = Weapon(
    "Javelin",
    .05,
    (1, 6),
    "piercing",
    [30, 120],
    2,
    ["thrown"]
)
Light_Hammer = Weapon(
    "Light_Hammer",
    2,
    (1, 4),
    "bludgeoning",
    [20, 60],
    2,
   ["light", "thrown"] 
)
Mace = Weapon(
    "Mace",
    5,
    (1, 6),
    "bludgeoning",
    None,
    4,
    None
)
Quarterstaff = Weapon(
    "Quarterstaff",
    .02,
    (1, 6),
    "bludgeoning",
    None,
    4,
    ["versatile8"]
)
Sickle = Weapon(
    "Sickle",
    1,
    (1, 4),
    "slashing",
    None,
    2,
    ["light"]
)
Spear = Weapon(
    "Spear",
    1,
    (1, 6),
    "piercing",
    [20, 60],
    3,
    ["thrown", "versatile8"]
)

#Ranged Simple
Light_Crossbow = Weapon(
    "Light Crossbow",
    25,
    (1, 8),
    "piercing",
    [80, 320],
    5,
    ["ammunition", "loading", "two-handed"],
    melee = False
)
Dart = Weapon(
    "Dart",
    .005,
    (1, 4),
    "piercing",
    [20, 60],
    .25,
    ["finesse", "thrown"],
    melee = False 
)
Shortbow = Weapon(
    "Shortbow",
    25,
    (1, 6),
    "piercing",
    [80, 320],
    2,
    ["ammunition", "two-handed"],
    melee = False
)
Sling = Weapon(
    "Sling",
    .01,
    (1, 4),
    "bludgeoning",
    [30, 120],
    None,
    ["ammunition"],
    melee = False
)

#Melee Martial
Battleaxe = Weapon(
    "Battleaxe",
    10,
    (1, 8),
    "slashing",
    None,
    4,
    ["versatile10"]
)
Flail = Weapon(
    "Flail",
    10,
    (1, 8),
    "bludgeoning",
    None,
    2,
    None
)
Glaive = Weapon(
    "Glaive",
    20,
    (1, 10),
    "slashing",
    None,
    6,
    ["heavy", "reach", "two-handed"]
)
Greataxe = Weapon(
    "Greataxe",
    30,
    (1, 12),
    "slashing",
    None,
    7,
    ["heavy", "two-handed"]
)
Greatsword = Weapon(
    "Greatsword",
    50,
    (2, 6),
    "slashing",
    None,
    6,
    ["heavy", "two-handed"]
)
Halberd = Weapon(
    "Halberd",
    20,
    (1, 10),
    "slashing",
    None,
    6,
    ["heavy", "reach", "two-handed"]
)
# Lance = Weapon(
#     "Lance",
#     10,
#     (1, 12),
#     "piercing",
#     None,
#     6,
#     ["reach","special^1"]
# )
Longsword = Weapon(
    "Longsword",
    15,
    (1, 8),
    "slashing",
    None,
    3,
    ["versatile10"]
)
Maul = Weapon(
    "Maul",
    10,
    (2, 6),
    "bludgeoning",
    None,
    10,
    ["heavy", "two-handed"]
)
Morningstar = Weapon(
    "Morningstar",
    15,
    (1, 8),
    "piercing",
    None,
    4,
    None
)
Pike = Weapon(
    "Pike",
    5,
    (1, 10),
    "piercing",
    None,
    18,
    ["heavy", "reach", "two-handed"]
)
Rapier = Weapon(
    "Rapier",
    25,
    (1, 8),
    "piercing",
    None,
    2,
    ["finesse"]
)
Scimitar = Weapon(
    "Scimitar",
    25,
    (1, 6),
    "slashing",
    None,
    3,
    ["finesse", "light"]
)
Shortsword = Weapon(
    "Shortsword",
    10,
    (1, 6),
    "piercing",
    None,
    2,
    ["finesse", "light"]
)
Trident = Weapon(
    "Trident",
    5,
    (1, 6),
    "piercing",
    [20, 60],
    4,
    ["thrown", "versatile8"]
)
War_Pick = Weapon(
    "War Pick",
    5,
    (1, 8),
    "piercing",
    None,
    2,
    None
)
Warhammer = Weapon(
    "Warhammer",
    15,
    (1, 8),
    "bludgeoning",
    None,
    2,
    ["versatile10"]
)
Whip = Weapon(
    "Weapon",
    2,
    (1, 4),
    "slashing",
    None,
    3,
    ["finesse", "reach"]
)

#Ranged Martial
Blowgun = Weapon(
    "Blowgun",
    10,
    1,
    "piercing",
    [25, 100],
    1,
    ["ammunition", "loading"],
    melee = False 
)
Crossbow_hand = Weapon(
    "Hand Crossbow",
    75,
    (1, 6),
    "piercing",
    [30, 120],
    3,
    ["ammuntion", "light", "loading"],
    melee = False
)
Crossbow_heavy = Weapon(
    "Heavy Crossbow",
    50,
    (1, 10),
    "piercing",
    [100, 400],
    18,
    ["ammunition", "heavy", "loading", "two-handed"],
    melee = False
)
Longbow = Weapon(
    "Longbow",
    50,
    (1, 8),
    "piercing",
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

SIMPLE = [

]
MARTIAL = [
    
]
