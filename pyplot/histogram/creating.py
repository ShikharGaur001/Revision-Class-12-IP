import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)  # 1000 values from a normal distribution

plt.hist(data)
plt.title("Basic Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
