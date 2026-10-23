from .validate import PositiveInteger, PositiveFloat, String


class Stock:
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    def __init__(self, name, shares, price) -> None:
        self.name = name
        self.shares = shares
        self.price = price


s = Stock("GOOG", 100, 490.10)
