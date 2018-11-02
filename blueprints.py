import constants
import functions
from random import choice

class Character():
    def __init__(self, race, _class):
        self.race = race
        self._class = _class
        self.background = choice(constants.BACKGROUNDS)
        self.skills = functions.mod_skills()
        self.alignment = choice(constants.ALIGNMENT)
        self.size = self.race.size
        self.speed = self.race.speed
        self.languages = self.race.languages
        self.equipment = []
        self.armor_class = 0

    def determine_ability_scores(self):
        self.abilities = {
        "Strength" :     0,
        "Dexterity" :    0,
        "Constitution" : 0,
        "Charisma" :     0,
        "Intelligence" : 0,
        "Wisdom" :       0
        }
        for i in self.abilities:
            scores = functions.die(4, 6)
            scores.sort()
            scores = scores[1::]
            self.abilities[i] = sum(scores)

    def set_alignment(self):
        if self.race.alignment:
            if functions.die(1,6) == 1:
                self.alignment = choice(constants.ALIGNMENT)
            self.alignment = choice(self.race.alignment)
        else:
            self.alignment = choice(constants.ALIGNMENT)
    
    def set_extras(self):
        self.hp_start = self._class.hit_dice + self.abilities["Constitution"]
        self.initiative = self.abilities["Dexterity"]
    
    def set_languages(self):
        langs = constants.LANGUAGES
        if self.race.name == "Human":
            langs.remove("Common")
            self.languages.remove("Any")
            self.languages.append(choice(langs))
        elif self.race.name == "Half-Elf":
            langs.remove("Common")
            langs.remove("Elvish")
            self.languages.remove("Any")
            self.languages.append(choice(langs))
        
class Race():
    def __init__(self, name, abilities, alignment, size, speed, languages):
        self.name = name                       #String
        self.abilities = abilities             #Dictionary, ability scores
        self.alignment = alignment             #Array of strings, any particular
        self.size = size
        self.speed = speed
        self.languages = languages

class Class():
    def __init__(self, name, hit_dice, armor_prof, weapon_prof, tools, saving_throws, skills, equipment, features, cantrips, spells_known, spell_slots):
        self.name = name                       #String
        self.hit_dice = hit_dice               #Int
        self.armor_prof = armor_prof           #Array of strings
        self.weapon_prof = weapon_prof         #Array of strings
        self.tools = tools                     #Array of strings, because of Bard
        self.saving_throws = saving_throws     #Array of strings
        self.skills = skills                   #Dictionary hold skills and values
        self.equipment = equipment             #Array of strings
        self.features = features               #Array of strings
        self.cantrips = cantrips               #Int
        self.spells_known = spells_known       #Int, or string if needs to be calced
        self.spell_slots = spell_slots         #Int, spell slots at level 1

class Background():
    def __init__(self, skills, languages, tools):
        self.skills = skills
        self.languages = languages
        self.tools = tools

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

class Armor():
    def __init__(self, name, AC, strength, stealth, weight, cost):
        self.name = name
        self.AC = AC
        self.strength = strength
        self.stealth = stealth
        self.weight = weight
        self.cost = cost
        