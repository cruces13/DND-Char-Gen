import races
import classes
import functions
import armor
import weapons
from random import choice, randint


ALIGNMENT = [
    "Chaotic Good",
    "Chaotic Neutral",
    "Chaotic Evil",
    "Neutral Good",
    "True Neutral",
    "Neutral Evil",
    "Lawful Good",
    "Lawful Neutral",
    "Lawful Evil"
]
LANGUAGES = [
    "Common",
    "Dwarvish",
    "Elvish",
    "Giant",
    "Gnomish",
    "Goblin",
    "Halfling",
    "Orc"
]
SKILL_TAG = {
        "Acrobatics" :      "Dexterity",
        "Animal Handling" : "Wisdom",
        "Arcana" :          "Intelligence",
        "Athletics" :       "Strength",
        "Deception" :       "Charisma",
        "History" :         "Intelligence",
        "Insight" :         "Wisdom",
        "Intimidation" :    "Charisma",
        "Investigation" :   "Intelligence",
        "Medicine" :        "Wisdom",
        "Nature" :          "Intelligence",
        "Perception" :      "Wisdom",
        "Performance" :     "Charisma",
        "Persuasion" :      "Charisma",
        "Religion" :        "Intelligence",
        "Sleight of Hand" : "Dexterity",
        "Stealth" :         "Dexterity",
        "Survival" :        "Wisdom"
    }

class Character():
    def __init__(self,
                race = choice(races.RACES),
                _class = choice(classes.CLASSES),
                alignment = choice(ALIGNMENT)
                ):
        self.race = race
        self._class = _class
        self.alignment = alignment
        self.size = self.race.size
        self.speed = self.race.speed
        self.languages = self.race.languages
        self.equipment = []
        self.armor = None
        self.has_shield = False
        self.AC = 0
        self.saving_throws = self._class.saving_throws

    def determine_ability_scores(self, method):
        ## Does NOT YET account for class bias
        self.abilities = {
        "Strength" :     0,
        "Dexterity" :    0,
        "Constitution" : 0,
        "Charisma" :     0,
        "Intelligence" : 0,
        "Wisdom" :       0
        }
        if method == "roll":
            for i in self.abilities:
                scores = functions.die(4, 6)
                scores.sort()
                scores = scores[1::]
                self.abilities[i] = sum(scores)
        elif method == "array":
            scores = [8, 10, 12, 13, 14, 15]
            for i in self.abilities:
                rand_index = randint(0, len(scores) - 1)
                self.abilities[i] = scores[rand_index]
                scores.pop(rand_index)
        #Add racial modifier
        for i in self.abilities:
            self.abilities[i] += self.race.abilities[i]

    def ability_scores_modifiers(self):
        #Functional but ugly
        self.str_mod = (self.abilities["Strength"] - 10) // 2
        self.dex_mod = (self.abilities["Dexterity"] - 10) // 2
        self.con_mod = (self.abilities["Constitution"] - 10) // 2
        self.cha_mod = (self.abilities["Charisma"] - 10) // 2
        self.int_mod = (self.abilities["Intelligence"] - 10) // 2
        self.wis_mod = (self.abilities["Wisdom"] - 10) // 2
        self.ability_mods = {
            "Strength" : self.str_mod,
            "Dexterity" : self.dex_mod,
            "Charisma" : self.cha_mod,
            "Constitution" : self.con_mod,
            "Intelligence" : self.int_mod,
            "Wisdom" : self.wis_mod
        }

    def set_skill_proficiencies(self):
        #Functional
        self.skill_proficiencies = []
        for _ in range(self._class.skills[0]):
            temp = choice(self._class.skills[1])
            while (temp in self.skill_proficiencies):
                temp = choice(self._class.skills[1])
            self.skill_proficiencies.append(temp)

    def skill_modifiers(self):
        #Functional
        self.skills = {
        "Acrobatics" :      0,
        "Animal Handling" : 0,
        "Arcana" :          0,
        "Athletics" :       0,
        "Deception" :       0,
        "History" :         0,
        "Insight" :         0,
        "Intimidation" :    0,
        "Investigation" :   0,
        "Medicine" :        0,
        "Nature" :          0,
        "Perception" :      0,
        "Performance" :     0,
        "Persuasion" :      0,
        "Religion" :        0,
        "Sleight of Hand" : 0,
        "Stealth" :         0,
        "Survival" :        0
        }
        for i in self.skills:
            self.skills[i] = self.ability_mods[SKILL_TAG[i]]
            if i in self.skill_proficiencies:
                self.skills[i] += self._class.prof_bonus

    def set_alignment(self):
        #Functional, accounts for race bias
        if self.race.alignment:
            if functions.die(1,6) == 1:
                self.alignment = choice(ALIGNMENT)
            self.alignment = choice(self.race.alignment)
        else:
            self.alignment = choice(ALIGNMENT)
    
    def set_extras(self):
        ##WIP
        self.hp_start = self._class.hit_dice + self.abilities["Constitution"]
        self.initiative = self.abilities["Dexterity"]
    
    def set_languages(self):
        #Functional, accounts for race bias
        langs = LANGUAGES
        if self.race.name == "Human":
            langs.remove("Common")
            self.languages.remove("Any")
            self.languages.append(choice(langs))
        elif self.race.name == "Half-Elf":
            langs.remove("Common")
            langs.remove("Elvish")
            self.languages.remove("Any")
            self.languages.append(choice(langs))

    def check_equip(self, style):
        #Functional but ugly
        if style == "Ranged":
            ranged_count = 0
            for item in self.equipment:
                if item in weapons.RANGED:
                    ranged_count += 1
            return ranged_count
        elif style == "Armor":
            armor_count = 0
            for item in self.equipment:
                if item in armor.ARMOR:
                    armor_count += 1
            return armor_count

    def get_equipment(self):
        ##Does NOT YET account for wildcards, ugly
        for i in self._class.equipment:
            decision = choice(i)
            if type(decision) is list:
                for i in decision:
                    self.equipment.append(i)
            else:
                self.equipment.append(decision)
        for i in self.equipment:
            if i == "Shield":
                self.has_shield = True
            for j in armor.ARMOR:
                if i == j.name:
                    self.armor = j
        #"Smart" Select
        if self.check_equip("Ranged") > 1 or self.check_equip("Armor") > 1:
            self.get_equipment()
        #Check for duplicates
        for item in self.equipment:
            if self.equipment.count(item) > 1:
                self.get_equipment()

    def calc_armor_class(self):
        #Functional but can probably be simplified
        if self.armor:
            if self.armor in armor.LIGHT_ARMOR:
                self.AC = self.armor.AC + self.dex_mod
            elif self.armor in armor.MEDIUM_ARMOR:
                if self.dex_mod > 2:
                    self.AC = self.armor.AC + 2
                else:
                    self.AC = self.armor.AC + self.dex_mod
            elif self.armor in armor.HEAVY_ARMOR:
                self.AC = self.armor.AC
        else:
            self.AC = 10 + self.dex_mod
        if self.has_shield:
            self.AC += 2



char = Character()
char.determine_ability_scores("array")
char.set_alignment()
char.set_extras()
char.set_languages()
char.ability_scores_modifiers()
char.get_equipment()
char.calc_armor_class()
char.set_skill_proficiencies()
print(char.race.name, char._class.name)
print(char.alignment)
print(char.abilities)
print(char.languages)
print("Character's equipment ", char.equipment)
print(char.str_mod, char.dex_mod)
print("The Armor class is ", char.AC)
print(char.skill_proficiencies)
char.skill_modifiers()

