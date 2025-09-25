import pytest

from src.masks import get_mask_account_number, get_mask_card_number


def test_get_mask_card_number(sample_card_numbers: dict) -> None:
    """Общий тест функции."""

    card_number_1 = sample_card_numbers["valid_16_digits"]
    card_number_2 = sample_card_numbers["valid_with_spaces"]
    card_number_3 = sample_card_numbers["valid_16_digits_with_name"]
    card_number_4 = sample_card_numbers["valid_16_digits_with_names"]
    card_number_5 = sample_card_numbers["account"]
    card_number_6 = sample_card_numbers["too_short"]
    card_number_7 = sample_card_numbers["too_long"]
    card_number_8 = sample_card_numbers["empty_string"]
    card_number_9 = sample_card_numbers["with_letters"]
    card_number_10 = sample_card_numbers["wrong_data_type_int"]

    result_1 = get_mask_card_number(card_number_1)
    result_2 = get_mask_card_number(card_number_2)
    result_3 = get_mask_card_number(card_number_3)
    result_4 = get_mask_card_number(card_number_4)
    result_5 = get_mask_card_number(card_number_10)

    assert result_1 == "1596 83** **** 5199"
    assert result_2 == "1596 83** **** 5199"
    assert result_3 == "Maestro 1596 83** **** 5199"
    assert result_4 == "Visa Classic 6831 98** **** 7658"
    assert result_5 == "1596 83** **** 5199"

    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр"):
        get_mask_card_number(card_number_5)
    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр"):
        get_mask_card_number(card_number_6)
    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр"):
        get_mask_card_number(card_number_7)
    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр"):
        get_mask_card_number(card_number_8)
    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр"):
        get_mask_card_number(card_number_9)


@pytest.mark.parametrize(
    "account_num, is_valid",
    [
        ("64686473678894779589", True),
        ("Счет 64686473678894779589", True),
        ("Счет:64686473678894779589", True),
        ("Счет: 64686473678894779589", True),
        (64686473678894779589, True),
        ("", False),
        ("6468647367889477958", False),
        ("646864736788947795899", False),
        ("6686a767b8947c589", False),
    ],
)
def test_get_mask_account_number(account_num: str, is_valid: bool) -> None:
    """Общий тест функции."""

    if is_valid:
        result = get_mask_account_number(account_num)
        assert result == "Счет **9589" or "Счет: **9589" or "**9589"
    else:
        with pytest.raises(ValueError):
            get_mask_account_number(account_num)
