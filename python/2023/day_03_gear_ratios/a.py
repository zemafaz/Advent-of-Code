def check_if_symbol(c: str) -> bool:
    return not c.isdigit() and c != "." and c != "\n"


def check_surroundings(i: int, previous: str, current: str, next: str):
    for j in range(-1, 2):
        if (previous and 0 <= i + j < len(previous) and
                check_if_symbol(previous[i+j])):
            return True
        if (next and 0 <= i + j < len(next) and
                check_if_symbol(next[i+j])):
            return True
    if ((i - 1 >= 0 and check_if_symbol(current[i-1])) or
            (i + 1 < len(current) and check_if_symbol(current[i+1]))):
        return True
    return False


with open("./input") as file:
    previous = None
    res = 0
    current = file.tell()
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
            if c.isdigit():
                current_num += c
                if not add_num:
                    add_num |= check_surroundings(i, previous, line, next)
            else:
                if add_num:
                    res += int(current_num)
                current_num = ""
                add_num = False
        previous = line
    print(res)
