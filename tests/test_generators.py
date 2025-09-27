from typing import Generator

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(sample_transactions: list[dict]) -> None:
    """Общий тест функции"""
    # Фильтрация по USD
    usd_gen = filter_by_currency(sample_transactions, "USD")
    usd_list = list(usd_gen)
    assert len(usd_list) == 3
    assert all(transaction["operationAmount"]["currency"]["code"] == "USD" for transaction in usd_list)

    # Фильтрация по RUB
    rub_gen = filter_by_currency(sample_transactions, "RUB")
    rub_list = list(rub_gen)
    assert len(rub_list) == 2
    assert all(transaction["operationAmount"]["currency"]["code"] == "RUB" for transaction in rub_list)

    # Нет таких транзакций
    eur_gen = filter_by_currency(sample_transactions, "EUR")
    assert list(eur_gen) == []

    # Пустой список
    empty_gen = filter_by_currency([], "USD")
    assert list(empty_gen) == []


def test_transaction_descriptions(sample_transactions: list[dict], empty_transactions: list) -> None:
    """Общий тест функции"""
    # Обычный случай
    description_gen = transaction_descriptions(sample_transactions)
    descriptions = list(description_gen)
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    assert descriptions == expected

    # Пустой список
    empty_gen = transaction_descriptions(empty_transactions)
    assert list(empty_gen) == []


@pytest.mark.parametrize(
    "start,end,expected",
    [
        (1, 1, ["0000 0000 0000 0001"]),
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (12345, 12345, ["0000 0000 0001 2345"]),
        (9999999999999999, 9999999999999999, ["9999 9999 9999 9999"]),
    ],
)
def test_card_number_generator_parametrized(start: int, end: int, expected: list[str]) -> None:
    """Параметризованный общий тест функции"""
    result = list(card_number_generator(start, end))
    assert result == expected
