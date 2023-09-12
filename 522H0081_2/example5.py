# Import the required function libraries
from itertools import product
import random

# Define ranks , suits and cards
Ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
Suits = {'♡', '♢', '♣', '♠'}
Cards = list(product(Ranks , Suits))
print("Tong bo bai la =",len(Cards))
print(Cards[:10])
'''Write a function to calculate the experimental probability of drawing the red
card with the number of tests n as the parameter:'''

def simulator_poker(n):
    count = 0
    for i in range(n):
        index = random.randint(0, 51)
        if Cards[index][1] == '♡' or Cards[index][1] == '♢':
            count += 1
    return count/n
'''Call above function with n = 10, 100, 1000, 10000, ...'''

print("simulator_poker(10) =", simulator_poker(10))
print("simulator_poker(100) =", simulator_poker(100))
print("simulator_poker(1000) =",simulator_poker(1000))
print("simulator_poker(10000) =", simulator_poker(10000))