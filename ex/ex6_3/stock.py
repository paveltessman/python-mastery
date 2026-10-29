from structure import Structure


class Stock(Structure):
    def __init__(self, name, shares, price) -> None:
        self._init()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares


Stock.set_fields()


if __name__ == "__main__":
    s = Stock("GOOG", 50, 490.1)
