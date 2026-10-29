import sys


def _init():
    locs = sys._getframe(1).f_locals
    self = locs["self"]
    for name, val in locs.items():
        if name == "self":
            continue
        setattr(self, name, val)


class Stock:
    def __init__(self, name, shares, price):
        _init()


if __name__ == "__main__":
    s = Stock(name="GOOG", price=490.1, shares=50)
