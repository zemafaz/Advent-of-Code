import os

with open(os.path.join(os.path.dirname(__file__), "input")) as file:
    res: int = 0
    while line := file.readline():
        only_digits: str = "".join(filter(lambda c: c.isdigit(), line))
        res += int(only_digits[0] + only_digits[-1])
    print(res)
