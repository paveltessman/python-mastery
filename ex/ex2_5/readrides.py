from __future__ import annotations
from collections.abc import Sequence
import csv
from typing import Any, overload

type Row = dict[str, str]


def _get_row(route: str, date: str, daytype: str, rides: str) -> Row:
    row = {
        "route": route,
        "date": date,
        "daytype": daytype,
        "rides": rides,
    }
    return row


class RideData(Sequence[Row]):
    def __init__(self) -> None:
        self.routes: list[str] = []
        self.dates: list[str] = []
        self.daytypes: list[str] = []
        self.numrides: list[str] = []

    def __len__(self) -> int:
        return len(self.routes)

    @overload
    def __getitem__(self, index: slice[Any, Any, Any]) -> RideData: ...

    @overload
    def __getitem__(
        self,
        index: int,
    ) -> Row: ...

    def __getitem__(  # pyright:ignore[reportIncompatibleMethodOverride]
        self,
        index: int | slice[Any, Any, Any],
    ) -> Row | RideData:
        if isinstance(index, int):
            row = _get_row(
                self.routes[index],
                self.dates[index],
                self.daytypes[index],
                self.numrides[index],
            )
            return row

        rows = RideData()
        for route, date, daytype, ride in zip(
            self.routes[index],
            self.dates[index],
            self.daytypes[index],
            self.numrides[index],
        ):
            rows.append(_get_row(route, date, daytype, ride))
        return rows

    def append(self, row: Row) -> None:
        self.routes.append(row["route"])
        self.dates.append(row["date"])
        self.daytypes.append(row["daytype"])
        self.numrides.append(row["rides"])


def read_rides_as_dicts(filename):
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {"route": route, "date": date, "daytype": daytype, "rides": rides}
            records.append(record)
    return records
