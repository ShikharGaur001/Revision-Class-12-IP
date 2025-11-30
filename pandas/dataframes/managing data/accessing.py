import pandas as pd

df5 = pd.DataFrame({
    'Population': [10000, 12000, 15000, 20000],
    'Hospitals': [1500, 2000, 1800, 1700],
    'Schools': [7500, 7800, 5600, 6500]
}, index=['Delhi', 'Mumbai', 'Kolkata', 'Chennai'])

print(df5)
print(df5['Population'])
print(df5.Population)
print(df5[[ 'Hospitals']]) 

# loc and iloc

print(df5.loc['Delhi','Population'])
print(df5.iloc[0:2,1:2])

#Accessing individual element

print(df5.Population['Chennai'])

# at , iat
print(df5.at['Chennai','Schools'])
print(df5.iat[3,2])