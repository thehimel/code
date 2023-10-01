from unittest.mock import Mock
from mocking_with_pytest.get_data import get_country_data


def test_get_country_data(mocker):
    """
    In mocking, we mock the behaviour of the part that initiates an API call like 'requests.get' in this case.
    Let's call 'requests.get' as the 'mocking entity' for future reference. While constructing the mocked
    response, we need to see what components of the mocking entity we are using in the function that we are going to
    test. In this example, we are using the components 'status_code' and 'json'. As json() is a method, return_value is
    needed.As status_code is a variable, no return_value is needed. Then we patch 'requests.get' with the mocked
    response as the return value for this mocking entity. It means, wherever 'requests.get' is used, it will return the
    specified mocked response. It's important to include the patch section before the assertion section.
    """
    # Construct a mock response with the components that are used in the entity to be mocked.
    mock_response = Mock()
    status_code_ok = 200
    mock_response.status_code = status_code_ok
    mock_response.json.return_value = [
        {
            "name": {"common": "United States"},
            "currencies": {"USD": {"name": "United States dollar", "symbol": "$"}},
            "region": "Americas",
            "population": 329484123,
        }
    ]

    # Patch the entity 'requests.get' with the mocked response.
    mocker.patch("requests.get", return_value=mock_response)

    expected = {
        "status_code": status_code_ok,
        "data": {
            "name": "United States",
            "currencies": ["USD"],
            "region": "Americas",
            "population": 329484123,
        }
    }
    assert get_country_data(name="canada") == expected
