import pandas as pd

dict1 = {
    'Student': ['Aether', 'Freminet', 'Tighnari'],
    'Marks': [90, 99, 69],
    'Sports': ['Adventure', 'Diving', 'Research']
}

#! dataframe me d aur f bada!!!
df = pd.DataFrame(dict1)
print(df)

df = pd.DataFrame(dict1, index=['Mondstadt', 'Fontain', 'Sumeru'])
print(df)


