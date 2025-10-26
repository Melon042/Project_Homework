import pytest
from unittest.mock import patch, Mock
from src.external_api import get_transaction_amount_rub


def test_get_transaction_amount_rub_usd():
    """Тест конвертации USD в RUB."""
    with patch("os.getenv", return_value="test_api_key"):
        transaction = {
            "operationAmount": {
                "amount": "100",
                "currency": {"code": "USD"}
            }
        }

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": 9000.5}

        with patch("requests.get", return_value=mock_response) as mock_get:
            result = get_transaction_amount_rub(transaction)
            assert result == 9000.5

        mock_get.assert_called_once_with(
            "https://api.apilayer.com/exchangerates_data/convert",
            headers={"apikey": "test_api_key"},
            params={"to": "RUB", "from": "USD", "amount": "100"}
        )


def test_get_transaction_amount_rub_eur():
    """Тест конвертации EUR в RUB."""
    with patch("os.getenv", return_value="test_api_key"):
        transaction = {
            "operationAmount": {
                "amount": "50",
                "currency": {"code": "EUR"}
            }
        }

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": 4500.0}

        with patch("requests.get", return_value=mock_response):
            result = get_transaction_amount_rub(transaction)
            assert result == 4500.0


def test_get_transaction_amount_rub_rub():
    """Тест для RUB."""
    transaction = {
        "operationAmount": {
            "amount": "123.45",
            "currency": {"code": "RUB"}
        }
    }
    result = get_transaction_amount_rub(transaction)
    assert result == 123.45


def test_get_transaction_amount_rub_unsupported_currency():
    """Тест для неподдерживаемой валюты."""
    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "GBP"}
        }
    }
    with pytest.raises(ValueError, match='Неподдерживаемая валюта'):
        get_transaction_amount_rub(transaction)
