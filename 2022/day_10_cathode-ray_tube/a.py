from io import TextIOWrapper

def solution(file_path: str) -> int:
    
    file: TextIOWrapper = open(file_path, "r")

    current_clock: int = 1
    current_value: int = 1

    current_iter_value: int = 0
    current_iter: int = 20

    for line in file:
        split: list[str] = line.split()
        previous_value: int = current_value

        if split[0] == "addx":
            current_clock += 2
            current_value += int(split[1])
        elif split[0] == "noop":
            current_clock += 1
        else:
            raise Exception("Invalid operation!")

        if current_clock >= current_iter:
            if current_clock == current_iter:
                current_iter_value += current_iter * current_value
            else:
                current_iter_value += current_iter * previous_value
            current_iter += 40
            if current_iter > 220:
                break

    file.close()

    return current_iter_value

if __name__ == "__main__":
    output: int = 13140
    res: int = solution("./test")
    
    if res != output:
        print(f"\nDid not pass test:\n\tExpected {output}, returned {res}")
    else:
        print("\nPassed test!")

    res = solution("./input")
    print(f"\nSolution for input: {res}")
