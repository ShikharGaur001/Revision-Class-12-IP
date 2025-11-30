import pandas as pd
import numpy as np

#* pd.Series(sequence)
#? np.arange(start, stop, step) ---> sequence
sr1 = pd.Series(np.arange(2, 50, 10))

#? np.linspace(start, stop, number of values)
sr2 = pd.Series(np.linspace(24, 64, 6))

#? np.tile(sequence, number of times u want)
sr3 = pd.Series(np.tile([3,5, 'haklaYash'], 3))

print(sr1)
print(sr2)
print(sr3)