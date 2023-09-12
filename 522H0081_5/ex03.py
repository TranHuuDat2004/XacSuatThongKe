import matplotlib.pyplot as plt
from scipy.stats import binom

# Parameters
n = 10  # Number of trials (bullets)
p = 0.4  # Probability of hitting the target

# (a) Calculate the probability of hitting the target in the third try
x = 3  # Number of successes
prob_third_try = binom.pmf(x, n, p)
print("Probability of hitting the target in the third try:", round(prob_third_try,5))

# (b) Create a graph of X and the corresponding probabilities
X = range(1, n+1)  # Possible values of X: 1 to n
probabilities = [binom.pmf(x, n, p) for x in X]

plt.bar(X, probabilities)
plt.xlabel('X (Number of tries)')
plt.ylabel('Probability')
plt.title('Binomial Distribution')
plt.show()
