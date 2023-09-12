import random

def simulator_poker2(n):
    count_all_different = 0  # Counter for the number of times all 4 cards are of different suits

    for _ in range(n):
        deck = ['♥A', '♥2', '♥3', '♥4', '♥5', '♥6', '♥7', '♥8', '♥9', '♥10', '♥J', '♥Q', '♥K',
                '♠A', '♠2', '♠3', '♠4', '♠5', '♠6', '♠7', '♠8', '♠9', '♠10', '♠J', '♠Q', '♠K',
                '♦A', '♦2', '♦3', '♦4', '♦5', '♦6', '♦7', '♦8', '♦9', '♦10', '♦J', '♦Q', '♦K',
                '♣A', '♣2', '♣3', '♣4', '♣5', '♣6', '♣7', '♣8', '♣9', '♣10', '♣J', '♣Q', '♣K']

        hand = random.sample(deck, 4)  # Take 4 random cards from the deck

        suits = [card[0] for card in hand]  # Extract the suits of the cards in the hand

        if len(set(suits)) == 4:  # Check if all suits are different
            count_all_different += 1

    probability = count_all_different / n  # Calculate the experimental probability

    return probability

# Example usage:
n = 10000  # Number of trials
probability = simulator_poker2(n)
print("Experimental Probability:", probability)
