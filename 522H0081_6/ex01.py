import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def plot_cdf_normal(mu, sigma):
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)  # Generate x values
    cdf = norm.cdf(x, mu, sigma)  # Compute the CDF values
    
    plt.plot(x, cdf)
    plt.xlabel('X')
    plt.ylabel('Cumulative Probability')
    plt.title('CDF of Normal Distribution')
    plt.grid(True)
    plt.show()

# Example usage
plot_cdf_normal(0, 1.5)
