from IPython.core.pylabtools import figsize
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

figsize(12.5, 3.5)

count_data = np.loadtxt("demos/bayesian-programming/014_poisson.csv")
n_count_data = len(count_data)
plt.bar(np.arange(n_count_data), count_data, color="#348ABD")
plt.xlabel("Time (days)")
plt.ylabel("count of text-msgs received")
plt.title("Did the user's texting habits change over time?")
plt.xlim(0, n_count_data)

plt.show()
