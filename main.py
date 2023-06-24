import csv
from country import Country
from countrycollection import CountryCollection
from game import Game

def load_country_data():
    country_data = []
    with open("data/country_code_namelist.csv", "r") as countries_file:
        reader = csv.reader(countries_file)
        next(reader)  # skip the header row
        for row in reader:
            name, offical_name, code = row
            image_path = f"data/{code.lower()}.jpg"
            country_data.append((name, code, image_path))
            #Country name,Official state name,Alpha-2 code
    return country_data


def main():
    # Load country data (name, code, and image path)
    countries_data = load_country_data()

    # Create Country objects and add them to a CountryCollection
    countries = [Country(name, code, image_path) for name, code, image_path in countries_data]
    country_collection = CountryCollection(countries)

    # Create a Game object and start the game
    game = Game(country_collection)
    game.start_game()

if __name__ == "__main__":
    main()
