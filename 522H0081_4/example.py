# For example, launch 8,000 times

import random

x = [random.randint(0, 9) for i in range(8000)]
X = set(x) # liet ke cac khong gian mau
print("x là:",x)
print("X là:", X)