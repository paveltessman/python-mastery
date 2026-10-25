# pyright: strict

import csv
from typing import Any, Iterable


def read_csv_as_dicts(
    filename: str,
    types: list[type],
    headers: list[str] | None = None,
) -> list[dict[str, Any]]:
    with open(filename, "r") as f:
        records = csv_as_dicts(f, types, headers)
        return records


def read_csv_as_instances[T: Any](
    filename: str,
    cls: type[T],
    headers: list[str] | None = None,
) -> list[T]:
    with open(filename) as file:
        records = csv_as_instances(file, cls, headers)
    return records


def csv_as_dicts(
    lines: Iterable[str],
    types: list[type],
    headers: list[str] | None = None,
) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = {name: func(val) for name, func, val in zip(headers, types, row)}
        records.append(record)
    return records


def csv_as_instances[T: Any](
    lines: Iterable[str],
    cls: type[T],
    headers: list[str] | None = None,
) -> list[T]:
    records: list[T] = []
    rows = csv.reader(lines)
    if headers is None:
        _ = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records
