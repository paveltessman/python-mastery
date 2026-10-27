def typedproperty(name, expected_type):
    private_name = "_" + name

    @property
    def value(self):
        return getattr(self, private_name)

    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError("opa")
        setattr(self, private_name, val)

    return value


def validator(expected_type):
    attr_name = ""

    def __set_name__(self, cls, name):
        nonlocal attr_name
        attr_name = name

    return typedproperty(attr_name, expected_type)


def String():
    return validator(str)


def Integer():
    return validator(int)


def Float():
    return validator(float)
