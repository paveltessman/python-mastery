import csv

from collections import Counter
import tracemalloc
from pprint import pprint


class Record:
    def __init__(self, row: list[str]) -> None:
        if len(row) != 4:
            raise ValueError
        self.route = row[0]
        self.date = row[1]
        self.daytype = row[2]
        self.rides = int(row[3])


type Data = list[Record]


def read_rides(filename: str) -> Data:
    records: Data = []

    with open(filename, "r") as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skip headers
        for row in rows:
            record = Record(row)
            records.append(record)

    return records


def count_routes(data: Data) -> int:
    routes = {row.route for row in data}
    return len(routes)


def how_many_people(data: Data, date: str, route: str) -> int:
    total = sum([row.rides for row in data if row.date == date and row.route == route])
    return total


def total_rides_by_route(data: Data) -> dict[str, int]:
    c = Counter()
    for row in data:
        c[row.route] += row.rides
    return c


def greatest_increase(data: Data):
    def count_year(year: str) -> Counter[str]:
        c: Counter[str] = Counter()
        for row in data:
            row_year = row.date[-4:]
            if row_year != year:
                continue
            c[row.route] += row.rides
        return c

    counter_2001 = count_year("2001")
    counter_2011 = count_year("2011")

    return (counter_2011 - counter_2001).most_common(5)


if __name__ == "__main__":
    tracemalloc.start()

    data = read_rides("Data/ctabus.csv")

    print(count_routes(data))
    print(how_many_people(data, "02/02/2011", "22"))
    print(total_rides_by_route(data))
    pprint(greatest_increase(data))

    print("Memory Use: Current %d, Peak %d" % tracemalloc.get_traced_memory())
