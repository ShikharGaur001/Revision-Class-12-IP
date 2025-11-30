import pandas as pd
import numpy as np

a = [1, 2, 3, 4, 5, 6]

# dictionary ki wajah se apne aap NaN aajata
# pr... normally use karoge toh pachitaoge
#* sr = pd.Series(a, index=['a', 'b', 'c', 'd', 'e', 'f'])
sr = pd.Series(a, index=[haklaYash for haklaYash in 'abcdef'])

print(sr)