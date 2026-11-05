from structure import Structure
from validate import String, PositiveInteger, PositiveFloat


class Stock(Structure):
    _fields = ("name", "shares", "price")
    _types = (str, int, float)

    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)


Stock.create_init()


if __name__ == "__main__":
    s = Stock("GOOG", 50, 490.1)
