"""
Author: Himel Das
"""

import requests
from utilities.logger import logging


def get_country_data(name: str) -> dict or None:
    base_url = "https://restcountries.com/v3.1/name"
    response = requests.get(url=f"{base_url}/{name}")
    reply = {"status_code": response.status_code}

    if response.status_code == 200:
        country_data = response.json()[0]
        reply["data"] = {
            "name": country_data["name"]["common"],
            "currencies": list(country_data["currencies"].keys()),
            "region": country_data["region"],
            "population": country_data["population"],
        }
    return reply


if __name__ == "__main__":
    logging.info(get_country_data(name="usa"))
