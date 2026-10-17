from __future__ import annotations
from functools import total_ordering
from typing import Any, Self


@total_ordering
class MutInt:
    __slots__ = ["value"]

    def __init__(self, value: int) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f"MutInt({self.value!r})"

    def __format__(self, format_spec: str, /) -> str:
        return format(self.value, format_spec)

    def __add__(self, other: Any) -> MutInt:
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        if isinstance(other, int):
            return MutInt(self.value + other)
        return NotImplemented

    __radd__ = __add__

    def __iadd__(self, other: Any) -> Self:
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        if isinstance(other, int):
            self.value += other
            return self
        return NotImplemented

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, MutInt):
            return self.value == other.value
        if isinstance(other, int):
            return self.value == other
        return NotImplemented

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, MutInt):
            return self.value < other.value
        if isinstance(other, int):
            return self.value < other
        return NotImplemented

    def __int__(self) -> int:
        return self.value

    __index__ = __int__

    def __float__(self) -> float:
        return float(self.value)
