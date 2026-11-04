from validate import validated, Integer
from functools import wraps


def logged(prefix):
    def decorator(func):
        print(prefix, "adding logging to", func.__name__)

        @wraps(func)
        def wrapper(*args, **kwargs):
            print("calling", func.__name__)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@logged("opa")
@validated
def add(x: Integer, y: Integer):
    return x + y


@logged("opa2")
@validated
def sub(x: Integer, y: Integer):
    return x - y
