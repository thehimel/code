"""Author: Himel Das"""

import re
from utilities.logger import logger


class Country:
    def __init__(self, name: str, continent: str, currency: str):
        """Initialise a Country object."""
        self._currency = None  # Single underscore prefix is for a private attribute
        self.set_currency(currency=currency)
        self.name = name
        self.continent = continent

    def get_currency(self):
        """Getter method for currency."""
        return self._currency

    def set_currency(self, currency):
        """Setter method for currency."""
        if not self.is_valid_currency(currency=currency):
            raise ValueError("Currency should be a 3 characters long alphabetic string.")
        self._currency = currency

    @staticmethod
    def is_valid_currency(currency):
        """Check if the currency is valid."""
        pattern = r'^[a-zA-Z]{3}$'  # Regex pattern to match 3-character alphabetic string.
        return re.match(pattern=pattern, string=currency)

    def __str__(self):
        """String representation of the instance."""
        return f"Name: {self.name}, Continent: {self.continent}, Currency: {self.get_currency()}"


def handler():
    """This is important because if we define something inside '__main__', it is accessible all over the file, and that
     can interfere with variables and methods of other entities."""
    country = Country(name="USA", continent="North America", currency="USD")  # Create an instance of the class
    logger.info(country)


if __name__ == "__main__":
    """Main function of the script."""
    handler()
