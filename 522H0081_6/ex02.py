import numpy as np
from scipy.special import erf

def cdf_normal(x, mu, sigma):
    z = (x - mu) / sigma
    cdf = (1 + erf(z / np.sqrt(2))) / 2
    return cdf

mu = 10
sigma = 1

probability = cdf_normal(12, mu, sigma) - cdf_normal(9, mu, sigma)
print("Probability:", round(probability,5))