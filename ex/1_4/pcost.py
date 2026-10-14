def portfolio_cost(filename: str) -> float:
    total = 0.0

    with open(filename, "r") as f:
        for line in f:
            data = line.split()

            try:
                amount = int(data[1])
                price = float(data[2])

            except ValueError as e:
                print(f"Couldn't parse {line!r}: {e}")
                continue

            total += price * amount

    return total


print(portfolio_cost("Data/portfolio3.dat"))
