import pytest


@pytest.fixture
def sample_card_numbers() -> dict:
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
        "wrong_data_type_int": 1596837868705199,
    }


@pytest.fixture
def sample_acc_and_card_nums() -> dict:
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
def sample_timestamps() -> dict:
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


@pytest.fixture
def sample_operations() -> list[dict]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T00:00:00"},
        {"id": 2, "state": "EXECUTED", "date": "2023-01-02T00:00:00"},
        {"id": 3, "state": "CANCELED", "date": "2023-01-03T00:00:00"},
        {"id": 4, "state": "PENDING", "date": "2023-01-04T00:00:00"},
        {"id": 5, "date": "2023-01-05T00:00:00"},
        {"id": 6, "state": "EXECUTED", "date": "2023-01-06T00:00:00"},
    ]


@pytest.fixture
def empty_operation() -> list:
    return []


@pytest.fixture
def sample_operations_dates() -> list[dict]:
    return [
        {"id": 1, "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "date": "2018-09-12T21:27:25.241689"},
        {"id": 4, "date": "2018-10-14T08:21:33.419441"},
        {"id": 5, "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def empty_transactions():
    return []
