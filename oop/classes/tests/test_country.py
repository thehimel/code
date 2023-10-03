"""Author: Himel Das"""

import pytest

from oop.classes.country import Country

test_data = {
    "valid": [
        ("USA", "North America", "USD"),
        ("CA", "North America", "CAD"),
    ],
    "invalid": [
        ("AU", "Oceania", "INVALID_CURRENCY"),
        ("MX", "North America", "INVALID_001"),
    ],
}


@pytest.mark.parametrize("name, continent, currency", test_data["valid"])
def test_country_creation(name, continent, currency):
    """Positive path testing for the creation of Country instance."""
    country = Country(name=name, continent=continent, currency=currency)
    assert country.name == name
    assert country.get_currency() == currency


@pytest.mark.parametrize("name, continent, currency", test_data["invalid"])
def test_country_creation_invalid(name, continent, currency):
    """Negative path testing for the creation of Country instance."""
    with pytest.raises(ValueError):
        Country(name=name, continent=continent, currency=currency)


if __name__ == "__main__":
    """Main function to run the tests."""
    pytest.main()
