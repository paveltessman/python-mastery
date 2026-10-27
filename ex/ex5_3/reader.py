import csv


def read_csv_as_dicts(filename, types, headers=None):
    with open(filename, "r") as f:
        records = csv_as_dicts(f, types, headers)
        return records


def read_csv_as_instances(filename, cls, headers=None):
    with open(filename) as file:
        records = csv_as_instances(file, cls, headers)
    return records


def convert_csv(lines, fn, headers=None):
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    return list(map(lambda row: fn(headers, row), rows))


def csv_as_dicts(lines, types, headers=None):
    def to_dict(headers, row):
        return {name: func(val) for name, func, val in zip(headers, types, row)}

    return convert_csv(lines, to_dict, headers)


def csv_as_instances(lines, cls, headers=None):
    def from_row(_, row):
        return cls.from_row(row)

    return convert_csv(lines, from_row, headers)


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    squares = map(lambda x: x * x, nums)
