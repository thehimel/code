"""
Author: Himel Das

In mocking, we mock the behaviour of the part that initiates an API call like 'requests.get' in this case.
Let's call 'requests.get' as the 'mocking target' for future reference. While constructing the mocked
response, we need to see what components of the mocking target we are using in the function that we are going to
test. In this example, we are using the components 'status_code' and 'json'. As json() is a method, return_value is
needed.As status_code is a variable, no return_value is needed. Then we patch 'requests.get' with the mocked
response as the return value for this mocking target. It means, wherever 'requests.get' is used, it will return the
specified mocked response. It's important to include the patch section before the assertion section.
"""

from unittest.mock import Mock

import pytest

from mocking_with_pytest.simple.get_data import get_country


def test_get_country_data_positive(mocker):
    # Construct a mock response with the components of the mocking target.
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [
        {
            "name": {"common": "United States"},
            "currencies": {"USD": {"name": "United States dollar", "symbol": "$"}},
            "region": "Americas",
            "population": 329484123,
        }
    ]

    # Patch the target with the mocked response.
    mocker.patch(target="requests.get", return_value=mock_response)

    expected = {
        "status_code": 200,
        "data": {
            "name": "United States",
            "currencies": ["USD"],
            "region": "Americas",
            "population": 329484123,
        },
    }
    assert get_country(name="canada") == expected


def test_get_country_data_negative(mocker):
    # Construct a mock response with the components that are used in the entity to be mocked.
    mock_response = Mock(status_code=500)

    # Patch the target with the mocked response.
    mocker.patch(target="requests.get", return_value=mock_response)

    expected = {"status_code": 500}
    response = get_country(name="canada")
    assert expected == response
    assert "data" not in response


if __name__ == "__main__":
    pytest.main()
