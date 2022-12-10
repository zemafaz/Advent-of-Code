from io import TextIOWrapper

def solution(file_path: str) -> str:
    
    file: TextIOWrapper = open(file_path, "r")

    current_clock: int = 0
    current_value: int = 1

    current_iter: int = 40
    screen: str = ""

    for line in file:

        split: list[str] = line.split()
        operation_time: int = 0

        if split[0] == "addx":
            operation_time = 2
        elif split[0] == "noop":
            operation_time = 1
        else:
            raise Exception("Invalid operation!")

        for _ in range(operation_time):
            if abs(current_clock % 40 - current_value) <= 1:
                screen += "#"
            else:
                screen += "."
            current_clock += 1
            if current_clock == current_iter and current_clock != 240:
                screen += "\n"
                current_iter += 40
        
        if split[0] == "addx":
            current_value += int(split[1])

        if current_clock == 240:
            break

    file.close()

    return screen

if __name__ == "__main__":
    output: str = """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######....."""
    res: str = solution("./test")
    
    if res != output:
        print(f"\nDid not pass test:\n\tExpected:\n{output}\n\n\tReturned:\n{res}")
    else:
        print("\nPassed test!")

    res = solution("./input")
    print(f"\nSolution for input:\n{res}")
