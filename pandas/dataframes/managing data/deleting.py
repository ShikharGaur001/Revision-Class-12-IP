import pandas as pd

df5 = pd.DataFrame({
    'Population': [10000, 12000, 15000, 20000],
    'Hospitals': [1500, 2000, 1800, 1700],
    'Schools': [7500, 7800, 5600, 6500]
}, index=['Delhi', 'Mumbai', 'Kolkata', 'Chennai'])
print(df5)


# drop
a = df5.drop(['Population','Hospitals'],axis = 1)
b =df5.drop(['Mumbai','Chennai'],axis = 0)


print(a)
print(b)

# del

del df5['Schools']
print(df5)  