# readrides.py

import csv


def read_rides_as_dict(filename: str) -> None:
    records = []

    with open(filename, "r") as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skip headers
        for row in rows:
            record = {}
            record["route"] = row[0]
            record["date"] = row[1]
            record["daytype"] = row[2]
            record["rides"] = int(row[3])
            records.append(record)


def read_rides_as_class(filename: str) -> None:
    class Record:
        def __init__(self, route, date, daytype, rides) -> None:
            self.route = route
            self.date = date
            self.daytype = daytype
            self.rides = rides

    records = []
    with open(filename, "r") as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skip headers
        for row in rows:
            record = Record(row[0], row[1], row[2], int(row[3]))
            records.append(record)


def read_rides_as_class_with_slots(filename: str) -> None:
    class Record:
        __slots__ = ["route", "date", "daytype", "rides"]

        def __init__(self, route, date, daytype, rides) -> None:
            self.route = route
            self.date = date
            self.daytype = daytype
            self.rides = rides

    records = []
    with open(filename, "r") as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skip headers
        for row in rows:
            record = Record(row[0], row[1], row[2], int(row[3]))
            records.append(record)


def read_rides_as_named_tuple(filename: str) -> None:
    from typing import NamedTuple

    class Record(NamedTuple):
        route: str
        date: str
        daytype: str
        rides: int

    records = []
    with open(filename, "r") as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skip headers
        for row in rows:
            record = Record(row[0], row[1], row[2], int(row[3]))
            records.append(record)


def read_rides_as_tuples(filename):
    """
    Read the bus ride data as a list of tuples
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records


if __name__ == "__main__":
    import tracemalloc

    tracemalloc.start()
    rows = read_rides_as_class("Data/ctabus.csv")
    print("Memory Use: Current %d, Peak %d" % tracemalloc.get_traced_memory())
