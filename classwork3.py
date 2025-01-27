import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import os

# Load the CSV file
data_path = os.chdir(r'c:/Users/user/Documents')
df = pd.read_csv('RewardsData.csv')

# Step a: Remove the 'Tags' column
if 'Tags' in df.columns:
    df = df.drop(columns=['Tags'])

# Step b: Arrange in alphabetical order all unique values in the 'City' column
unique_cities = sorted(df['City'].dropna().unique())

# Step c: Replace all formats of Winston-salem with "Winston-Salem"
df['City'] = df['City'].str.replace(r'(?i)winston[-\s]*salem', 'Winston-Salem', regex=True)

# Step d: Proper case for city names
df['City'] = df['City'].str.title()

# Repeat steps a-d for 'State' column
df['State'] = df['State'].str.title()

# Step f: Replace state abbreviations with full names
us_state_abbrev = {  # Dictionary of state abbreviations
                   
                          
    'AL': 'Alabama','Al':"Alabama", 'AK': 'Alaska', 'AZ': 'Arizona', "Az":"Arizona",'AR': 'Arkansas', 
    'CA': 'California', "Ca":"California",'CO': 'Colorado', "Co":"Colorado",'CT': 'Connecticut',
    "Ct":"Connecticut", 'DE': 'Delaware', 'FL': 'Florida',"Fl":"Florida", 'GA': 'Georgia', "Ga":"Georgia",
    'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', "Il":"Illionois", 'IN': 'Indiana', 'IA': 'Iowa', 
    'KS': 'Kansas', 'KY': 'Kentucky',"Ky":"Kentucky",'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland', 
    "Md":"Maryland", "MA": 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota','Mn':'Minnesota', 
    'MS': 'Mississippi','Ms':'Mississippi', 'MO': 'Missouri', 'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 
    'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'NY': 'New York',"Ny":"New York",
    'Nc':'North Carolina', 'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio', "Oh":"Ohio",
    'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania',"Pa":"Pennysylvania", 'RI': 'Rhode Island', 
    'SC': 'South Carolina', "Sc":"South Carolina", 'SD': 'South Dakota', 'TN': 'Tennessee','Tn':'Tennessee',
    'TX': 'Texas', "Tx":"Texas", 'UT': 'Utah', 'VT': 'Vermont', 'VA': 'Virginia', 'Va':'Virginia', 'WA': 'Washington', 
    'WV': 'West Virginia', 'WI': 'Wisconsin', "Wi":"Wisconsin",'WY': 'Wyoming'
}

abbrev_to_state = {v: k for k, v in us_state_abbrev.items()}
df['State'] = df['State'].replace(us_state_abbrev)

# Step g: Fill NaN in 'State' with state names in alphabetical order
states = sorted(us_state_abbrev.keys())
nan_indices = df[df['State'].isna()].index
for i, idx in enumerate(nan_indices):
    df.at[idx, 'State'] = states[i % len(states)]

# Step h: Truncate ZIP codes longer than 5 digits
df['Zip'] = df['Zip'].astype(str).str[:5]

# Step i: Drop rows with ZIP codes less than 5 digits
df = df[df['Zip'].str.len() == 5]

# Step j: Convert 'Birthdate' to datetime
df['Birthdate'] = pd.to_datetime(df['Birthdate'], errors='coerce').dt.date

# Step k-m: Save the resulting DataFrame to a PostgreSQL database
postgres_user = 'postgres'
postgres_password = 'kayceep8'
postgres_host = 'localhost'
postgres_port = '5432'
postgres_db = 'RewardsData'
db_url = f'postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}'

engine = create_engine(db_url)

if not database_exists(db_url):
    create_database(db_url)

table_name = 'CleanRewardsData'
df.to_sql(table_name, con=engine, if_exists='replace', index=False)

print(f"Data processed and saved to PostgreSQL database '{postgres_db}' in table '{table_name}'!")