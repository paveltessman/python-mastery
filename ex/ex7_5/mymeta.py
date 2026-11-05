class mytype(type):
    @staticmethod
    def __new__(meta, name, bases, __dict__):
        print("creating class :", name)
        print("base classes   :", bases)
        print("attributes     :", list(__dict__))
        return super().__new__(meta, name, bases, __dict__)


class myobject(metaclass=mytype):
    pass


class Stock(myobject):
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


s = Stock("GOOD", 100, 490.10)


class MyStock(Stock):
    pass

m = MyStock("OOO", 50, 15.1)
