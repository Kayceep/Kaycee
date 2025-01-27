import requests
from sqlalchemy import create_engine
import pandas as pd
from bs4 import BeautifulSoup
from sqlalchemy_utils import database_exists, create_database
import psycopg2


uid = 'postgres'
pwd = 'kayceep8'
postgres_url = f'postgresql+psycopg2://{uid}:{pwd}@localhost:5432/Banks'

if not database_exists(postgres_url):
    create_database(postgres_url)
    print('database created')
else:
    print('database exists')

engine = create_engine(postgres_url)


url = ' https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks'

table_name = 'top_17_banks'
csv_path = 'top_17_banks.csv'
df = pd.DataFrame(columns = ['Euro', 'Pound', 'INR'])
count = 0

hmtl_page = requests.get(url).text
retrieved_data = BeautifulSoup(hmtl_page, 'html.parser')

tables = retrieved_data.find_all('tbody')
rows = tables[0].find_all('tr')


USD_to_EUR = 0.93
USD_to_GBP = 0.8  
USD_to_INR = 82.95
for row in rows:
    if count < 17:  # count starts at 0 and will stop at 16 (indexing)
        col = row.find_all('td')
        if len(col) != 0:  # if the columns are not empty

            
            bank_name = col[1].text
            dollar_text = col[2].text.strip()  # Convert the parsed content to float
            dollar_value = float(dollar_text) 

            # Convert the dollar value into other currencies
            Euro = round(dollar_value * USD_to_EUR, 2)
            Pound = round(dollar_value * USD_to_GBP, 2)
            INR = round(dollar_value * USD_to_INR, 2)

    
            data_dict = {
                'bank': bank_name,
                'Euro': Euro,
                'Pound': Pound,
                'INR': INR
            }

    
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)  # Adds the new dataframe to the existing dataframe

    else:
        break

df.to_sql(table_name, engine, if_exists='replace')  # Transfer the data to the database
print('Successfully transferred to the database')
df.to_csv(csv_path)  # Save the data to a CSV file
print('Saved to CSV')