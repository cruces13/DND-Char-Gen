from random import randint, choice


def die(count, size):
    dice = []
    for _ in range(count):
        dice.append(randint(1, size))
    return dice

def calc_spells_known(obj, ability):
    #Adjusts the Spells known attribute
    return obj.abilities[ability]