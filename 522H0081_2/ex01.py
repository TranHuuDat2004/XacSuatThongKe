import random

def simulator_dice1(n):
    count_even = 0  # Counter for the number of times both dice are even

    for _ in range(n):
        dice1 = random.randint(1, 6)  # Roll the first dice
        dice2 = random.randint(1, 6)  # Roll the second dice

        if dice1 % 2 == 0 and dice2 % 2 == 0:  # Check if both dice are even
            count_even += 1

    probability = count_even / n  # Calculate the experimental probability

    return probability

# Example usage:
n = 10000  # Number of times to roll the dice
probability = simulator_dice1(n)
print("xác suất của biến cố cả hai con súc sắc đều chẵn:", probability)
