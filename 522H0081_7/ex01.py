import random

# a/ Both dice are the same
def simulator_dice_a(n):
    count = 0  

    for a in range(n):
        dice1 = random.randint(1, 6)  # Roll the first dice
        dice2 = random.randint(1, 6)  # Roll the second dice

        if dice1 == dice2 :  
            count += 1

    probability = count / n  # Calculate the experimental probability

    return probability

# b/ Both dice are different
def simulator_dice_b(n):
    count = 0  

    for b in range(n):
        dice1 = random.randint(1, 6)  
        dice2 = random.randint(1, 6)  

        if dice1 != dice2 :  
            count += 1

    probability = count / n  

    return probability

# c/ Both dice are even
def simulator_dice_c(n):
    count = 0  

    for c in range(n):
        dice1 = random.randint(1, 6)  
        dice2 = random.randint(1, 6)  

        if dice1 %2 == 0 and dice2 %2 == 0:  
            count += 1

    probability = count / n  

    return probability

# d/ Both dice are odd
def simulator_dice_d(n):
    count = 0  

    for d in range(n):
        dice1 = random.randint(1, 6)  
        dice2 = random.randint(1, 6)  

        if dice1 %2 != 0 and dice2 %2 != 0:  
            count += 1

    probability = count / n  

    return probability

# e/ One die is even and the other is odd
def simulator_dice_e(n):
    count = 0  

    for e in range(n):
        dice1 = random.randint(1, 6)  
        dice2 = random.randint(1, 6)  

        if (dice1 %2 != 0 and dice2 %2 == 0) or (dice1 %2 == 0 and dice2 %2 != 0):  
            count += 1

    probability = count / n  

    return probability

# f/ Both dice are 6
def simulator_dice_f(n):
    count = 0  

    for f in range(n):
        dice1 = random.randint(1, 6)  
        dice2 = random.randint(1, 6)  

        if dice1 == 6 and dice2  == 6 :
            count += 1

    probability = count / n  

    return probability

# g/ Summation of both dice are greater than 10.
def simulator_dice_g(n):
    count = 0  

    for g in range(n):
        dice1 = random.randint(1, 6)  
        dice2 = random.randint(1, 6)  

        if dice1 + dice2 > 10:  
            count += 1

    probability = count / n

    return probability

n = 1000 # Số lần thử nghiệm

result_a = simulator_dice_a(n)
print("a/ Both dice are the same:", result_a)

result_b = simulator_dice_b(n)
print("b/ Both dice are different:", result_b)

result_c = simulator_dice_c(n)
print("c/ Both dice are even:", result_c)

result_d = simulator_dice_d(n)
print("d/ Both dice are odd:", result_d)

result_e = simulator_dice_e(n)
print("e/ One die is even and the other is odd:", result_e)

result_f = simulator_dice_f(n)
print("f/ Both dice are 6:", result_f)

result_g = simulator_dice_g(n)
print("g/ Summation of both dice are greater than 10:", result_g)