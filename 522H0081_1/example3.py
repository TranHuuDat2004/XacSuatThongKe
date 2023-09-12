'''A urn contains 8 white balls, 6 black balls and 9 red balls. Six balls are “randomly draw” from the urn.
(a) How many ways 6 balls can be selected?
(b) Enumerate all possible cases of 6 balls.
(c) Enumerate all possible cases of the first and the last ball should be red. '''

'''The set of ways of concatenating one item from
collection A with one from B.'''

def cross(A, B):
    return {a + b for a in A for b in B}
# lưu ý tham số cross(A, B); A chỉ truyền 1 chữ cái tượng trưng cho màu quả bóng

urn = cross('W', '12345678') | cross('B', '123456') | cross('R', '123456789') #8 white balls, 6 black balls and 9 red balls.
print("urn = ", urn)

import itertools
U6 = list(itertools.combinations(urn, 6))

print("\nSolution for (a)")
print(len(U6))
print("\nSolution for (b)")
for s in U6:
    print(s)
print("\nSolution for (c)")
for s in U6:
    if s[0][0]=='R' and s[-1][0]=='R':
        print(s)

# kết quả chạy nó lạ lắm