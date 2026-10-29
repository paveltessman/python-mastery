import inspect


def add(x, y):
    "Adds two things"
    return x + y


sig = inspect.signature(add)
