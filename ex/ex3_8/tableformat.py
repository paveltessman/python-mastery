from abc import ABC, abstractmethod
from ..ex3_4 import stock


class TableFormatter(ABC):
    @abstractmethod
    def print_headings(self, headers):
        raise NotImplementedError()

    @abstractmethod
    def print_row(self, rowdata):
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    def print_headings(self, headers):
        print(" ".join("%10s" % h for h in headers))
        print(("-" * 10 + " ") * len(headers))

    def print_row(self, rowdata):
        print(" ".join("%10s" % d for d in rowdata))


class CSVTableFormatter(TableFormatter):
    def print_headings(self, headers):
        print(",".join(headers))

    def print_row(self, rowdata):
        print(",".join(str(r) for r in rowdata))


class HTMLTableFormatter(TableFormatter):
    def print_headings(self, headers):
        print("<tr>", end=" ")
        print(*(f"<th>{name}</th>" for name in headers), end=" ")
        print("</tr>")

    def print_row(self, rowdata):
        print("<tr>", end=" ")
        print(*(f"<td>{val}</td>" for val in rowdata), end=" ")
        print("</tr>")


class ColumnFormatMixin:
    formats = []

    def row(self, rowdata):
        rowdata = [(fmt & d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)


class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])


class PortfolioFormatter(ColumnFormatMixin, UpperHeadersMixin, TextTableFormatter):
    formats = ["%s", "%d", "%0.2f"]


def get_formatter(kind, column_formats=None, upper_headers=False):
    formatters = {
        "csv": CSVTableFormatter,
        "text": TextTableFormatter,
        "html": HTMLTableFormatter,
    }

    formatter = formatters[kind]

    if column_formats:

        class formatter(ColumnFormatMixin, formatter):
            formats = column_formats

    if upper_headers:

        class formatter(UpperHeadersMixin, formatter):
            pass

    return formatter()


def print_table(records, fields, formatter):

    if not isinstance(formatter, TableFormatter):
        raise TypeError("bro...")

    formatter.print_headings(fields)

    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.print_row(rowdata)


if __name__ == "__main__":

    p = stock.from_csv("Data/portfolio.csv", stock.Stock)

    print_table(
        p,
        ["name", "shares", "price"],
        get_formatter("text", column_formats=['"%s"', "%d", "%0.2f"]),
    )
