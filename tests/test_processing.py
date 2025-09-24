import pytest
from src.processing import filter_by_state, sort_by_date

def test_filter_by_state_default(sample_operations):
    """Тест с параметром 'EXECUTED'."""
    result = filter_by_state(sample_operations)
    assert len(result) == 3


def test_filter_by_state_canceled(sample_operations):
    """Тест с параметром 'CANCELED'."""
    result = filter_by_state(sample_operations, "CANCELED")
    assert len(result) == 1


@pytest.mark.parametrize("state, expected_count", [
    ("EXECUTED", 3),
    ("CANCELED", 1),
    ("PENDING", 1),
    ("EXEC", 0),
    ("", 0),
    ("executed", 0),
])

def test_filter_by_state_parametrized(sample_operations, state, expected_count):
    """Тест для разных значений 'state'."""
    result = filter_by_state(sample_operations, state)
    assert len(result) == expected_count


def test_filter_by_state_no_such_state(sample_operations):
    """Тест когда нет операций с указанным state."""
    result = filter_by_state(sample_operations, "REJECTED")
    assert result == []


def test_filter_by_state_empty_operation_list(empty_operation):
    """Тест пустого списка."""
    result = filter_by_state(empty_operation, "EXECUTED")
    assert result == []


def test_sort_by_date(sample_operations_dates):
    """Общий тест функции"""
    descending = sort_by_date(sample_operations_dates)
    assert [operation["id"] for operation in descending] == [1, 4, 5, 3, 2]

    ascending = sort_by_date(sample_operations_dates, reverse=False)
    assert [operation["id"] for operation in ascending] == [2, 3, 4, 5, 1]

    with pytest.raises(KeyError):
        sort_by_date([{"id": 1}])