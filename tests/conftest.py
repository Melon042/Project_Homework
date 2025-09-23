import pytest


@pytest.fixture
def sample_card_numbers():
    """Фикстура предоставляет тестовые данные номеров карт"""
    return {
        "valid_16_digits": "1596837868705199",
        "valid_16_digits_with_name": "Maestro 1596837868705199",
        "valid_16_digits_with_names": "Visa Classic 6831982476737658",
        "valid_with_spaces": "1596 8378 6870 5199",
        "account": "Счет 64686473678894779589",
        "too_short": "159683786870519",
        "too_long": "15968378687051999",
        "empty_string": "",
        "with_letters": "159a878c87051e9q",
        "wrong_data_type_int": 1596837868705199
    }
