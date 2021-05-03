import random



pool_choice = ["shi", "fu", "mi"]
user_choise = ""
ia_choice = pool_choice[random.randint(0,2)]


print("Welcome to shifumi arcade game !")
print("Enter 1 for SHI, 2 for FU, 3 for MI")

x = input()

print("You have choosen: " + pool_choice[int(x) -1])
print("Enter exit to leave the game")

x = input()

if x == "exit":
    