import pandas as pd
import numpy as np

a = [1, 2, 3, 4, 5, 6]

# sr = pd.Series(a)
sr = pd.Series(a, dtype=np.float64)
print(sr)