import random
n = 10
count = 0
for simulations in range(n):
    tosses = random.randint(0, 1)
    if tosses == 1:
        count += 1
print("Xac suat nem dong xu ra mat ngua la =", count/n)