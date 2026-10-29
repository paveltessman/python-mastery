class Structure:
    _fields = ()

    def __init__(self, *args) -> None:
        if len(args) != len(self._fields):
            raise TypeError(f"Expected {len(self._fields)} arguments")

        for arg in zip(self._fields, args):
            setattr(self, arg[0], arg[1])

    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        vals = ",".join(repr(v) for _, v in self.__dict__.items())
        return f"{cls_name}({vals})"

    def __setattr__(self, name, value) -> None:
        if name not in self._fields:
            raise AttributeError(f"No attribute {name!r}")
        self.__dict__[name] = value


if __name__ == "__main__":

    class Stock(Structure):
        _fields = ("name", "shares", "price")

    s = Stock("GOOG", 100, 490.1)
