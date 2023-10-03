"""
Author: Himel Das
"""

import requests

from utilities.logger import logger


def get_country(country_name: str) -> dict:
    api_url = "https://restcountries.com/v3.1/name"
    response = requests.get(url=f"{api_url}/{country_name}")

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


def get_countries_with_population(country_names: [str]) -> list:
    res = []
    for country_name in country_names:
        response = get_country(country_name=country_name)
        data = response["body"]

        if response["success"]:
            country = {
                "name": data["name"],
                "population": data["population"],
            }
            res.append(country)
    return res


if __name__ == "__main__":
    logger.info(get_country(country_name="usa"))
    countries = ["usa", "canada", "australia", "unknown"]
    logger.info(
        msg=f"Countries with population: {get_countries_with_population(country_names=countries)}"
    )
