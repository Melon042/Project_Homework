from src.csv_xlsx_readers import read_csv, read_xlsx
from src.generators import filter_by_currency
from src.masks import get_mask_account_number
from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.utils import get_list_from_json_file
from src.widget import get_date, get_mask_account_or_card_num


def main():
    """Основная логика проекта"""

    option_chosen = input(
        """Привет! Добро пожаловать программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла"""
    )

    file_chosen = ""
    if option_chosen == "1":
        file_chosen = "Для обработки выбран JSON-файл."
    elif option_chosen == "2":
        file_chosen = "Для обработки выбран CSV-файл."
    elif option_chosen == "3":
        file_chosen = "Для обработки выбран XLSX-файл."
    else:
        raise ValueError("Выбран несуществующий пункт меню.")
    print(file_chosen)

    status_chosen = ""
    while status_chosen.upper() not in ["EXECUTED", "CANCELED", "PENDING"]:
        status_chosen = input(
            """Введите статус, по которому необходимо выполнить фильтрацию.
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING."""
        )
        if status_chosen.upper() not in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f'Статус операции "{status_chosen}" недоступен.')
    print(f'Операции отфильтрованы по статусу "{status_chosen.upper()}"')

    to_sort_by_date = False
    if input("Отсортировать операции по дате? Да / Нет").capitalize() == "Да":
        to_sort_by_date = True

    ascend_or_descend = "descend"
    if input("Отсортировать по возрастанию или по убыванию").lower() == "по возрастанию":
        ascend_or_descend = "ascend"

    rub_only = False
    if input("Выводить только рублевые транзакции? Да / Нет").capitalize() == "Да":
        rub_only = True

    to_sort_by_word_in_description = False
    if input("Отсортировать список транзакций по определенному слову в описании? Да / Нет").capitalize() == "Да":
        to_sort_by_word_in_description = True
        searched_word = input("Введите слово для поиска").lower()

    print("Распечатываю итоговый список транзакций...")

    operations_list = []
    if option_chosen == "1":
        operations_list = get_list_from_json_file("Data/operations.json")
    elif option_chosen == "2":
        operations_list = read_csv("Data/transactions.csv")
    elif option_chosen == "3":
        operations_list = read_xlsx("Data/transactions_excel.xlsx")

    operations_list = filter_by_state(operations_list, status_chosen.upper())

    if to_sort_by_date:
        if ascend_or_descend == "ascend":
            operations_list = sort_by_date(operations_list, reverse=False)
        else:
            operations_list = sort_by_date(operations_list)

    if rub_only:
        operations_list = list(filter_by_currency(operations_list, "RUB"))

    if to_sort_by_word_in_description:
        operations_list = process_bank_search(operations_list, searched_word)

    if len(operations_list) > 0:
        print(f"Всего банковских операций в выборке: {len(operations_list)}\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")

    if len(operations_list) > 0:
        if option_chosen == "1":
            for operation in operations_list:
                if operation["operationAmount"]["currency"]["name"] == "руб.":
                    currency_syntax = operation["operationAmount"]["currency"]["name"]
                else:
                    currency_syntax = operation["operationAmount"]["currency"]["code"]
                if operation["description"] == "Открытие вклада":
                    print(
                        f"""{get_date(operation['date'])} {operation['description']}
                    {get_mask_account_number(operation['to'])}
                    Сумма: {operation['operationAmount']['amount']} {currency_syntax}\n
                    """
                    )
                else:
                    print(
                        f"{get_date(operation['date'])} {operation['description']}\n"
                        f"{get_mask_account_or_card_num(operation['from'])} -> "
                        f"{get_mask_account_or_card_num(operation['to'])}\n"
                        f"Сумма: {operation['operationAmount']['amount']} {currency_syntax}\n"
                    )
        else:
            for operation in operations_list:
                if operation["currency_code"] == "RUB":
                    currency = "руб."
                else:
                    currency = operation["currency_code"]

                if operation["description"] == "Открытие вклада":
                    print(
                        f"""{get_date(operation['date'])} {operation['description']}
                    {get_mask_account_number(operation['to'])}
                    Сумма: {operation['amount']} {currency}\n"""
                    )
                else:
                    print(
                        f"{get_date(operation['date'])} {operation['description']}\n"
                        f"{get_mask_account_or_card_num(operation['from'])} -> "
                        f"{get_mask_account_or_card_num(operation['to'])}\n"
                        f"Сумма: {operation['amount']} {currency}\n"
                    )
