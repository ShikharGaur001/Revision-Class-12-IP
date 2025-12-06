import numpy as np
import matplotlib.pyplot as plt
mu = 100
sigma = 15
x = mu + sigma*np.random.randn(10000)
y = mu + 30*np.random.randn(10000)
plt.hist([x, y], bins = 100, histtype='barstacked')
plt.title('Research data Histogram')
# saving figure
plt.savefig('.\\pyplot\\histogram\\random.png')
plt.show()