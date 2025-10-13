import pytest

from src.decorators import log


@log()
def success_function(a, b):
    return a + b


@log()
def error_function(x):
    return 10 / x


# Тесты
def test_log_success_console(capsys):
    """Тест успешного выполнения с выводом в консоль."""
    result = success_function(2, 3)
    assert result == 5

    captured = capsys.readouterr()
    output = captured.out.strip()

    assert "success_function ok" in output
    assert "Start time:" in output
    assert "End time:" in output


def test_log_error_console(capsys):
    """Тест ошибки с выводом в консоль."""
    with pytest.raises(ZeroDivisionError):
        error_function(0)

    captured = capsys.readouterr()
    output = captured.out.strip()

    assert "error_function error: ZeroDivisionError" in output
    assert "Start time:" in output
    assert "End time:" in output
    assert "Inputs: (0,)" in output


def test_log_success_file(tmp_path):
    """Тест успешного выполнения и записи в файл."""
    log_file = tmp_path / "my_log.txt"

    @log(filename=str(log_file))
    def temp_func(a, b):
        return a * b

    result = temp_func(2, 3)
    assert result == 6

    with open(log_file, "r", encoding="utf-8") as f:
        content = f.read().strip()

    assert "temp_func ok" in content
    assert "Start time:" in content
    assert "End time:" in content


def test_log_error_file(tmp_path):
    """Тест ошибки и записи в файл."""
    log_file = tmp_path / "error_log.txt"

    @log(filename=str(log_file))
    def temp_func(x):
        return 10 / x

    with pytest.raises(ZeroDivisionError):
        temp_func(0)

    with open(log_file, "r", encoding="utf-8") as f:
        content = f.read().strip()

    assert "temp_func error: ZeroDivisionError" in content
    assert "Start time:" in content
    assert "End time:" in content
    assert "Inputs: (0,)" in content
