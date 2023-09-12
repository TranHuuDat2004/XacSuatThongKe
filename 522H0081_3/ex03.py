import random

# (a) Create a set 'Cards' to store all the cards in the deck
suits = ['♠', '♡', '♢', '♣']
ranks = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

Cards = {rank + suit for suit in suits for rank in ranks}

# (b) Randomly collect 3 cards and save them in variable 'B'
B = random.sample(Cards, 3)
print(B)

# (c) Event A1: Cards include 1 or 2 K
A1 = [card for card in B if 'K' in card and card.count('K') <= 2]

# (d) Event A2: Cards include at least 1 K
A2 = [card for card in B if 'K' in card]

# (e) Calculate the probabilities of events A1 and A2
P_A1 = len(A1) / len(B)
P_A2 = len(A2) / len(B)

# Print the results
print("Event A1:")
print(A1)
print("\nEvent A2:")
print(A2)
print("\nProbability of A1:", P_A1)
print("Probability of A2:", P_A2)
