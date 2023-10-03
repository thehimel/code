"""Author: Himel Das"""

from mocking_with_pytest.advanced.country import Country
from mocking_with_pytest.simple.get_data import get_country
from utilities.logger import logger


def main():
    name = "usa"
    response = get_country(name=name)
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
        logger.error(msg=f"Error fetching data for the country '{name}': {data}.")


if __name__ == "__main__":
    main()
