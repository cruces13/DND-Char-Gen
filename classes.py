import armor


class Class():
    def __init__(self, name, hit_dice, armor_prof, weapon_prof, tools, saving_throws, skills, equipment, features, cantrips, spells_known, spell_slots):
        self.name = name                       #String
        self.hit_dice = hit_dice               #Int
        self.armor_prof = armor_prof           #Array of strings
        self.weapon_prof = weapon_prof         #Array of strings
        self.tools = tools                     #Array of strings, because of Bard
        self.saving_throws = saving_throws     #Array of strings
        self.skills = skills                   #2D Array, first value is how many choices
        self.equipment = equipment             #Array of strings
        self.features = features               #Array of strings
        self.cantrips = cantrips               #Int
        self.spells_known = spells_known       #Int, or string if needs to be calced
        self.spell_slots = spell_slots         #Int, spell slots at level 1


Barbarian = Class(
    "Barbarian",
    12,
    ["Light Armor", "Medium Armor", "Shields"], 
    ["Simple", "Martial"],
    None,
    ["Strength", "Constitution"],
    [2, ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"]],
    [
        ["Greataxe", "Any Martial"],
        ["2 Handaxes", "Any Simple"],
        [["Explorer's Pack", "4 Javelins"]]
    ],
    ["Rage", "Unarmored Defense"],
    None,
    None,
    None
)
Bard = Class(
    "Bard",
    12,
    ["Light Armor"],
    ["Simple", "Hand Crossbow", "Longsword", "Rapier", "Shortsword"],
    "Three musical instruments",
    ["Dexterity", "Charisma"],
    [2, ["Athletics", "Acrobatics", "Sleight of Hand", "Stealth", "Arcana",
        "History", "Investigation", "Nature", "Religion", "Animal Handling",
        "Insight", "Medicine", "Perception", "Survival", "Deception",
        "Intimidation", "Performance", "Persuasion"]],
    [
        ["Rapier", "Longsword", "Any Simple"],
        ["Diplomat's Pack", "Entertainer's Pack"],
        ["Lute", "Any instrument"],
        ["Leather"],
        ["Dagger"]
    ],
    ["Spellcasting", "Bardic Inspiration(d6)"],
    2,
    4,
    2
)
Cleric = Class(
    "Cleric",
    8,
    ["Light Armor", "Medium Armor", "Shields"],
    ["Simple"],
    None,
    ["Wisdom", "Charisma"],
    [2, ["History", "Insight", "Medicine", "Persuasion", "Religion"]],
    [
        ["Mace"],
        ["Scale Mail", "Leather"],
        ["Light Crossbow and 20 Bolts", "Any Simple"],
        ["Priest's Pack", "Explorer's Pack"],
        ["Shield"],
        ["Holy Symbol"]
    ],
    ["Spellcasting", "Divine Domain"],
    3,
    "Wisdom mod + cleric level",
    2
)
Druid = Class(
    "Druid",
    8,
    ["Light Armor", "Medium Armor", "Shields"], #Cannot be made of metal
    ["Club", "Dagger", "Dart", "Javelin", "Mace", "Quarterstaff", "Scimitar", "Sling", "Spear"],
    "Herbalism Kit",
    ["Intelligence", "Wisdom"],
    [2, ["Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"]],
    [
        ["Shield", "Any Simple"],
        ["Scimitar", "Any Simple Melee"],
        ["Leather"],
        ["Explorer's Pack"],
        ["Druidic Focus"]
    ],
    ["Druidic", "Spellcasting"],
    2,
    "Wisdom mod + druid level",
    2
)
Fighter = Class(
    "Fighter",
    10,
    ["Light Armor", "Medium Armor", "Heavy Armor", "Shields"],
    ["Simple", "Martial"],
    None,
    ["Strength", "Constitution"],
    [2, ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight",
        "Intimidation", "Perception", "Survival"]],
    [
        ["Chain Mail", ["Leather", "Longbow", "20 Arrows"]],
        [["Any Martial", "Shield"], "Any 2 Martial"],
        [["Light Crossbow", "20 Bolts"], "2 Handaxes"],
        ["Dungeoneer's Pack", "Explorer's Pack"]
    ],
    ["Fighting Style", "Second Wind"],
    None,
    None,
    None
)
Monk = Class(
    "Monk",
    8,
    None,
    ["Simple", "Shortsword"],
    ["One Artisan's Tools", "One instrument"],
    ["Strength", "Dexterity"],
    [2, ["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"]],
    [
        ["Shortsword", "Any Simple"],
        ["Dungeoneer's Pack", "Explorer's Pack"],
        ["10 Darts"]
    ],
    ["Unarmored Defense", "Martial Arts(1d4)"],
    None,
    None,
    None
)
Paladin = Class(
    "Paladin",
    10,
    ["Light Armor", "Medium Armor", "Heavy Armor", "Shields"],
    ["Simple", "Martial"],
    None,
    ["Wisdom", "Charisma"],
    [2, ["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"]],
    [
        [["Any Martial", "Shield"], "Any 2 Martial"],
        ["5 Javelins", "Any Simple Melee"],
        ["Priest's Pack", "Explorer's Pack"],
        [["Chain Mail", "Holy Symbol"]]
    ],
    ["Divine Sense", "Lay on Hands"],
    None,
    None,
    None
)
Ranger = Class(
    "Ranger",
    10,
    ["Light Armor", "Medium Armor", "Shields"],
    ["Simple", "Martial"],
    None,
    ["Strength", "Dexterity"],
    [3, ["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"]],
    [
        ["Scale Mail", "Leather"],
        ["2 Shortswords", "Any 2 Simple Melee"],
        ["Dungeoneer's Pack", "Explorer's Pack"],
        [["Longbow", "20 Arrows"]]
    ],
    ["Favored Enemy", "Natural Explorer"],
    None,
    None,
    None
)
Rogue = Class(
    "Rogue",
    8,
    ["Light Armor"],
    ["Simple", "Hand Crossbow", "Longswords", "Rapier", "Shortsword"],
    "Thieve's Tools",
    ["Dexterity", "Intelligence"],
    [4, ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"]],
    [
        ["Rapier", "Shortsword"],
        [["Shortbow", "20 Arrows"], "Shortsword"],
        ["Burglar's Pack", "Dungeoneer's Pack", "Explorer's Pack"],
        [["Leather", "2 Daggers", "Thieve's Tools"]]
    ],
    ["Expertise", "Sneak Attack(1d6)", "Thieves' Cant"],
    None,
    None,
    None
)
Sorceror = Class(
    "Sorceror",
    6,
    None,
    ["Dagger", "Dart", "Sling", "Quarterstaff", "Light Crossbow"],
    None,
    ["Constitution", "Charisma"],
    [2, ["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"]],
    [
        [["Light Crossbow", "20 Bolts"], "Any Simple"],
        ["Component Pouch", "Arcane Focus"],
        ["Dungeoneer's Pack", "Explorer's Pack"],
        ["2 Daggers"]
    ],
    ["Spellcasting", "Sorcerous Origin"],
    4,
    2,
    2
)
Warlock = Class(
    "Warlock",
    8,
    ["Light Armor"],
    ["Simple"],
    None,
    ["Wisdom", "Charisma"],
    [2, ["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"]],
    [
        [["Light Crossbow", "20 Bolts"], "Any Simple"],
        ["Component Pouch", "Arcane Focus"],
        ["Scholar's Pack", "Dungeoneer's Pack"],
        [["Leather", "Any Simple", "2 Daggers"]]
    ],
    ["Otherworldly Patron", "Pact Magic"],
    2,
    2,
    1
)
Wizard = Class(
    "Wizard",
    6,
    None,
    ["Dagger", "Dart", "Sling", "Quarterstaff", "Light Crossbow"],
    None,
    ["Intelligence", "Wisdom"],
    [2, ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"]],
    [
        ["Quarterstaff", "Dagger"],
        ["Component Pouch", "Arcane Focus"],
        ["Scholar's Pack", "Explorer's Pack"],
        ["Spellbook"]
    ],
    ["Spellcasting", "Arcane Recovery"],
    3,
    "Intelligence mod + Wizard level",
    2
)

CLASSES = [
    Barbarian,
    Bard,
    Cleric,
    Druid,
    Fighter,
    Monk, 
    Paladin,
    Ranger,
    Rogue,
    Sorceror,
    Warlock,
    Wizard
]