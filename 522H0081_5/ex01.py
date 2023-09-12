import matplotlib.pyplot as plt
from scipy.stats import binom

# Parameters
n = 5  # Number of machines
p = 0.1  # Probability of a machine being broken in 1 session

# (a) Calculate the probability of 2 machines being broken in 1 session
x = 2  # Number of successes (broken machines)
prob_2_broken = binom.pmf(x, n, p)
print("Probability of 2 machines being broken:", round(prob_2_broken,5))

# (b) Create a graph of X and the corresponding probabilities
X = range(n + 1)  # Possible values of X: 0, 1, 2, ..., n
probabilities = [binom.pmf(x, n, p) for x in X]

plt.bar(X, probabilities)
plt.xlabel('X (Number of broken machines)')
plt.ylabel('Probability')
plt.title('Binomial Distribution')
plt.show()
