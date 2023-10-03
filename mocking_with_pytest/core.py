"""Author: Himel Das"""

from mocking_with_pytest.country import Country
from mocking_with_pytest.get_data import get_countries_with_population
from mocking_with_pytest.get_data import get_country
from utilities.logger import logger


def main():
    country_name = "usa"
    response = get_country(country_name=country_name)
    data = response["body"]

    if response["success"]:
        country = Country(
            name=data["name"],
            currencies=data["currencies"],
            region=data["region"],
            population=data["population"],
        )
        logger.info(f"Country: {country.to_dict()}")
    else:
        logger.error(
            msg=f"Error fetching data for the country '{country_name}': {data}."
        )

    countries = ["usa", "canada", "australia", "unknown"]
    logger.info(
        msg=f"Countries with population: {get_countries_with_population(country_names=countries)}"
    )


if __name__ == "__main__":
    main()
