import pandas as pd

staff = pd.Series([20, 36, 44])
salary = pd.Series([10000, 15000, 20000])

school = {
    'People': staff,
    'Amount': salary
}

df = pd.DataFrame(school)
print(df)

df2 = pd.DataFrame(df)
print(df2)