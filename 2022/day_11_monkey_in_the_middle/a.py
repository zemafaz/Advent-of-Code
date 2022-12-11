from io import TextIOWrapper
from collections import deque
from math import prod

class Monkey:

    def __init__(self,
            items: deque[int],
            operation: str,
            operator: str,
            divisible: int,
            true: int,
            false: int):
        self.items: deque[int] = items
        self.operation: str = operation
        self.operator: str = operator
        self.divisible: int = divisible
        self.true: int = true
        self.false: int = false
        self.inspections = 0

    def __str__(self) -> str:
        return f"""Monkey:
    items: {self.items}
    operation: {self.operation}
    operator: {self.operator}
    divisible: {self.divisible}
    if true: {self.true}
    if false: {self.false}
    """


def solution(file_path: str) -> int:
    
    file: TextIOWrapper = open(file_path, "r")

    monkeys: list[Monkey] = []

    c_items: deque[int] = deque()
    c_operation: str = ""
    c_operator: str = ""
    c_divisible: int = 0
    c_true: int = 0
    c_false: int = 0
    
    for line in file:
        if line == "\n":
            monkeys.append(Monkey(c_items, c_operation, c_operator, c_divisible, c_true, c_false))
            continue
        split = line.split()
        if split[0] == "Starting":
            c_items = deque()
            for n in split[2:]:
                if n[-1] == ",":
                    n = n[:-1]
                c_items.append(int(n))
        elif split[0] == "Operation:":
            c_operation = split[-2]
            c_operator = split[-1]
        elif split[0] == "Test:":
            c_divisible = int(split[-1])
        elif split[0] == "If":
            if split[1] == "true:":
                c_true = int(split[-1])
            elif split[1] == "false:":
                c_false = int(split[-1])
            else:
                raise Exception("What is this?")
        else:
            continue

    file.close()

    for _ in range(20):
        for monkey in monkeys:
            monkey.inspections += len(monkey.items)
            while len(monkey.items) > 0:
                item: int = monkey.items.popleft()
                operator: int = 0
                if monkey.operator == "old":
                    operator = item 
                else:
                    operator = int(monkey.operator)
                if monkey.operation == "*":
                    item *= operator
                elif monkey.operation == "+":
                    item += operator
                else:
                    raise Exception("What the heck!")
                item = item // 3
                if item % monkey.divisible == 0:
                    monkeys[monkey.true].items.append(item)
                else:
                    monkeys[monkey.false].items.append(item)
    inspections: list[int] = list(map(lambda x: x.inspections, monkeys))
    inspections.sort()
    return prod(inspections[-2:])

if __name__ == "__main__":
    output: int = 10605
    res: int = solution("./test")
    
    if res != output:
        print(f"\nDid not pass test:\n\tExpected {output}, returned {res}")
    else:
        print("\nPassed test!")

    res = solution("./input")
    print(f"\nSolution for input: {res}")
