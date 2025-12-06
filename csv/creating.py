import pandas as pd
import numpy as np

#* Actors data
data = {
    "Actor": ["Shah Rukh Khan", "Tom Cruise", "Robert Downey Jr.", "Salman Khan", "Keanu Reeves"],
    "Industry": ["Bollywood", "Hollywood", "Hollywood", "Bollywood", "Hollywood"],
    "Hit_Movies": [62, 48, 25, 57, 36],
    "Awards": [21, 42, 53, 14, 28],
    "Active_Years": [32, 40, 35, 35, 38]
}

data2 = {
    "Game": ["GTA V", "Minecraft", "PUBG", "Fortnite", "Elden Ring", "Valorant"],
    "Genre": ["Action", "Sandbox", "Battle Royale", "Battle Royale", "RPG", np.nan],
    "Release_Year": [2013, 2011, 2017, 2017, 2022, 2020],
    "Players_Million": [185, np.nan, 70, 350, 20, 28],
    "Rating": [9.5, 9.0, np.nan, 8.5, 9.8, 8.1]
}

#* Create DataFrame
df = pd.DataFrame(data)
df2 = pd.DataFrame(data2)
# print(df)

#* Save CSV
# df.to_csv(".\\csv\\actors.csv")

#? index ko none kardo warna kand ho jayega...

# df.to_csv(".\\csv\\actors.csv", index=None)

#* sep='' ka use karke seperator change kar sakte...

#* handling NaNas... na_rep = "NULL"

df2.to_csv('.\\csv\\games.csv', sep='|', na_rep='XD')
