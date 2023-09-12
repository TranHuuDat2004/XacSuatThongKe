import random

def simulator_dice3(n):
    count_same = 0  # Counter for the number of times the two dice have the same value

    for _ in range(n):
        dice1 = random.randint(1, 6)  # Roll the first dice
        dice2 = random.randint(1, 6)  # Roll the second dice

        if dice1 == 1 and dice2 == 6:
            count_same += 1

    probability = count_same / n  # Calculate the experimental probability

    return probability

# Example usage:
n = 10000  # Number of times to roll the dice
probability = simulator_dice3(n)
print("xác suất của biến cố một con súc sắc cho 1 và con kia cho 6:", probability)