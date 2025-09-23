from src.masks import get_mask_card_number


def test_valid_card_masking(sample_card_numbers):
    """Тестируем правильность маскирования валидного номера карты с использованием фикстуры"""

    card_number_1 = sample_card_numbers["valid_16_digits"]
    card_number_2 = sample_card_numbers["valid_16_digits_with_name"]
    card_number_3 = sample_card_numbers["valid_with_spaces"]
    card_number_4 = sample_card_numbers["valid_16_digits_with_names"]

    result_1 = get_mask_card_number(card_number_1)
    result_2 = get_mask_card_number(card_number_2)
    result_3 = get_mask_card_number(card_number_3)
    result_4 = get_mask_card_number(card_number_4)

    assert result_1 == "1596 83** **** 5199"
    assert result_2 == "Maestro 1596 83** **** 5199"
    assert result_3 == "1596 83** **** 5199"
    assert result_4 == "Visa Classic 6831 98** **** 7658"
