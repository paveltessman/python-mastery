n = 10
code = """
for i in range(n):
    print(i, end=" ")
print()
"""

exec(code)


class Stock:
    _fields = ("name", "shares", "price")


argstr = ",".join(Stock._fields)

code = f"def __init__(self, {argstr}):\n"

for name in Stock._fields:
    code += f"    self.{name} = {name}\n"

print(code)


locs = {}

exec(code, locs)

Stock.__init__ = locs["__init__"]

s = Stock("GOOG", 100, 490.1)
