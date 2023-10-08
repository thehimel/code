"""
Author: Himel Das

This is an example of inheritance for the scenario when you want to extend the functionality of parent class.

In the child class, if the __init__() method is not define, directly the constructor of the parent class is invoked.
However, in that case, we do not have the opportunity to add any extra attribute to the class.
If we define the __init__() method in child class and do not define the super() method, we are directly overriding
the __init__() method of the parent class.
However, in the case when we do not override the constructor of the parent class and just want to add some attributes to
the child class, we can do that but adding super() method and passing the parent attributes. Here we are calling the
constructor of the parent class using super(). The concept of method overriding is referred as polymorphism.
"""
from oop.classes.country import Country as CountryMain
from utilities.logger import logging


class Country(CountryMain):
    def __init__(self, name: str, continent: str, currency: str):
        super().__init__(name=name, continent=continent, currency=currency)
        self.continents = [
            "Africa",
            "Antarctica",
            "Asia",
            "Europe",
            "North America",
            "Australia (Oceania)",
            "South America",
        ]

    def get_continents(self):
        return self.continents

    def __str__(self):
        """Method overriding."""
        return f"{self.name} is situated in the continent {self.continent} and their currency is {self.get_currency()}."


def handler():
    country = Country(name="USA", continent="North America", currency="USD")
    logging.info(country.get_currency())  # Invoking method from the parent class as part of the instance.
    logging.info(country.get_continents())  # Invoking method from the child class as part of the instance.
    logging.info(country)


if __name__ == "__main__":
    handler()
