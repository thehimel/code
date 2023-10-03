"""
Author: Himel Das
"""

import pytest

from mocking_with_pytest.advanced.get_data import get_countries_with_population

test_data = [
    (
        ["usa", "canada", "australia"],
        [
            {"name": "United States", "population": 329484123},
            {"name": "Canada", "population": 38005238},
            {"name": "Australia", "population": 25687041},
        ],
    ),
    (
        ["australia", "unknown"],
        [
            {"name": "Australia", "population": 25687041},
        ],
    ),
]


@pytest.mark.parametrize("country_names, expected", test_data)
def test_get_countries_with_population(country_names, expected, mocker):
    mocked_response = {
        "usa": {
            "success": True,
            "body": {
                "name": "United States",
                "currencies": ["USD"],
                "region": "Americas",
                "population": 329484123,
            },
        },
        "canada": {
            "success": True,
            "body": {
                "name": "Canada",
                "currencies": ["CAD"],
                "region": "Americas",
                "population": 38005238,
            },
        },
        "australia": {
            "success": True,
            "body": {
                "name": "Australia",
                "currencies": ["AUD"],
                "region": "Oceania",
                "population": 25687041,
            },
        },
        "unknown": {"success": False, "body": {"status": 404, "message": "Not Found"}},
    }
    mocker.patch(
        target="mocking_with_pytest.advanced.get_data.get_country",
        side_effect=lambda *args, **kwargs: mocked_response[kwargs["country_name"]],
    )
    assert get_countries_with_population(country_names=country_names) == expected


if __name__ == "__main__":
    pytest.main()
