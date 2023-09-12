S = {('Thanh', 'Nữ'), ('Hồng', 'Nữ'), ('Thương', 'Nữ'), ('Đào', 'Nữ'),
('My', 'Nữ'), ('Yến', 'Nữ'), ('Hạnh', 'Nữ'), ('My', 'Nữ'),('Vy', 'Nữ'),
('Tiên', 'Nữ'),('Thanh', 'Nam'), ('Thanh', 'Nam'),('Bình', 'Nam'),
('Nhật', 'Nam'), ('Hào', 'Nam'), ('Đạt', 'Nam'), ('Minh', 'Nam')}

# (a) Event A: Names that are "Thanh"
A = [item for item in S if item[0] == 'Thanh']

# (b) Event B: Names that are "Nữ" (Female)
B = [item for item in S if item[1] == 'Nữ']

# (c) Event A ∩ B: Names that are both "Thanh" and "Nữ" (Female)
A_B = [item for item in S if item[0] == 'Thanh' and item[1] == 'Nữ']

# (d) Probabilities
P_A = len(A) / len(S)
P_B = len(B) / len(S)
P_A_B = len(A_B) / len(S)

# (e) Probability of the name "Thanh" given that it is a female
P_Thanh_given_Female = len(A_B) / len(B)

# Print the results
print("(a) Event A:", A)

print("\n(b) Event B:", B)

print("\n(c) Event A ∩ B:", A_B)

print("\n(d) Probabilities:")
print("P(A):", P_A)
print("P(B):", P_B)
print("P(A ∩ B):", P_A_B)
print("\n(e) Probability of 'Thanh' given 'Female':", P_Thanh_given_Female)