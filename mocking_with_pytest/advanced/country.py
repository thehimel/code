"""Author: Himel Das"""


class Country:
    def __init__(self, name: str, currencies: [str], region: str, population: int):
        """Initialise a Country object."""
        self.name = name
        self.currencies = currencies
        self.region = region
        self.population = population

    def get_data(self):
        return {
            "name": self.name,
            "currencies": self.currencies,
            "region": self.region,
            "population": self.region,
        }
