from random import randint, choice
import constants

def die(count, size):
    #Returns and int if count == 1, returns array otherwise
    if count == 1:
        return randint(1, size)
    else:
        dice = []
        for _ in range(count):
            dice.append(randint(1, size))
        return dice



def mod_skills():
    skills = {
        "Acrobatics" :      0,
        "Animal Handling" : 0,
        "Arcana" :          0,
        "Athletics" :       0,
        "Deception" :       0,
        "History" :         0,
        "Insight" :         0,
        "Intimidator" :     0,
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
    return skills

def calc_spells_known(obj, ability):
    #Adjusts the Spells known attribute
    return obj.abilities[ability]