import random

suits = ['♥', '♦', '♣', '♠']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = [f"{rank}{suit}" for rank in ranks for suit in suits]

def calculate_probability_a(n):
    count = 0
    
    for _ in range(n):
        hand = random.sample(deck, 4)  # Draw 4 cards randomly from the deck
        
        # Check if all 4 cards are from the same suit
        if len(set([card[1] for card in hand])) == 1:
            count += 1
    
    probability = count / n
    return probability


def calculate_probability_b(n):
    count = 0
    
    for _ in range(n):
        hand = random.sample(deck, 4)  # Draw 4 cards randomly from the deck
        
        # Check if all 4 cards are from different suits
        if len(set([card[1] for card in hand])) == 4:
            count += 1
    
    probability = count / n
    return probability


def calculate_probability_c(n):
    count = 0
    
    for _ in range(n):
        hand = random.sample(deck, 4)  # Draw 4 cards randomly from the deck
        
        # Check if all 4 cards are the same color
        colors = {'♥', '♦'}  # Colors for Hearts and Diamonds
        if set([card[1] for card in hand]) <= colors or set([card[1] for card in hand]) > colors:
            count += 1
    
    probability = count / n
    return probability


def calculate_probability_d(n):
    count = 0
    
    for _ in range(n):
        hand = random.sample(deck, 4)  # Draw 4 cards randomly from the deck
        
        # Check if all 4 cards are the same value
        if len(set([card[0] for card in hand])) == 1:
            count += 1
    
    probability = count / n
    return probability


def calculate_probability_e(n):
    count = 0
    
    for _ in range(n):
        hand = random.sample(deck, 4)  # Draw 4 cards randomly from the deck
        
        # Check if all 4 cards are numbers
        numbers = set(map(str, range(2, 11)))
        if set([card[0] for card in hand]) <= numbers:
            count += 1
    
    probability = count / n
    return probability


def calculate_probability_f(n):
    count = 0
    
    for _ in range(n):
        hand = random.sample(deck, 4)  # Draw 4 cards randomly from the deck
        
        # Check if all 4 cards are faces
        faces = {'J', 'Q', 'K', 'A'}
        if set([card[0] for card in hand]) <= faces:
            count += 1
    
    probability = count / n
    return probability


n = 10000

# Event a: All 4 cards are from the same suit
prob_a = calculate_probability_a(n)
print("a/ All 4 cards are from the same suit:", prob_a)

# Event b: All 4 cards are from different suits
prob_b = calculate_probability_b(n)
print("b/ All 4 cards are different suits:", prob_b)

# Event c: All 4 cards are the same color
prob_c = calculate_probability_c(n)
print("c/ All 4 cards are the same color:", prob_c)

# Event d: All 4 cards are the same value
prob_d = calculate_probability_d(n)
print("d/ All 4 cards are the same value:", prob_d)

# Event e: All 4 cards are numbers
prob_e = calculate_probability_e(n)
print("e/ All 4 cards are numbers:", prob_e)

# Event f: All 4 cards are faces
prob_f = calculate_probability_f(n)
print("f/ All 4 cards are faces:", prob_f)
