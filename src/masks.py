def get_mask_card_number(card_num: str) -> str:
    """Маскирует номер карты"""
    if len(card_num) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")
    masked_card_num = f"{card_num[:4]} {card_num[4:6]}** **** {card_num[12:]}"
    return masked_card_num


def get_mask_account(account_num: str) -> str:
    """Маскирует номер счёта"""
    if len(account_num) != 20:
        raise ValueError("Номер счёта должен содержать 20 цифр")
    masked_account_num = f"**{account_num[-4:]}"
    return masked_account_num
