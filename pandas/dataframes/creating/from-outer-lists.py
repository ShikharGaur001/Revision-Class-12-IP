import pandas as pd

dict1 = {'Roll no': 101, 'name': 'Razzi', 'Marks': 78}
dict2 = {'Roll no': 102, 'name': 'Bennett', 'Marks': 52}
dict3 = {'Roll no': 103, 'name': 'Kaveh', 'Marks': 93}

# List of dictionaries
list1 = [dict1, dict2, dict3]

df = pd.DataFrame(list1, index=['student1','student2','student3'])
# print(df)

# List of Lists

lst1 = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

df = pd.DataFrame(lst1)

# Optional labels
index = ['row1', 'row2', 'row3']
column = ['c1', 'c2', 'c3']

df = pd.DataFrame(lst1, index=index, columns=column)
print(df)