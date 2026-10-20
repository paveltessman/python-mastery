import csv
from typing import Any, Protocol
from decimal import Decimal


class Stock:
    __slots__ = ("name", "_shares", "_price")
    _type = float

    def __init__(self, row: list[Any]) -> None:
        self.name = row[0]
        self._shares = int(row[1])
        self._price = self._type(row[2])

    @property
    def shares(self) -> int:
        return self._shares

    @shares.setter
    def shares(self, val: int) -> None:
        if val < 0:
            raise ValueError("Please be correct")
        self._shares = val

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, val: Any) -> None:
        if not isinstance(val, self._type):
            raise ValueError("opa")
        self._price = val

    @property
    def cost(self) -> float:
        return self.shares * self.price

    def sell(self, nshares: int) -> None:
        self.shares -= nshares

    def __repr__(self) -> str:
        return f"Stock('{self.name}', {self.shares}, {self.price})"


class DStock(Stock):
    _type = Decimal


class RowReader(Protocol):
    def __init__(self, row: list[Any]) -> None: ...


def from_csv[T: RowReader](path: str, cls: type[T]) -> list[T]:
    with open(path, "r") as f:
        rows = csv.reader(f)
        _ = next(rows)

        stocks: list[T] = []
        for row in rows:
            stock = cls(row)
            stocks.append(stock)
    return stocks


if __name__ == "__main__":
    goog = Stock(["GOOG", 100, 490.10])
    print(repr(goog))
