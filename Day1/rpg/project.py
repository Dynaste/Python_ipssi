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

# create Link character
with open('ressources/players.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            if row[1] == "Link":
                link = Entities()
                link.init(f'{row[1]}', f'{row[2]}', f'{row[3]}', f'{row[12]}')      

# create Ganon Boss
with open('ressources/bosses.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            if row[1] == "Ganon":
                ganon = Entities()
                ganon.init(f'{row[1]}', f'{row[2]}', f'{row[3]}', f'{row[12]}')   

# create Bokoblin ennemy
with open('ressources/enemies.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
           if row[1] == "Bokoblin":
                bokoblin = Entities()
                bokoblin.init(f'{row[1]}', f'{row[2]}', f'{row[3]}', f'{row[12]}')  



print(ganon.name)
print(link.name)
print(bokoblin.name)





# with open('ressources/bosses.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     print("-------------------------------")
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#             print(f'{row[1]} has {row[2]} HP and {row[4]} STR')
#             line_count += 1
#     print(f'Processed {line_count} lines.')



# with open('ressources/players.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     print("-------------------------------")
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             player = Players()
#             # print(row[1], row[2], row[3], row[12])
#             player.init(row[1], row[2], row[3], row[12])
#             print(f'{row[1]} has {row[2]} HP and {row[4]} STR')
#             line_count += 1
#     print(f'Processed {line_count} lines.')


# with open('ressources/enemies.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     print("-------------------------------")
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#             print(f'{row[1]} has {row[2]} HP and {row[4]} STR, this monster has a rarity of: {row[12]}')
#             line_count += 1
#     print(f'Processed {line_count} lines.')