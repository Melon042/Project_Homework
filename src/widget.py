from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Маскирует данные карты или счёта"""
    account_card_splited = account_card.split()
    counter = 0
    for i in account_card_splited:
        if i.isdigit():
            if len(i) == 16:
                i_index = account_card_splited.index(i)
                account_card_splited[i_index] = get_mask_card_number(i)
                return " ".join(account_card_splited)
            elif len(i) == 20:
                i_index = account_card_splited.index(i)
                account_card_splited[i_index] = get_mask_account(i)
                return " ".join(account_card_splited)
            else:
                raise ValueError("Некорректный номер карты или счёта")
        else:
            counter += 1
            if counter == len(account_card_splited):
                raise ValueError("Некорректный номер карты или счёта")
            else:
                continue


def get_date(timestamp: str) -> str:
    """Принимает временную метку и возвращает дату в формате ДД.ММ.ГГГГ"""
    year = timestamp[0:4]
    month = timestamp[5:7]
    day = timestamp[8:10]
    date = f"{day}.{month}.{year}"
    return date
