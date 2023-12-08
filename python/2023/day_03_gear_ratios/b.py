
def get_number(line: str, index: int) -> str:
    def aux(line: str, index: int, step: int) -> str:
        if index == -1 or index == len(line) or not line[index].isdigit():
            return index
        return aux(line, index + step, step)

    if not line[index].isdigit():
        raise ValueError("Character is not a digit")

    res: str = line[aux(line, index, -1)+1:aux(line, index, 1)]
    return res


def check_surroundings(i: int, previous: str, current: str, next: str) -> int:

    def aux(line: str, i: int) -> None:
        found_number: bool = False
        for j in range(-1, 2):
            if not line[i+j].isdigit() and found_number:
                num: int = int(get_number(line, i+j-1))
                nums.append(num)
                found_number = False
            elif line[i+j].isdigit():
                found_number = True
                if i == 1:
                    num: int = int(get_number(line, i+j))
                    nums.append(num)
            else:
                found_number = False
            if len(nums) > 2:
                raise ValueError(toolong=True)

    try:
        nums: list[int] = []
        if previous:
            aux(previous, i)
        aux(current, i)
        if next:
            aux(next, i)
        if len(nums) != 2:
            return 0
        return nums[0] * nums[1]
    except ValueError as v:
        if v.toolong:
            return 0
        raise v


with open("./input") as file:
    previous = None
    res = 0
    current = file.tell()
    j = 1
    while True:
        file.seek(current)
        line = file.readline()
        if not line:
            break
        current = file.tell()
        next = file.readline()
        current_num = ""
        add_num = False
        for i, c in enumerate(line):
            if c == "*":
                to_add: int = check_surroundings(i, previous, line, next)
                if to_add != 0:
                    print(f"Added 
                res += to_add
        previous = line
    print(res)
