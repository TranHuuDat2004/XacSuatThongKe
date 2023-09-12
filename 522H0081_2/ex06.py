import random

def simulator_poker1(n):
    count_all_hearts = 0  # Counter for the number of times all 5 cards are hearts

    for _ in range(n):
        deck = ['♥A', '♥2', '♥3', '♥4', '♥5', '♥6', '♥7', '♥8', '♥9', '♥10', '♥J', '♥Q', '♥K',
                '♠A', '♠2', '♠3', '♠4', '♠5', '♠6', '♠7', '♠8', '♠9', '♠10', '♠J', '♠Q', '♠K',
                '♦A', '♦2', '♦3', '♦4', '♦5', '♦6', '♦7', '♦8', '♦9', '♦10', '♦J', '♦Q', '♦K',
                '♣A', '♣2', '♣3', '♣4', '♣5', '♣6', '♣7', '♣8', '♣9', '♣10', '♣J', '♣Q', '♣K']

        hand = random.sample(deck, 5)  # Take 5 random cards from the deck

        if all(card[0] == '♥' for card in hand):  # Check if all cards are hearts
            count_all_hearts += 1

    probability = count_all_hearts / n  # Calculate the experimental probability

    return probability

# Example usage:
n = 10000  # Number of trials
probability = simulator_poker1(n)
print("xác suất thử nghiệm của sự kiện 5 thẻ đều là trái tim (♥):", probability)
