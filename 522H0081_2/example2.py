from fractions import Fraction
import itertools
import random
'''All combinations of n items; each combo as a
concatenated str.'''
def P(event , space):
    return Fraction(len(event & space), len(space))

def cross(A, B):
    return {a + b for a in A for b in B} # kieu du lieu tu dien (dictionary)
urn = cross('W', '12345678') | cross('B', '123456') | cross('R', '123456789')
print("Khong gian mau =", urn)

def combos(items , n):
    return {' '.join(combo) for combo in itertools.combinations(items , n)}

U6 = combos(urn, 6)
U6_list = list(U6)
print("So luong danh sach U6 =",len(U6_list))
print("Lay ngau nhien 6 banh =",random.sample(U6_list, 10))

# Problem 1: All 6 balls are red
red6 = {s for s in U6 if s.count('R') == 6}
print("Problem 1: All 6 balls are red =", P(red6, U6))

# Problem 2: 3 blue balls, 2 white balls and 1 red ball
b3w2r1 = {s for s in U6 if s.count('B') == 3 and s.count('W') == 2 and s.count('R') == 1}

print("Problem 2: 3 blue balls, 2 white balls and 1 red ball =",P(b3w2r1 , U6))
# Problem 3: exactly 4 white balls
w4 = {s for s in U6 if s.count('W') == 4}
print("Problem 3:exactly 4 white balls =",P(w4, U6))
