# Link => 60hp , 15str
# Oponent => Bokoblin: 30hp, 5str
# Boss => 150hp, 20str
# 10 floor
# fonction :
    # Heal => restore 50% hp
    # Attack => deal dmg based on str
import csv

class Entities:
    def init(self, name, hp, strength, rarity):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.rarity = rarity

def importCsv(path, className, name):
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                if row[1] == str(name).capitalize():
                    # name = Entities()
                    className.init(f'{row[1]}', f'{row[2]}', f'{row[3]}', f'{row[12]}')
link = Entities()
ganon = Entities()
bokoblin = Entities()
importCsv('ressources/players.csv', link, "Link")
importCsv('ressources/bosses.csv', ganon, "Ganon")
importCsv('ressources/enemies.csv', bokoblin, "Bokoblin")


print(ganon.name)
print(link.name)
print(bokoblin.name)