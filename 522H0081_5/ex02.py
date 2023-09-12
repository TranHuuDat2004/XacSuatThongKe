import matplotlib.pyplot as plt
from scipy.stats import poisson

# Parameter
lambda_ = 3  # Average number of calls per minute

# (a) Calculate the probability of 2 calls in 1 minute
x = 2  # Number of calls
prob_2_calls = poisson.pmf(x, lambda_)
print("Probability of 2 calls:", round(prob_2_calls,5))

# (b) Create a graph of X and the corresponding probabilities
X = range(1, 6)  # Possible values of X: 1, 2, 3, 4, 5
probabilities = [poisson.pmf(x, lambda_) for x in X]

plt.bar(X, probabilities)
plt.xlabel('X (Number of calls)')
plt.ylabel('Probability')
plt.title('Poisson Distribution')
plt.show()
