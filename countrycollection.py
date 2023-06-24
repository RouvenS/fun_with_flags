class CountryCollection:
    def __init__(self, countries):
        self.countries = countries

    def get_random_country(self):
        import random
        return random.choice(self.countries)