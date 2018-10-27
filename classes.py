class Weapon(object):
    def __init__(self, name, cost, damage, damage_type, distance, weight, properties):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.damage_type = damage_type
        self.distance = distance
        self.weight = weight
        self.properties = properties

class Die(object):
    def __init__(self, die, count):
        self.count = count
        self.die = die



Club = Weapon("Club", .01, Die(1,4), "Bludgeoning", None, 2, ["light"])
Dagger = Weapon("Dagger", 2, Die(1,4), "Piercing", [20, 60], 1, ["finesse", "light", "thrown"])
print(Club.cost)
print(Dagger.cost)
