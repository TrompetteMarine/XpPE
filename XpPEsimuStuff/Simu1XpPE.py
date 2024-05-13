import numpy as np 
from scipy.stats import norm
import matplotlib.pyplot as plt 
from matplotlib.pyplot import *
from matplotlib.legend_handler import HandlerLine2D
import matplotlib.patches as mp
# Parameters
params = [1, 2, 3]  # Parameters moving from 1 to 3
benchmark_param = 1.5  # Benchmark parameter
counterfactual_params = np.random.uniform(0.2, 0.8, 1000)  # Counterfactual parameters

# Generate data
x = np.linspace(-1, 1, 1000)
benchmark_cdf = norm.cdf(x, loc=0, scale=benchmark_param)
counterfactual_cdf = np.percentile([norm.cdf(x, loc=0, scale=p) for p in counterfactual_params], 50, axis=0)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, benchmark_cdf, label=f'Benchmark (no Learning)', linestyle='--')
for param in params:
    cdf = norm.cdf(x, loc=0, scale=param)
    plt.plot(x, cdf, label=f'Other Agreement: n={param}')
plt.plot(x, counterfactual_cdf, label='Bot Counterfactual', linestyle='-.')
plt.title('Probability for leader to switch votes considering Other group menmbers vote')
plt.xlabel('x')
plt.ylabel(r'$p(X= v \rightarrow X= 1- v|D,n)$')
plt.legend()
plt.grid(True)
plt.show()