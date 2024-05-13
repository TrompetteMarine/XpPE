import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import logistic

# Define parameters
num_samples = 10
num_distributions = 10
threshold = 0.556
max_dominant = 4
max_trials = 10

# Define marginal distribution p(x)
def p_x(x):
    return  (np.exp(x)/1+np.exp(x))

# Generate D parameters
D_values = np.random.uniform(0, 1, num_distributions)

# Generate and plot cumulative distribution functions
dominant_count = 0
trial_count = 0
plt.figure(figsize=(8, 5))  # Adjust plot size
for i in range(num_distributions):
    if trial_count >= max_trials:
        break
    D = D_values[i]
    x = logistic.rvs(loc=0, scale=1/D, size=num_samples)
    x_sorted = np.sort(x)
    y = np.arange(1, num_samples + 1) / num_samples
    if D > threshold and dominant_count < max_dominant:
        plt.plot(x_sorted, y, label=f'p(x|D={D:.3f})', linewidth=2)  # Highlight dominating distributions
        dominant_count += 1
        trial_count += 1
    else:
        plt.plot(x_sorted, y, label=f'p(x|D={D:.3f})', alpha=0.5)  # Non-dominating distributions with lower opacity
        trial_count += 1

# Plot marginal distribution
x_marginal = np.linspace(0, 10, 1000)
plt.plot(x_marginal, logistic.cdf(x_marginal), 'k--', label='p(x)', linewidth=2)

plt.title('Cumulative Distribution Functions')
plt.xlabel('x')
plt.xlim([0,10])
plt.ylabel('Cumulative Probability')
plt.legend()
plt.grid(True)
plt.tight_layout()  # Adjust layout
plt.show()

print(f"Number of conditional distributions dominating p(x): {dominant_count}")
