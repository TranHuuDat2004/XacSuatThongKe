import random
count = 0
n = 10000
for i in range(n):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    if die1==1 and die2==6:
        count += 1
print("Xac suat de tong xi ngau ra mat chan la =",count/n)