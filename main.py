import races
import classes
import functions
import armor
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

class Character():
    def __init__(self,
                race = choice(races.RACES),
                _class = choice(classes.CLASSES),
                skills = functions.mod_skills(),
                alignment = choice(ALIGNMENT)
                ):
        self.race = race
        self._class = _class
        self.skills = skills
        self.alignment = alignment
        self.size = self.race.size
        self.speed = self.race.speed
        self.languages = self.race.languages
        self.armor = None
        self.has_shield = False
        self.AC = 0

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

    def ability_scores_modifiers(self):
        #Functional but ugly
        self.str_mod = (self.abilities["Strength"] - 10) // 2
        self.dex_mod = (self.abilities["Dexterity"] - 10) // 2
        self.con_mod = (self.abilities["Constitution"] - 10) // 2
        self.cha_mod = (self.abilities["Charisma"] - 10) // 2
        self.int_mod = (self.abilities["Intelligence"] - 10) // 2
        self.wis_mod = (self.abilities["Wisdom"] - 10) // 2

    def set_skill_proficiencies(self):
        #Functional
        self.skill_proficiencies = []
        for _ in range(self._class.skills[0]):
            self.skill_proficiencies.append(choice(self._class.skills[1]))

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

    def get_equipment(self):
        ##Does NOT YET account for multiple range coverage
        class_equip = self._class.equipment
        self.equipment = []
        for i in class_equip:
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



char = Character(_class=classes.Rogue)
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