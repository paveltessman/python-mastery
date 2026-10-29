class Structure:
    _fields = ()

    @classmethod
    def create_init(cls):

        argstr = ",".join(cls._fields)
        code = f"def __init__(self, {argstr}):\n"
        for name in cls._fields:
            code += f"    self.{name} = {name}\n"

        locs = {}
        exec(code, locs)
        cls.__init__ = locs["__init__"]

    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        vals = ",".join(repr(v) for _, v in self.__dict__.items())
        return f"{cls_name}({vals})"

    def __setattr__(self, name, value) -> None:
        if name not in self._fields:
            raise AttributeError(f"No attribute {name!r}")
        self.__dict__[name] = value
