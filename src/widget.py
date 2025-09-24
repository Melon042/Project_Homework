from src.masks import get_mask_account_number, get_mask_card_number

def get_mask_account_or_card_num(account_card: str) -> str:
    """Маскирует номер карты или счёта."""
    account_card = str(account_card)

    digits_only = ''.join(char for char in account_card if char.isdigit())

    if len(digits_only) == 16:
        return get_mask_card_number(account_card)
    elif len(digits_only) == 20:
        return get_mask_account_number(account_card)
    else:
        raise ValueError("Некорректный номер карты или счёта")


def get_date(timestamp: str) -> str:
    """Принимает временную метку и возвращает дату в формате 'ДД.ММ.ГГГГ'."""
    timestamp = str(timestamp)

    if len(timestamp) < 10:
        raise ValueError("Некорректный формат даты")

    if timestamp[4] != '-' or timestamp[7] != '-':
        raise ValueError("Некорректный формат даты")

    year = timestamp[0:4]
    month = timestamp[5:7]
    day = timestamp[8:10]

    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        raise ValueError("Некорректный формат даты")

    return f"{day}.{month}.{year}"
