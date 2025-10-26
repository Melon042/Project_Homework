import json
import os


def get_list_from_json_file(path_to_json_file):
    """Принимает путь до JSON-файла и возвращает список.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    try:
        if not os.path.isfile(path_to_json_file):
            return []
        with open(path_to_json_file, "r", encoding="utf-8") as file:
            data_json = file.read().strip()
        if not data_json:
            return []
        data = json.loads(data_json)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, FileNotFoundError):
        return []
