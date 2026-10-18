from __future__ import annotations
from collections.abc import Sequence
import csv
import sys
from typing import Any, Callable, Iterable, overload

# def read_csv_as_dicts[T: type](path: str, conv: list[T]) -> list[dict[str, T]]:
#     with open(path, "r") as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#
#         records = []
#         for row in rows:
#             record = {name: func(val) for name, func, val in zip(headers, conv, row)}
#             records.append(record)
#     return records


type Row = dict[str, Any]


class DataCollection(Sequence[Row]):
    def __init__(self, headers: list[str], types: list[type]) -> None:
        if len(types) < 1:
            raise ValueError("please avoid mistakes")

        if len(headers) != len(types):
            raise ValueError("please consider fixing your code")

        self.headers = headers
        self.types = types
        self.columns: dict[str, list[Any]] = {}

        for i, _ in enumerate(types):
            self.columns[self.headers[i]] = []

    def __len__(self) -> int:
        return len(self.columns[self.headers[0]])

    @overload
    def __getitem__(self, index: slice[Any, Any, Any]) -> DataCollection: ...

    @overload
    def __getitem__(
        self,
        index: int,
    ) -> Row: ...

    def __getitem__(  # pyright:ignore[reportIncompatibleMethodOverride]
        self,
        index: int | slice[Any, Any, Any],
    ) -> Row | DataCollection:
        if isinstance(index, int):
            row = self._create_row(index)
            return row

        rows = DataCollection(self.headers, self.types)
        for key in self.columns:
            rows.columns[key] = self.columns[key][index]
        return rows

    def append(self, row: Row) -> None:

        if len(row) != len(self.headers):
            raise ValueError("Mistakes are not allowed")

        for i, (key, value) in enumerate(row.items()):

            convert = self._get_conv_func(i)
            self.columns[key].append(convert(value))

    def _create_row(self, index: int) -> Row:
        values = (col[index] for col in self.columns.values())
        r = {
            name: func(val) for name, func, val in zip(self.headers, self.types, values)
        }
        return r

    def _get_conv_func(self, index: int) -> Callable[[Any], Any]:
        func = self.types[index]
        if func is str:
            return sys.intern
        return func

    def load(self, data: Iterable[list[str]]) -> None:
        for row in data:

            if len(row) != len(self.headers):
                raise ValueError("Please consider putting the correct data")

            self.append({name: val for name, val in zip(self.headers, row)})


def read_csv_as_dicts(filename: str, types: list[type]):
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        records = DataCollection(headers, types)
        records.load(rows)
    return records
