import random
from functions import shifumi


pool_choice = ["Pierre", "Papier", "Ciseaux"]
score = 0

print("Welcome to shifumi arcade game !")
print("Enter 1 for PIERRE, 2 for PAPIER, 3 for CISEAUX")
user_choice = input()

shifumi(pool_choice, score, user_choice)