from __future__ import annotations
import csv


def from_csv(path: str) -> list[Stock]:
    with open(path, "r") as f:
        rows = csv.reader(f)
        _ = next(rows)

        stocks: list[Stock] = []
        for row in rows:
            stock = Stock(row[0], int(row[1]), float(row[2]))
            stocks.append(stock)
    return stocks


def print_portfolio(data: list[Stock]) -> None:
    print("%10s %10s %10s" % ("name", "shares", "price"))
    print("%10s %10s %10s" % (10*"-", 10*"-", 10*"-"))
    for s in data:
        print("%10s %10d %10.2f" % (s.name, s.shares, s.price))


class Stock:
    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def cell(self, nshares: int) -> None:
        self.shares -= nshares
