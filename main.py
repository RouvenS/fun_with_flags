import pandas as pd
import random
import tkinter as tk



#read country code csv file
countries_df = pd.read_csv('country_code_namelist.csv')

wrong_countries = []


#function that picks random countries
def pick_coutries():
    wrong_countries = []
    right_country = ""
    while len(wrong_countries) < 3:
        wrong_country = random.choice(countries_df['Country name'].tolist())
        if wrong_country not in wrong_countries:
            wrong_countries.append(wrong_country)
    while True:
        right_country = random.choice(countries_df['Country name'].tolist())
        if right_country not in wrong_countries:
            break

    return wrong_countries, right_country


# Call the function and assign its output to variables
wrong_countries, right_country = pick_coutries()


"""
#GUI
"""

root = tk.Tk()
root.geometry("800x500")
root.title("Fun with Flags!")

country1 = tk.Button(root, text=wrong_countries[0], width=20, height=4)
country1.pack()
country2 = tk.Button(root, text=wrong_countries[1], width=20, height=4)
country2.pack()
country3 = tk.Button(root, text=wrong_countries[2], width=20, height=4)
country3.pack()
country4 = tk.Button(root, text=right_country, width=20, height=4)
country4.pack()
root.mainloop()