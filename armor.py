
class Armor():
    def __init__(self, name, AC, strength, stealth, weight, cost):
        self.name = name
        self.AC = AC
        self.strength = strength
        self.stealth = stealth
        self.weight = weight
        self.cost = cost

#Light and medium armor adds dex modifier, medium armor mod max at 2
#Light Armor
Padded = Armor(
    "Padded",
    11,
    None,
    None,
    8,
    5
    )
Leather = Armor(
    "Leather",
    11,
    None,
    True,
    10,
    10
    )
Studded_Leather = Armor(
    "Studded Leather",
    12,
    None,
    None,
    13,
    45
)
#Medium Armor
Hide = Armor(
    "Hide",
    12,
    None,
    None,
    12,
    10
)
Chain_Shirt = Armor(
    "Chain Shirt",
    13,
    None,
    None,
    20,
    50
)
Scale_Mail = Armor(
    "Scale Mail",
    14,
    None,
    True,
    45,
    50
)
Breastplate = Armor(
    "Breastplate",
    14,
    None,
    None,
    20,
    400
)
Half_Plate = Armor(
    "Half Plate",
    15,
    None,
    True,
    40,
    750
)
#Heavy Armor
Ring_Mail = Armor(
    "Ring Mail",
    14,
    None,
    True,
    40,
    30
)
Chain_Mail = Armor(
    "Chain Mail",
    16,
    13,
    True,
    55,
    75
)
Splint_Mail = Armor(
    "Splint Mail",
    17,
    15,
    True,
    60,
    200
)
Plate_Mail = Armor(
    "Plate Mail",
    18,
    15,
    True,
    65,
    1500
)
#Shield
Shield = Armor(
    "Shield",
    2,
    None,
    None,
    6,
    10
)
LIGHT_ARMOR = [Padded, Leather, Studded_Leather]
MEDIUM_ARMOR = [Hide, Chain_Shirt, Scale_Mail, Breastplate, Half_Plate]
HEAVY_ARMOR = [Ring_Mail, Chain_Mail, Splint_Mail, Plate_Mail]
SHIELD = [Shield]
ARMOR = [j for i in [LIGHT_ARMOR, MEDIUM_ARMOR, HEAVY_ARMOR] for j in i]
