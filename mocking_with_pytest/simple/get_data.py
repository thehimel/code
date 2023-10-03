"""
Author: Himel Das
"""

import requests

from utilities.logger import logger


def get_country(name: str) -> dict:
    base_url = "https://restcountries.com/v3.1/name"
    response = requests.get(url=f"{base_url}/{name}")

    if response.status_code == 200:
        country_data = response.json()[0]
        reply = {
            "success": True,
            "body": {
                "name": country_data["name"]["common"],
                "currencies": list(country_data["currencies"].keys()),
                "region": country_data["region"],
                "population": country_data["population"],
            },
        }
    else:
        reply = {"success": False, "body": response.text}

    return reply


if __name__ == "__main__":
    logger.info(get_country(name="usa"))
