import pandas as pd

#  outerdict ki keys ---> dataframe ke columns ki heading...
# inner dict ki keys ---> dataframe ke rows ka naam...
dict2 = {
    'Sales': {'name': 'Aether', 'age': 21, 'sex': 'Male'},
    'Marketing': {'name': 'Kaveh', 'age': 23, 'sex': 'Male'}
}

df = pd.DataFrame(dict2)
# print(df)

#* NaN values in DataFrame

dict3 = {
    'Sales': {'name': 'Aether', 'age': 21, 'sex': 'Male'},
    'Marketing': {'name': 'Kaveh', 'age': 23}
}

df2 = pd.DataFrame(dict3)
# print(df2)



dict4 = {
    'Sales': {'name': 'Aether', 'age': 21, 'sex': 'Male'},
    'Marketing': {'name': 'Kaveh', 'age': 23, 'salary': 7777777}
}

df4 = pd.DataFrame(dict4)
print(df4)