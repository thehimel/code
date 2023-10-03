"""Author: Himel Das"""

import requests

from utilities.logger import logger


class Country:
    def __init__(self, name: str):
        """Initialise a Country object."""
        self.name = None
        self.currencies = None
        self.region = None
        self.population = None
        self.set_country(name=name)
        self.api_url = "https://restcountries.com/v3.1/name"

    def set_country(self, name: str) -> dict or None:
        response = requests.get(url=f"{self.api_url}/{name}")

        if response.status_code == 200:
            country_data = response.json()[0]
            self.name = country_data["name"]["common"]
            self.currencies = list(country_data["currencies"].keys())
            self.region = country_data["region"]
            self.population = country_data["population"]
        else:
            logger.error(msg=f"Error fetching data from the server. Status code: {response.status_code}")

    def get_country(self):
        data = {
            "name": self.name,
            "currencies": self.currencies,
            "region": self.region,
            "population": self.region,
        }
        return data
