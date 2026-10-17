total = 0.0

with open("Data/portfolio.dat", "r") as f:

    for line in f:

        data = line.split()
        amount = int(data[1])
        price = float(data[2])

        total += price * amount

print(total)
