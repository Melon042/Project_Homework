import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_transaction_amount_rub(transaction: dict) -> float:
    """Возвращает сумму транзакции в рублях, конвертируя USD и EUR через внешний API"""
    if transaction["operationAmount"]["currency"]["code"] in ("USD", "EUR"):

        apikey = os.getenv("Exchange_Rates_Data_API")
        headers = {"apikey": apikey}

        response = requests.get(
            "https://api.apilayer.com/exchangerates_data/convert",
            headers=headers,
            params={
                "to": "RUB",
                "from": transaction["operationAmount"]["currency"]["code"],
                "amount": transaction["operationAmount"]["amount"],
            },
        )

        if response.status_code != 200:
            raise Exception(f"API error: {response.status_code}")

        result = response.json()

        return float(result["result"])

    elif transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    else:
        raise ValueError("Неподдерживаемая валюта. (Поддерживаются: RUB, USD, EUR.)")
