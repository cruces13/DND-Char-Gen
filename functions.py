from random import randint
from constants import ABILITIES

def die(count, size):
    if count == 1:
        return randint(1, size)
    else:
        dice = []
        for _ in range(count):
            dice.append(randint(1, size))
        return dice


###### THIS CURRENTLY GIVES WRONG EXPECTED OUTPUT, CHECK LINE 21
def determine_ability_scores():
    for i in range(len(ABILITIES)):
        scores = []
        scores = die(4, 6)
        scores.sort()
        scores = scores[1::]
        list(ABILITIES.values())[i] = sum(scores)
    return ABILITIES


print(determine_ability_scores())