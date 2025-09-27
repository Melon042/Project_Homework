from typing import Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator[dict, None, None]:
    """Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator[str, None, None]:
    """Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """Генерирует номера банковских карт в формате 'XXXX XXXX XXXX XXXX'.
    Генератор должен принимать начальное и конечное значения для генерации диапазона номеров."""
    for num in range(start, stop + 1):
        num_str = str(num)
        while len(num_str) < 16:
            num_str = "0" + num_str

        card_number = []
        for i in range(0, 16, 4):
            card_number.append(num_str[i: i + 4])
        card_number_formated = " ".join(card_number)
        yield card_number_formated
