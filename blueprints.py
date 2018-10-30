import constants
import random

class Character():
    def __init__(self, race, _class, background, abilities, skills, alignment, size):
        self.race = race
        self._class = _class
        self.background = background
        self.abilities = abilities
        self.skills = skills
        self.alignment = alignment
        self.size = size

class Race():
    def __init__(self, name, abilities, alignment, size, speed, languages):
        self.name = name                       #String
        self.abilities = abilities             #Dictionary, ability scores
        self.alignment = alignment             #Array of strings, any particular
        self.size = size
        self.speed = speed
        self.languages = languages

class Class():
    def __init__(self, hit_dice, hp_start, armor_prof, weapon_prof, tools, saving_throws, skills, equipment, features, cantrips, spells):
        self.hit_dice = hit_dice               #Int
        self.hp_start = hp_start               #Int, hit die + con modifier
        self.armor_prof = armor_prof           #Array of strings
        self.weapon_prof = weapon_prof         #Array of strings
        self.tools = tools                     #Array of strings, because of Bard
        self.saving_throws = saving_throws     #Array of strings
        self.skills = skills                   #Dictionary hold skills and values
        self.equipment = equipment             #Array of strings
        self.features = features               #Array of strings
        self.cantrips = cantrips               #Int, Cantrips known
        self.spells = spells                   #Int, spell slots at level 1

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
        