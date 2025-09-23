def get_mask_card_number(card_num: str) -> str:
    """Маскирует номер карты"""
    card_num_splited = card_num.split()
    counter = 0
    card_num_temp = ''
    for char in card_num:
        if char != " ":
            card_num_temp += char
    if card_num_temp.isdigit():
        if len(card_num_temp) != 16:
            raise ValueError("Номер карты должен содержать 16 цифр")
        else:
            masked_card_num = f"{card_num_temp[:4]} {card_num_temp[4:6]}** **** {card_num_temp[12:]}"
            return masked_card_num

    for item in card_num_splited:
        if item.isdigit():
            if len(item) != 16:
                raise ValueError("Номер карты должен содержать 16 цифр")
            masked_card_num = f"{item[:4]} {item[4:6]}** **** {item[12:]}"
            card_num_splited[card_num_splited.index(item)] = masked_card_num
            return " ".join(card_num_splited)
        else:
            counter += 1
            if counter == len(card_num_splited):
                raise ValueError("Некорректный номер карты")
            else:
                continue
    raise ValueError("Некорректный номер карты")


def get_mask_account(account_num: str) -> str:
    """Маскирует номер счёта"""
    if len(account_num) != 20:
        raise ValueError("Номер счёта должен содержать 20 цифр")
    masked_account_num = f"**{account_num[-4:]}"
    return masked_account_num
