from blueprints import Class
import functions

Barbarian = Class(
    "Barbarian",
    12,
    ["Light Armor", "Medium Armor", "Shields"],
    ["Simple", "Martial"],
    None,
    ["Strength", "Constitution"],
    ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"],
    [
        ["Greataxe", "Any Martial"],
        ["2 Handaxes", "Any Simple"],
        ["Explorer's Pack", "4 Javelins"]
    ],
    ["Rage", "Unarmored Defense"],
    None,
    None,
    None
)
Bard = Class(
    "Bard",
    12,
    ["light armor"],
    ["Simple", "Hand Crossbow", "Longsword", "Rapier", "Shortsword"],
    "Three musical instruments",
    ["Dexterity", "Charisma"],
    ["Any three"],
    [
        ["Rapier", "Longsword", "Any Simple"],
        ["Diplomat's Pack", "Entertainer's Pack"],
        ["Lute", "Any instrument"],
        ["Leather Armor"],
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
    ["History", "Insight", "Medicine", "Persuasion", "Religion"],
    [
        ["Mace"],
        ["Scale Mail", "Leather Armor"],
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
    ["Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"],
    [
        ["Shield", "Any Simple"],
        ["Scimitar", "Any Simple Melee"],
        ["Leather Armor"],
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
    ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"],
    [
        ["Chain Mail", ["Leather Armor", "Longbow", "20 Arrows"]],
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
    ["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"],
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
    ["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"],
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
    ["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"], #Choose Three
    [
        ["Scale Mail", "Leather Armor"],
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
    ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"], #Choose four
    [
        ["Rapier", "Shortsword"],
        [["Shortbow", "20 Arrows"], "Shortsword"],
        ["Burglar's Pack", "Dungeoneer's Pack", "Explorer's Pack"],
        [["Leather Armor", "2 Daggers", "Thieve's Tools"]]
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
    ["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"],
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
    ["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"],
    [
        [["Light Crossbow", "20 Bolts"], "Any Simple"],
        ["Component Pouch", "Arcane Focus"],
        ["Scholar's Pack", "Dungeoneer's Pack"],
        [["Leather Armor", "Any Simple", "2 Daggers"]]
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
    ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"],
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