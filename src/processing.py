def filter_by_state(list_dict: list, state='EXECUTED') -> list:
    """Функция принимает список словарей, фильтрует их по указанному значению ключа 'state' и возвращает отфильтрованный список."""
    list_filtered = []
    for item in list_dict:
        if item.get('state') == state:
            list_filtered.append(item)
    return list_filtered


def sort_by_date(list_dict: list, reverse: bool = True) -> list:
    """Функция принимает список словарей, сортирует их по дате и возвращает отсортированный список"""
    list_sorted = sorted(list_dict, key=lambda x: x['date'], reverse=reverse)
    return list_sorted
