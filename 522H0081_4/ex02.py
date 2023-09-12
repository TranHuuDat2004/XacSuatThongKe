import numpy as np

# (a) Save the results of flipping 2 coins into the variable x (list type)
x = []
for _ in range(10000):
    result = np.random.randint(0, 2) + np.random.randint(0, 2)
    x.append(result)

# Convert x to a NumPy array
x = np.array(x)

# (b) Find the values of random variable X and save to variable X
X = np.unique(x)

# (c) Calculate the probability distribution function of the random variable X and store it in variable P (list type)
P = []
for value in X:
    probability = np.count_nonzero(x == value) / len(x)
    P.append(probability)

# (d) Calculate the characteristic parameters of random variable X
expectation = np.mean(x)  # expectation
variance = np.var(x)  # variance
std_dev = np.std(x)  # standard deviation

# Optional: Round the values to a specific number of decimals
expectation = round(expectation, 2)
variance = round(variance, 2)
std_dev = round(std_dev, 2)

# (e) Calculate the probability to have at least one head
at_least_one_head = np.count_nonzero(x >= 1) / len(x)

print("Random variable X:", X)
print("Probability distribution function P:", P)
print("Expectation:", expectation)
print("Variance:", variance)
print("Standard Deviation:", std_dev)
print("Probability to have at least one head:", at_least_one_head)
