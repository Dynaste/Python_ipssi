import random
from functions import verifier

random_price = random.randint(1,500)
score = 100

# Randomizer price
print(random_price)

# Ask for a price
print('Enter your price:')
x = input()
print('Your proposition is: ' + x)


verifier(x, random_price, score)