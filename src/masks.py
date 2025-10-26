import logging

logger = logging.getLogger('masks_logger')
file_handler = logging.FileHandler('logs/masks.log', mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_num: str) -> str:
    """Маскирует номер карты."""
    logger.info('Вызов функции "get_mask_card_number".')

    card_num = str(card_num)

    digits_only = "".join(char for char in card_num if char.isdigit())

    if len(digits_only) != 16:
        logger.error('Ошибка ValueError, некорректная длина номера карты.')
        raise ValueError("Номер карты должен содержать 16 цифр")

    masked_card_num = f"{digits_only[:4]} {digits_only[4:6]}** **** {digits_only[12:]}"

    if not card_num.replace(" ", "").isdigit():
        prefix = ""
        for char in card_num:
            if char.isdigit():
                break
            prefix += char
        prefix = prefix.rstrip()
        logger.info(f'Успешно замаскирован номер карты с префиксом: "{prefix}"')
        return f"{prefix} {masked_card_num}"
    logger.info(f'Успешно замаскирован номер карты: "{masked_card_num}"')
    return masked_card_num


def get_mask_account_number(account_num: str) -> str:
    """Маскирует номер счёта."""
    logger.info('Вызов функции "get_mask_account_number".')

    account_num = str(account_num)

    digits_only = "".join(char for char in account_num if char.isdigit())

    if len(digits_only) != 20:
        logger.error('Ошибка ValueError, некорректная длина номера счёта.')
        raise ValueError("Номер счёта должен содержать 20 цифр")

    masked_account_num = f"**{digits_only[-4:]}"

    if not account_num.replace(" ", "").isdigit():
        prefix = ""
        for char in account_num:
            if char.isdigit():
                break
            prefix += char
        prefix = prefix.rstrip()
        logger.info(f'Успешно замаскирован номер счёта с префиксом: "{prefix}"')
        return f"{prefix} {masked_account_num}"
    logger.info(f'Успешно замаскирован номер счёта: "{masked_account_num}"')
    return masked_account_num
