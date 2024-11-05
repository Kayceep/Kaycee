import pandas as pd
import os 

os.chdir(r"C:\Users\user\OneDrive\Documents")

# number 1
# remove tag columns

df = pd.read_csv("RewardsData.csv")
df.drop(columns = ['Tags'])

# number two
# arrange unique name in columns

#sorted_cities = df['City'].drop_duplicates().sort_values().reset_index(drop = True)
#print(sorted_cities)
df['City'] = df['City'].apply(str)

sorted_cities = df['City'].unique()
sorted_cities.sort()
print(sorted_cities)

# number 3
# correct case for city name 

df['City'] = df['City'].str.title()

# number 4
# correct format for city names

df['City'] = df['City'].replace({'winston-salem': 'Winstom Salem'}, regex= True)

# number 5
df['State'] = df['State'].str.title()