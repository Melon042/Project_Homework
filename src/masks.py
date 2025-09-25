def get_mask_card_number(card_num: str) -> str:
    """Маскирует номер карты."""
    card_num = str(card_num)

    digits_only = "".join(char for char in card_num if char.isdigit())

    if len(digits_only) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    masked_card_num = f"{digits_only[:4]} {digits_only[4:6]}** **** {digits_only[12:]}"

    if not card_num.replace(" ", "").isdigit():
        prefix = ""
        for char in card_num:
            if char.isdigit():
                break
            prefix += char
        prefix = prefix.rstrip()
        return f"{prefix} {masked_card_num}"
    return masked_card_num


def get_mask_account_number(account_num: str) -> str:
    """Маскирует номер счёта."""
    account_num = str(account_num)

    digits_only = "".join(char for char in account_num if char.isdigit())

    if len(digits_only) != 20:
        raise ValueError("Номер счёта должен содержать 20 цифр")

    masked_account_num = f"**{digits_only[-4:]}"

    if not account_num.replace(" ", "").isdigit():
        prefix = ""
        for char in account_num:
            if char.isdigit():
                break
            prefix += char
        prefix = prefix.rstrip()
        return f"{prefix} {masked_account_num}"
    return masked_account_num
