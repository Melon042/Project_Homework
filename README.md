# Учебный pet-проект "Новый виджет"

## Описание проекта:
Разработка нового виджета личного кабинета клиентов для крупного банка.
Это виджет, который показывает несколько последних успешных банковских операций клиента.
Проект будет готовить данные на бэкенде для отображения в новом виджете.

## Установка:
Клонируйте репозиторий:
```
git clone https://github.com/Melon042/Project_Homework.git
```
## Описание функций:
* get_mask_card_number(card_num: str) -> str:
  #Маскирует номер карты
* get_mask_account(account_num: str) -> str:
  #Маскирует номер счёта
* mask_account_card(account_card: str) -> str:
  #Маскирует данные карты или счёта
* get_date(timestamp: str) -> str:
  #Принимает временную метку и возвращает дату в формате ДД.ММ.ГГГГ
* filter_by_state(bank_operations: list[dict], state: str = "EXECUTED") -> list[dict]:
  #Принимает список словарей, фильтрует их по указанному значению ключа 'state' и возвращает отфильтрованный список.
* sort_by_date(bank_operations: list[dict], reverse: bool = True) -> list[dict]:
  #Принимает список словарей, сортирует их по дате и возвращает отсортированный список.
* filter_by_currency(transactions: list[dict], currency: str) -> Generator[dict, None, None]:
  #Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной.
* transaction_descriptions(transactions: list[dict]) -> Generator[str, None, None]:
  #Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
* card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
  #Генерирует номера банковских карт в формате 'XXXX XXXX XXXX XXXX'.
* log(filename=None):
  #Декоратор, логирующий в файл или консоль (в зависимости от наличия параметра filename)
  #результат выполнения функции, время начала и завершения работы функции, входные параметры(в случае ошибки).
* get_list_from_json_file(path_to_json_file):
  #Принимает путь до JSON-файла и возвращает список.
  #Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
* get_transaction_amount_rub(transaction: dict) -> float:
  #Возвращает сумму транзакции в рублях, конвертируя USD и EUR через внешний API.

## Использование:
Вызовите функции с соответствующими параметрами и запустите код.

## Примеры использования функций:
* print(get_mask_card_number(7000792289606361))`

* usd_transactions = filter_by_currency(transactions, "USD")
  for _ in range(2):
      print(next(usd_transactions))

* descriptions = transaction_descriptions(transactions)
  for _ in range(5):
      print(next(descriptions))

* for card_number in card_number_generator(1, 5):
    print(card_number)

## Тестирование:
Покрытие кода тестами = 100%.

### Лицензия:
Этот проект пока не лицензирован.
