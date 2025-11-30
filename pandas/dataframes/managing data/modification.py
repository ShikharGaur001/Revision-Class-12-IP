import pandas as pd

df5 = pd.DataFrame({
    'Population': [10000, 12000, 15000, 20000],
    'Hospitals': [1500, 2000, 1800, 1700],
    'Schools': [7500, 7800, 5600, 6500]
}, index=['Delhi', 'Mumbai', 'Kolkata', 'Chennai'])
print(df5)

#* adding a column

# df5['Density']=[1200,1300,1400,1500]
# print(df5)

# df5['Density']=1200
# print(df5)

# df5.loc[:,'Density'] = [1500,1600,1700,1800]
# print(df5)

#! error pe error pe error pe error jugde sahab!!
#* Adding a row
# df5.at['Banglore',:]=1200
# print(df5)
# df5.loc['Banglore',:] = [25000, 2200, 8000, 1600]   
#  print(df5)  



#* Rename a Row/Columns
# df5.rename(index = {'Delhi':'Haryana','Mumbai':'Pune'}, inplace = 'True')
# print(df5)

# df5.rename(column = {'Population':'Demography','Hospitals':'chikitsalah'}, inplace = 'True')
# print(df5)

df5.rename(index = {'Delhi':'Haryana','Mumbai':'Pune'}, columns = {'Population':'Demography','Hospitals':'chikitsalah'}, inplace = 'True')
print(df5)