from abc import ABC, abstractmethod
from typing import Sequence
from ..ex3_4 import stock


class TableFormatter(ABC):
    @abstractmethod
    def print_headings(self, headers: Sequence[str]) -> None:
        _ = headers
        raise NotImplementedError()

    @abstractmethod
    def print_row(self, rowdata: list[str]) -> None:
        _ = rowdata
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    def print_headings(self, headers: Sequence[str]) -> None:
        print(" ".join("%10s" % h for h in headers))
        print(("-" * 10 + " ") * len(headers))

    def print_row(self, rowdata: list[str]) -> None:
        print(" ".join("%10s" % d for d in rowdata))


class CSVTableFormatter(TableFormatter):
    def print_headings(self, headers: Sequence[str]) -> None:
        print(",".join(headers))

    def print_row(self, rowdata: list[str]) -> None:
        print(",".join(str(r) for r in rowdata))


class HTMLTableFormatter(TableFormatter):
    def print_headings(self, headers: Sequence[str]) -> None:
        print("<tr>", end=" ")
        print(*(f"<th>{name}</th>" for name in headers), end=" ")
        print("</tr>")

    def print_row(self, rowdata: list[str]) -> None:
        print("<tr>", end=" ")
        print(*(f"<td>{val}</td>" for val in rowdata), end=" ")
        print("</tr>")


def print_table(
    records: Sequence[object],
    fields: Sequence[str],
    formatter: TableFormatter,
) -> None:

    if not isinstance(formatter, TableFormatter):
        raise TypeError("bro...")

    formatter.print_headings(fields)

    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.print_row(rowdata)


if __name__ == "__main__":

    p = stock.from_csv("Data/portfolio.csv", stock.Stock)

    print_table(p, ["name", "shares", "price"], TextTableFormatter())
    print()
    print_table(p, ["name", "shares", "price"], CSVTableFormatter())
    print()
    print_table(p, ["name", "shares", "price"], HTMLTableFormatter())
