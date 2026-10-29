import sys


class Structure:
    _fields = ()

    @staticmethod
    def _init():
        locs = sys._getframe(1).f_locals
        self = locs["self"]

        for name, val in locs.items():
            if name == "self":
                continue
            setattr(self, name, val)

    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        vals = ",".join(repr(v) for _, v in self.__dict__.items())
        return f"{cls_name}({vals})"

    def __setattr__(self, name, value) -> None:
        if name not in self._fields:
            raise AttributeError(f"No attribute {name!r}")
        self.__dict__[name] = value
