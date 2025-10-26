import functools
from datetime import datetime


def log(filename=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            try:
                result = func(*args, **kwargs)
                end_time = datetime.now()
                message = f"{func.__name__} ok. Start time: {start_time}, End time: {end_time}"
            except Exception as e:
                end_time = datetime.now()
                message = (
                    f"{func.__name__} error: {e.__class__.__name__}."
                    f"Start time: {start_time}, End time: {end_time}."
                    f"Inputs: {args}, {kwargs}"
                )
                raise
            finally:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(message + "\n")
                else:
                    print(message)
            return result

        return wrapper

    return decorator
