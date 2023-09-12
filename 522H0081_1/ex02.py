# A urn contains 8 white balls, 6 black balls and 9 red balls. Three balls are “randomly draw” from a urn.

import itertools

def cross(A, B):
    return {a + b for a in A for b in B}

# (a) Find a list of all possible 3 balls and assign to variable U3. Assign numberof set U3 to variable len_U3.
print("\nSolution for (a)")
urn = cross('W', '12345678') | cross('B', '123456') | cross('R', '123456789') #8 white balls, 6 black balls and 9 red balls.
# lưu ý tham số cross(A, B); A chỉ truyền 1 chữ cái tượng trưng cho màu quả bóng 

U3 = list(itertools.combinations(urn, 3))
len_U3 = len(U3)

print("List of all possible 3 balls:", U3)
print("Number of possible sets U3:", len_U3)

# (b) Enumerate all possible cases of three balls of different colors.
print("\nSolution for (b)")
count_b = 0
for balls_combination_b in U3:
    if len(set(balls_combination_b)) == 3: # set sẽ loại bỏ các phần tử trùng lặp và chỉ giữ lại các phần tử duy nhất
        print(balls_combination_b)
        count_b += 1 

print("Ket qua cau b = ", count_b)

# (c) Enumerate all possible cases of the first ball being white and the second ball red.
print("\nSolution for (c)")
count_c = 0
for balls_combination_c in U3:
    if balls_combination_c[0][0] == 'W' and balls_combination_c[1][0] == 'R':
        print(balls_combination_c)
        count_c += 1 

print("Ket qua cau c = ", count_c)