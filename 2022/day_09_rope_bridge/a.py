from io import TextIOWrapper

def solution(file_path: str) -> int:

    file: TextIOWrapper = open(file_path, "r")
    
    head: tuple[int, int] = (0,0)
    tail: tuple[int, int] = (0,0)
    tail_positions: set[tuple[int,int]] = set()

    for line in file:
        split: list[str] = line.split(" ")
        for _ in range(int(split[1])):
            previous_head: tuple[int, int] = head
            if split[0] == "U":
                head = (head[0] + 1, head[1])
            elif split[0] == "D":
                head = (head[0] - 1, head[1])
            elif split[0] == "L":
                head = (head[0], head[1] - 1)
            elif split[0] == "R":
                head = (head[0], head[1] + 1)
            else:
                raise Exception("Direction not recognized")

            if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
                tail = previous_head
            
            tail_positions.add(tail)

    file.close()

    return len(tail_positions)

if __name__ == "__main__":
    output: int = 13
    res: int = solution("./test")
    
    if res != output:
        print(f"\nDid not pass test:\n\tExpected {output}, returned {res}")
    else:
        print("\nPassed test!")

    res = solution("./input")
    print(f"\nSolution for input: {res}")
