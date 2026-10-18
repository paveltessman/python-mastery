import csv
from typing import Any, Protocol, Self
from decimal import Decimal


class Stock:
    types = (str, int, float)

    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row: list[Any]) -> Self:
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)  # pyright: ignore[reportArgumentType]

    def cost(self):
        return self.shares * self.price

    def cell(self, nshares: int) -> None:
        self.shares -= nshares


class DStock(Stock):
    types = (str, int, Decimal)


class RowReader(Protocol):
    @classmethod
    def from_row(cls, row: list[Any]) -> Self: ...


def from_csv[T: RowReader](path: str, cls: type[T]) -> list[T]:
    with open(path, "r") as f:
        rows = csv.reader(f)
        _ = next(rows)

        stocks: list[T] = []
        for row in rows:
            stock = cls.from_row(row)
            stocks.append(stock)
    return stocks
