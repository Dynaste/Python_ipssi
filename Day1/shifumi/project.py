import random
from functions import shifumi


pool_choice = ["Pierre", "Papier", "Ciseaux"]
score = 0

print("Welcome to shifumi arcade game !")
print("Enter 1 for PIERRE, 2 for PAPIER, 3 for CISEAUX")
user_choice = input()

shifumi(pool_choice, score, user_choice)

    
# while user_choice != "exit": 
#     ia_choice = pool_choice[random.randint(0,2)]
#     result = pool_choice[int(user_choice) -1]

#     print("You have chosen: " + result)
#     print("Your oponent has chosen: " + ia_choice)

#     if result == "Pierre":
#         if ia_choice == "Pierre":
#             print("Equality")
#         elif ia_choice == "Papier":
#             print("You loose")
#         else:
#             print("You win")
#             score = score + 1
#     elif result == "Papier":
#         if ia_choice == "Pierre":
#             print("You win")
#             score = score + 1
#         elif ia_choice == "Papier":
#             print("Equality")
#         else:
#             print("You loose")
#     else:
#         if ia_choice == "Pierre":
#             print("You loose")
#         elif ia_choice == "Papier":
#             print("You win")
#             score = score + 1
#         else:
#             print("Equality")

#     print("Current score: " + str(score))
#     print("Enter 1 for PIERRE, 2 for PAPIER, 3 for CISEAUX")
#     user_choice = input()