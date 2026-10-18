from typing import Sequence


def print_table(data: list[object], names: Sequence[str]) -> None:
    col_size = min(max((len(name) for name in names)) + 2, 10)

    for name in names:
        print(name.rjust(col_size), end="")
    print()

    for name in names:
        print(" ", "-" * (col_size - 2), end="")
    print()

    for obj in data:
        for name in names:
            print(str(getattr(obj, name)).rjust(col_size), end="")
        print()
