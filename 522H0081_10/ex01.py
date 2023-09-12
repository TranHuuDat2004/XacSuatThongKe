import random
import numpy as np

# (a) Flip two dice 10,000 times and store results in variable x
x = [random.randint(1, 6) + random.randint(1, 6) for _ in range(10000)]

# (b) Find the values of random variable X and save to variable X
X = list(set(x))

# (c) Calculate the probability distribution function of X and store it in variable P
P = [x.count(value) / len(x) for value in X]

# (d) Calculate the characteristic parameters of X
expectation = np.mean(X)
variance = np.var(X)
std_deviation = np.sqrt(variance)

# Print the results
print("Random variable X:", X)
print("Probability distribution P:", P)
print("Expectation:", expectation)
print("Variance:", variance)
print("Standard Deviation:", std_deviation)
