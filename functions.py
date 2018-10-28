import random

def die(count, size):
    if count == 1:
        return random.randint(1, size)
    else:
        dice = []
        for i in range(count):
            dice.append(random.randint(1, size))
