import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Define parameters for the normal distribution
mu = 3
sigma = 4  # square root of variance

# Create an array of X values
X = np.linspace(mu - 3*sigma, mu + 3*sigma, 1000)

# (a) Calculate the probability density function (PDF) of the normal distribution
pdf_normal = norm.pdf(X, mu, sigma)

# (b) Calculate the cumulative distribution function (CDF) of the normal distribution
cdf_normal = norm.cdf(X, mu, sigma)

# (c) Calculate the probability P{2 < X < 7}
p_2_to_7 = norm.cdf(7, mu, sigma) - norm.cdf(2, mu, sigma)

# Plot the PDF and CDF
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(X, pdf_normal, color='blue')
plt.title('Probability Density Function (PDF) of Normal Distribution')
plt.xlabel('X')
plt.ylabel('PDF')

plt.subplot(2, 1, 2)
plt.plot(X, cdf_normal, color='orange')
plt.title('Cumulative Distribution Function (CDF) of Normal Distribution')
plt.xlabel('X')
plt.ylabel('CDF')

plt.tight_layout()
plt.show()

# Print the probability P{2 < X < 7}
print("P{2 < X < 7}:", p_2_to_7)
