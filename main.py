import pandas as pd
import random

#read country code csv file
countries_df = pd.read_csv('country_code_namelist.csv')

#function that picks a random country
def right_country():
    country = random.choice(countries_df['Country name'].tolist())
    return country

def wrong_countries():
    wrong_countries = []
    while len(wrong_countries) < 3:
        wrong_country = random.choice(countries_df['Country name'].tolist())
        if wrong_country not in wrong_countries:
            wrong_countries.append(wrong_country)
    return wrong_countries

print(right_country() + '\n' + str(wrong_countries()))
