from unittest.mock import mock_open, patch

from src.utils import get_list_from_json_file


def test_get_list_from_json_file_valid_json():
    """Тест с валидным JSON-списком."""
    with patch("os.path.isfile", return_value=True), \
         patch("builtins.open", mock_open(read_data='[{"id": 1}, {"id": 2}]')):
        result = get_list_from_json_file("fake.json")
        assert result == [{"id": 1}, {"id": 2}]


def test_get_list_from_json_file_invalid_json():
    """Тест с не валидным JSON-списком."""
    with patch("os.path.isfile", return_value=True), \
         patch("builtins.open", mock_open(read_data="это не json")):
        result = get_list_from_json_file("fake.json")
        assert result == []


def test_get_list_from_json_file_empty_file():
    """Тест с пустым файлом."""
    with patch("os.path.isfile", return_value=True), \
         patch("builtins.open", mock_open(read_data="")):
        result = get_list_from_json_file("fake.json")
        assert result == []


def test_get_list_from_json_file_not_a_list():
    """JSON — не список."""
    with patch("os.path.isfile", return_value=True), \
         patch("builtins.open", mock_open(read_data='{"error": "not a list"}')):
        result = get_list_from_json_file("fake.json")
        assert result == []


def test_get_list_from_json_file_file_not_found():
    """Файл не существует."""
    with patch("os.path.isfile", return_value=False):
        result = get_list_from_json_file("fake.json")
        assert result == []
