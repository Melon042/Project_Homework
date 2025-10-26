import json
import logging
import os

logger = logging.getLogger('utils_logger')
file_handler = logging.FileHandler('logs/utils.log', mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_list_from_json_file(path_to_json_file):
    """Принимает путь до JSON-файла и возвращает список.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    logger.info('Вызов функции "get_list_from_json_file".')

    try:
        if not os.path.isfile(path_to_json_file):
            logger.warning('Файл не найден, возвращен пустой список.')
            return []
        with open(path_to_json_file, "r", encoding="utf-8") as file:
            data_json = file.read().strip()
        if not data_json:
            logger.warning('Файл пуст, возвращен пустой список.')
            return []
        data = json.loads(data_json)
        if isinstance(data, list):
            logger.info('Файл успешно прочитан, возвращён список.')
            return data
        else:
            logger.warning('Файл содержит не список, возвращён пустой список.')
            return []
    except (json.JSONDecodeError, FileNotFoundError) as e:
        logger.error(f'Возникла ошибка: {e}, возвращен пустой список.')
        return []
