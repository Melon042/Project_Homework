import re
from collections import Counter


def filter_by_state(bank_operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Принимает список словарей, фильтрует по указанному значению ключа "state", возвращает отфильтрованный список."""
    filtered_bank_operations = []
    for bank_operation in bank_operations:
        if bank_operation.get("state") == state:
            filtered_bank_operations.append(bank_operation)
    return filtered_bank_operations


def sort_by_date(bank_operations: list[dict], reverse: bool = True) -> list[dict]:
    """Принимает список словарей, сортирует их по дате и возвращает отсортированный список."""
    sorted_bank_operations = sorted(
        bank_operations, key=lambda bank_operation: bank_operation["date"], reverse=reverse
    )
    return sorted_bank_operations


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Принимает список словарей с данными о банковских операциях и строку поиска,
    возвращает список словарей, у которых в описании есть данная строка"""
    result = []

    for operation in data:
        if re.search(search, operation["description"]):
            result.append(operation)
    return result


def count_categories(data: list[dict], categories_list: list) -> dict:
    """Принимает список словарей с данными о банковских операциях и список категорий операций,
    возвращает словарь, в котором ключи — это названия категорий, а значения — это количество
    операций в каждой категории"""
    categories = []

    for operation in data:
        for category in categories_list:
            if category == operation["description"]:
                categories.append(category)
                break

    counted_categories = Counter(categories)

    for category in categories_list:
        if category not in counted_categories.keys():
            counted_categories[category] = 0

    return dict(counted_categories)
