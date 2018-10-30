from random import randint
from constants import ABILITIES

def die(count, size):
    #Returns and int if count == 1, returns array otherwise
    if count == 1:
        return randint(1, size)
    else:
        dice = []
        for _ in range(count):
            dice.append(randint(1, size))
        return dice

def determine_ability_scores():
    for i in ABILITIES:
        scores = die(4, 6)
        scores.sort()
        scores = scores[1::]
        ABILITIES[i] = sum(scores)
    return ABILITIES