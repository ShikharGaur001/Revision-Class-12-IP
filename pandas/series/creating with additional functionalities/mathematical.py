import pandas as pd
import numpy as np

# r = np.arange(1, 6, 1)
# a=[1,2,3,4,5]

# sr = pd.Series(index = r, data = r * 2)
# sr = pd.Series(data = (2 * a))
# print(sr)

section = ['a', 'b', 'c', 'd', 'e']
contri1=np.array([6700,5600,5000,5200,np.nan])
s12=pd.Series(data=contri1*2,index=section,dtype=np.float64)
print(s12)