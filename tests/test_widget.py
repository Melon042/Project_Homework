import pytest

from src.widget import get_date, get_mask_account_or_card_num


def test_get_mask_account_or_card_num(sample_acc_and_card_nums: dict) -> None:
    """Общий тест функции."""

    assert get_mask_account_or_card_num(sample_acc_and_card_nums["card"]) == "1596 83** **** 5199"
    assert get_mask_account_or_card_num(sample_acc_and_card_nums["card_with_spaces"]) == "1596 83** **** 5199"
    assert (
        get_mask_account_or_card_num(sample_acc_and_card_nums["card_with_prefix"])
        == "Visa Classic 6831 98** **** 7658"
    )
    assert get_mask_account_or_card_num(sample_acc_and_card_nums["account"]) == "**9589"
    assert get_mask_account_or_card_num(sample_acc_and_card_nums["account_with_prefix"]) == "Счет **9589"
    assert get_mask_account_or_card_num(sample_acc_and_card_nums["account_with_prefix_2"]) == "Счет: **9589"

    invalid_cases = ["too_short_card", "too_long_card", "too_short_account", "too_long_account", "letters", "empty"]

    for case in invalid_cases:
        with pytest.raises(ValueError, match="Некорректный номер карты или счёта"):
            get_mask_account_or_card_num(sample_acc_and_card_nums[case])


def test_get_date(sample_timestamps: dict) -> None:
    """Общий тест функции."""

    assert get_date(sample_timestamps["valid"]) == "11.03.2024"

    invalid_cases = [
        "invalid_short_year",
        "invalid_no_day",
        "invalid_wrong_separators",
        "invalid_letters",
        "empty",
        "invalid_none",
        "invalid_type_int",
    ]

    for case in invalid_cases:
        with pytest.raises(ValueError, match="Некорректный формат даты"):
            get_date(sample_timestamps[case])
