import matplotlib.pyplot as plt
import numpy as np

fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
sqfib = np.sqrt(fib)

plt.plot(range(1, 11), fib, "co", markersize=5, markeredgecolor='red', ls="-")
plt.plot(range(1, 11), sqfib, "k+", markersize=7, markeredgecolor='red', ls="-")
plt.show()