import pytest

from src.processing import count_categories, filter_by_state, process_bank_search, sort_by_date


def test_filter_by_state_default(sample_operations: list[dict]) -> None:
    """Тест с параметром 'EXECUTED'."""
    result = filter_by_state(sample_operations)
    assert len(result) == 3


def test_filter_by_state_canceled(sample_operations: list[dict]) -> None:
    """Тест с параметром 'CANCELED'."""
    result = filter_by_state(sample_operations, "CANCELED")
    assert len(result) == 1


@pytest.mark.parametrize(
    "state, expected_count",
    [
        ("EXECUTED", 3),
        ("CANCELED", 1),
        ("PENDING", 1),
        ("EXEC", 0),
        ("", 0),
        ("executed", 0),
    ],
)
def test_filter_by_state_parametrized(sample_operations: list[dict], state: str, expected_count: int) -> None:
    """Тест для разных значений 'state'."""
    result = filter_by_state(sample_operations, state)
    assert len(result) == expected_count


def test_filter_by_state_no_such_state(sample_operations: list[dict]) -> None:
    """Тест когда нет операций с указанным state."""
    result = filter_by_state(sample_operations, "REJECTED")
    assert result == []


def test_filter_by_state_empty_operation_list(empty_operation: list) -> None:
    """Тест пустого списка."""
    result = filter_by_state(empty_operation, "EXECUTED")
    assert result == []


def test_sort_by_date(sample_operations_dates: list[dict]) -> None:
    """Общий тест функции"""
    descending = sort_by_date(sample_operations_dates)
    assert [operation["id"] for operation in descending] == [1, 4, 5, 3, 2]

    ascending = sort_by_date(sample_operations_dates, reverse=False)
    assert [operation["id"] for operation in ascending] == [2, 3, 4, 5, 1]

    with pytest.raises(KeyError):
        sort_by_date([{"id": 1}])


# Тестовые данные
sample_data = [
    {"description": "Перевод"},
    {"description": "Покупка"},
    {"description": "Перевод"},
    {"description": "Оплата"},
]


def test_process_bank_search_found():
    result = process_bank_search(sample_data, "Перевод")
    assert len(result) == 2
    assert result[0]["description"] == "Перевод"


def test_process_bank_search_not_found():
    result = process_bank_search(sample_data, "Зарплата")
    assert result == []


def test_count_categories_basic():
    categories = ["Перевод", "Покупка", "Оплата"]
    result = count_categories(sample_data, categories)
    assert result == {"Перевод": 2, "Покупка": 1, "Оплата": 1}


def test_count_categories_no_match():
    categories = ["Зарплата", "Кэшбэк"]
    result = count_categories(sample_data, categories)
    assert result == {"Зарплата": 0, "Кэшбэк": 0}
