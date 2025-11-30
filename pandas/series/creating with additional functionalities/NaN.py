import pandas as pd
import numpy as np

# apan log jo numpy use karte h paper me... woh purana lol isliye np.NaN aata
# lekin jo abhi isme use kar rhe woh nya h ooohoohhh isliye np.nan use karo
sr = pd.Series([1, 2, 3, 4, np.nan, 6, 7])

print(sr)

# jagah ni milne pr... nan aajata
a={"a":0 ,"b":1 ,"c":2 ,"d":3}
sr2 = pd.Series(a,index=["b","c","d","e","h"])

print(sr2)