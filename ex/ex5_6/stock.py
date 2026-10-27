class Stock:
    def __init__(self, name, shares, price) -> None:
        self.name = name
        self.shares = shares
        self.price = price


if __name__ == "__main__":
    s = Stock("GOOG", 100, 490.10)
