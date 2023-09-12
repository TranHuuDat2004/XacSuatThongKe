import itertools

# (a) Performance probability space
S = [''.join(combo) for combo in itertools.product('MF', repeat=3)]

# (b) Number of elements in probability space S
num_elements_S = len(S)

# (c) Event B: At least one female cat
B = [item for item in S if 'F' in item]

# (d) Event A: All three cats are female
A = [item for item in S if item == 'FFF']

# (e) Probability of all three cats being female given at least one cat is female
P_A_given_B = len(A) / len(B)


# Print the results
print("(a) Performance probability space:")
print(S)
print("\n(b) Number of elements in probability space S:", num_elements_S)
print("\n(c) Event B: At least one female cat:")
print(B)
print("\n(d) Event A: All three cats are female:")
print(A)
print("\n(e) Probability of all three cats being female given at least one cat is female:", P_A_given_B)
