import random

def simulator_dice2(n):
    count_even_odd = 0  # Counter for the number of times one dice is even and the other is odd

    for _ in range(n):
        dice1 = random.randint(1, 6)  # Roll the first dice
        dice2 = random.randint(1, 6)  # Roll the second dice

        if (dice1 % 2 == 0 and dice2 % 2 != 0) or (dice1 % 2 != 0 and dice2 % 2 == 0):
            # Check if one dice is even and the other is odd
            count_even_odd += 1

    probability = count_even_odd / n  # Calculate the experimental probability

    return probability

# Example usage:
n = 10000  # Number of times to roll the dice
probability = simulator_dice2(n)
print("xác suất của biến cố một con chẵn và một con lẻ:", probability)
