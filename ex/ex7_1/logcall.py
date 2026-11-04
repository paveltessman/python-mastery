from validate import validated, Integer


def logged(func):
    print("adding logging to", func.__name__)

    def wrapper(*args, **kwargs):
        print("calling", func.__name__)
        return func(*args, **kwargs)

    return wrapper


@logged
@validated
def add(x: Integer, y: Integer):
    return x + y


@logged
@validated
def sub(x: Integer, y: Integer):
    return x - y
