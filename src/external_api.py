import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

Exchange_Rates_Data_API = os.getenv("Exchange_Rates_Data_API")

def get_transaction_amount_rub(transaction: dict) -> float:
    """Возвращает сумму транзакции в рублях, конвертируя USD и EUR через внешний API"""
    if transaction["operationAmount"]['currency']['code'] in ('USD', 'EUR'):

        headers = {"apikey": Exchange_Rates_Data_API}

        response = requests.get("https://api.apilayer.com/exchangerates_data/convert",
                                headers=headers,
                                params={'to': 'RUB', 'from': transaction["operationAmount"]["currency"]["code"],
                   'amount': transaction["operationAmount"]["amount"]})

        result = response.json()

        return float(result["result"])
    elif transaction["operationAmount"]['currency']['code'] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    else:
        raise ValueError('Неподдерживаемая валюта. (Поддерживаются: RUB, USD, EUR.)')
