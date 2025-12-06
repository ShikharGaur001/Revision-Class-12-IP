# table se csv karta h 🙃😊

import pandas as pd
# df=pd.read_csv('.\\csv\\cricket.csv')

# print(df)

#* columns change karne ke liye 'name' use karen...
#? names use karke column change nahi hue pr ek nya columns ban gye :(

# df=pd.read_csv('.\\csv\\cricket.csv', names=['Cricketer', 'Role', 'Matches', 'Score', 'Emotional Damage'])

#* ab header ko none karke hi dekh lete >.<...
#? ye banda hamare names ni dene pr... heading 0, 1, 2, ... bana deta h :O

# df=pd.read_csv('.\\csv\\cricket.csv', header=None)

#* skiprows!!!
#! skiprows me direct value diya toh jitna value.. utne rows gayab :O but but but... agar sequence[] dala toh woh indexing chalu ;_;
#? agar names h toh unhe kuch bhi ni hoga :D

# df=pd.read_csv('.\\csv\\cricket.csv',names=['Cricketer', 'Role', 'Matches', 'Score', 'Emotional Damage'], skiprows=1)

#* index_col isse index ki jagah naam diya hua column aajata h

# df=pd.read_csv('.\\csv\\cricket.csv', index_col='Player')

#* name ke saath

# df=pd.read_csv('.\\csv\\cricket.csv',names=['Cricketer', 'Role', 'Matches', 'Score', 'Emotional Damage'], index_col='Matches', skiprows=1)

#* nrows = <n> jitna n... utna hi data show hoga matlab rows...
#! iski value sequence ni hoti.. value must be integer >=0

# df=pd.read_csv('.\\csv\\cricket.csv',names=['Cricketer', 'Role', 'Matches', 'Score', 'Emotional Damage'], index_col='Matches', skiprows=1, nrows=3)
# print(df)

#* sep = ''... jo seperation ke liye symbol csv me use kiya h... use hi idhar sep = '' me use karna h...

df2 = pd.read_csv('.\\csv\\movies.csv', sep=';')
print(df2)