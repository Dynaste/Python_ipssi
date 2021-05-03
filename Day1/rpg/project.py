
# Link => 60hp , 15str

# Oponent => Bokoblin: 30hp, 5str

# Boss => 150hp, 20str

# 10 floor

# fonction :
    # Heal => restore 50% hp
    # Attack => deal dmg based on str


import csv

with open('ressources/bosses.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    print("-------------------------------")
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            print(f'{row[1]} has {row[2]} HP and {row[4]} STR')
            line_count += 1
    print(f'Processed {line_count} lines.')

with open('ressources/players.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    print("-------------------------------")
    for row in csv_reader:
        if line_count == 0:

            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            print(f'{row[1]} has {row[2]} HP and {row[4]} STR')
            line_count += 1
    print(f'Processed {line_count} lines.')

with open('ressources/enemies.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    print("-------------------------------")
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            print(f'{row[1]} has {row[2]} HP and {row[4]} STR')
            line_count += 1
    print(f'Processed {line_count} lines.')