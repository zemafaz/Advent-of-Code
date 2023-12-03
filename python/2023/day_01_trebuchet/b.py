import os

VALID_VALUES = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

with open(os.path.join(os.path.dirname(__file__), "input")) as file:
    res: int = 0
    while line := file.readline():

        index: int = len(line)

        for k in VALID_VALUES:
            current_index = line.find(k)
            if current_index != -1 and current_index < index:
                index = current_index
                first: int = VALID_VALUES[k]

        index: int = -1
        for k in VALID_VALUES:
            current_index = line.rfind(k)
            if current_index > index:
                index = current_index
                last: int = VALID_VALUES[k]

        res += first * 10 + last
    print(res)
