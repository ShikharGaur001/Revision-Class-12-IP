import pandas as pd

dfn = pd.DataFrame({
    'Marketing': [25, 'Neha', 'Female'],
    'Sales': [24, 'Rohit', 'Male']
}, index=['age', 'name', 'sex'])

print(dfn)

print(dfn.index)
print(dfn.columns)
print(dfn.axes)
print(dfn.dtypes)
print(dfn.size)
print(dfn.shape)
print(dfn.ndim)
print(dfn.empty)
print(len(dfn))
print(dfn.T)
print(dfn.values)