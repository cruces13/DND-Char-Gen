        
class Race():
    def __init__(self, name, abilities, alignment, size, speed, languages):
        self.name = name                       #String
        self.abilities = abilities             #Dictionary, ability scores
        self.alignment = alignment             #Array of strings, any particular
        self.size = size
        self.speed = speed
        self.languages = languages


#Race objects
Dragonborn = Race(
    "Dragonborn",
    {
    "Strength":     2,
    "Dexterity":    0,
    "Constitution": 0,
    "Charisma":     1,
    "Intelligence": 0,
    "Wisdom":       0
    },
    ["Chaotic Evil", "Chaotic Good", "Lawful Evil", "Lawful Good"],
    "Medium",
    30,
    ["Common", "Draconic"]
)
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
    None,
    "Medium",
    25,
    ["Common", "Dwarvish"]
)
Elf = Race(
    "Elf",
    {
    "Strength":     0,
    "Dexterity":    2,
    "Constitution": 0,
    "Charisma":     0,
    "Intelligence": 0,
    "Wisdom":       0,
    },
    ["Chaotic Good"],
    "Medium",
    30,
    ["Common", "Elvish"]
)
Gnome = Race(
    "Gnome",
    {
    "Strength":     0,
    "Dexterity":    0,
    "Constitution": 0,
    "Charisma":     0,
    "Intelligence": 2,
    "Wisdom":       0
    },
    ["Chaotic Good", "Neutral Good", "Lawful Good"],
    "Small",
    25,
    ["Common", "Gnomish"]
)
Halfling = Race(
    "Halfling",
    {
    "Strength":     0,
    "Dexterity":    2,
    "Constitution": 0,
    "Charisma":     0,
    "Intelligence": 0,
    "Wisdom":       0
    },
    ["Lawful Good"],
    "Small",
    25,
    ["Common", "Halfling"]
)
#Still need to implement 2 ability scores of choice +1
Half_Elf = Race(
    "Half-Elf",
    {
    "Strength":     0,
    "Dexterity":    0,
    "Constitution": 0,
    "Charisma":     2,
    "Intelligence": 0,
    "Wisdom":       0
    },
    ["Chaotic Good", "Chaotic Neutral", "Chaotic Evil"],
    "Medium",
    30,
    ["Common", "Elvish", "Any"]
)
Half_Orc = Race(
    "Half-Orc",
    {
    "Strength":     2,
    "Dexterity":    0,
    "Constitution": 1,
    "Charisma":     0,
    "Intelligence": 0,
    "Wisdom":       0
    },
    ["Chaotic Evil"],
    "Medium",
    25,
    ["Common", "Orc"]
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
    None,
    "Medium",
    30,
    ["Common", "Any"]
)
Tiefling = Race(
    "Tiefling",
    {
    "Strength":     0,
    "Dexterity":    0,
    "Constitution": 0,
    "Charisma":     2,
    "Intelligence": 1,
    "Wisdom":       0
    },
    ["Chaotic Good", "Chaotic Neutral", "Chaotic Evil"],
    "Medium",
    30,
    ["Common", "Infernal"]
)

RACES = [
    Dragonborn,
    Dwarf,
    Elf,
    Gnome,
    Half_Elf,
    Half_Orc,
    Halfling,
    Human,
    Tiefling
]
