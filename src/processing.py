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
