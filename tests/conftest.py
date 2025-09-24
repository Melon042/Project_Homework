import pytest


@pytest.fixture
def sample_card_numbers():
    """Предоставляет тестовые данные номеров карт."""
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


@pytest.fixture
def sample_acc_and_card_nums():
    """Предоставляет тестовые данные номеров счетов и карт."""
    return {
        "card": "1596837868705199",
        "card_with_spaces": "1596 8378 6870 5199",
        "card_with_prefix": "Visa Classic 6831982476737658",
        "account": "64686473678894779589",
        "account_with_prefix": "Счет 64686473678894779589",
        "account_with_prefix_2": "Счет:64686473678894779589",
        "too_short_card": "123456789012345",
        "too_long_card": "12345678901234567",
        "too_short_account": "1234567890123456789",
        "too_long_account": "123456789012345678901",
        "letters": "abc123def",
        "empty": "",
    }


@pytest.fixture
def sample_timestamps():
    return {
        "valid": "2024-03-11T02:26:18.671407",
        "invalid_short_year": "24-03-11T02:26:18",
        "invalid_no_day": "2024-03",
        "invalid_wrong_separators": "2024/03/11T02:26",
        "invalid_letters": "2024-0a-11T02:26:18",
        "empty": "",
        "invalid_none": None,
        "invalid_type_int": 20240311,
    }