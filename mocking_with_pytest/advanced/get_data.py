from mocking_with_pytest.simple.get_data import get_country


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
