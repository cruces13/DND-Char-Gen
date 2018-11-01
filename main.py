import blueprints
import races
import classes
from random import choice

char = blueprints.Character(choice(races.RACES), choice(classes.CLASSES))
char.determine_ability_scores()
char.set_alignment()
char.set_extras()
char.set_languages()
print(char.race.name, char._class.name, char.alignment, char.abilities, char.languages)
