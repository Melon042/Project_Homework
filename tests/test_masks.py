import pytest
from src.masks import get_mask_card_number


def test_get_mask_card_number(sample_card_numbers):
    """Полный тест функции со всеми вариантами вводных данных"""

    card_number_1 = sample_card_numbers["valid_16_digits"]
    card_number_2 = sample_card_numbers["valid_with_spaces"]
    card_number_3 = sample_card_numbers["valid_16_digits_with_name"]
    card_number_4 = sample_card_numbers["valid_16_digits_with_names"]
    card_number_5 = sample_card_numbers["account"]
    card_number_6 = sample_card_numbers["too_short"]
    card_number_7 = sample_card_numbers["too_long"]
    card_number_8 = sample_card_numbers["empty_string"]
    card_number_9 = sample_card_numbers["with_letters"]

    result_1 = get_mask_card_number(card_number_1)
    result_2 = get_mask_card_number(card_number_2)
    result_3 = get_mask_card_number(card_number_3)
    result_4 = get_mask_card_number(card_number_4)

    assert result_1 == "1596 83** **** 5199"
    assert result_2 == "1596 83** **** 5199"
    assert result_3 == "Maestro 1596 83** **** 5199"
    assert result_4 == "Visa Classic 6831 98** **** 7658"

    with pytest.raises(ValueError, match='Номер карты должен содержать 16 цифр'):
        get_mask_card_number(card_number_5)
    with pytest.raises(ValueError, match='Номер карты должен содержать 16 цифр'):
        get_mask_card_number(card_number_6)
    with pytest.raises(ValueError, match='Номер карты должен содержать 16 цифр'):
        get_mask_card_number(card_number_7)
    with pytest.raises(ValueError, match='Некорректный номер карты'):
        get_mask_card_number(card_number_8)
    with pytest.raises(ValueError, match='Некорректный номер карты'):
        get_mask_card_number(card_number_9)
