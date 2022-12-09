from io import TextIOWrapper

def solution(file_path: str) -> int:

    file: TextIOWrapper = open(file_path, "r")
    
    positions: list[complex] = [0] * 10
    tail_positions: set[complex] = set()
    dirs: dict[str, complex] = {"L": 1, "R": -1, "D": 1j, "U": -1j}
    
    def sign(x: complex) -> complex:
        return complex((x.real > 0) - (x.real<0), (x.imag>0) - (x.imag<0))
    
    for line in file:
        split: list[str] = line.split(" ")

        for _ in range(int(split[1])):
            positions[0] += dirs[split[0]]

            for i in range(1, len(positions)):
                dist: complex = positions[i-1] - positions[i]
                if abs(dist) >= 2:
                    positions[i] += sign(dist)

            tail_positions.add(positions[-1])

    file.close()

    return len(tail_positions)

if __name__ == "__main__":
    print()
    output: int = 1
    res: int = solution("./test")
    
    if res != output:
        print(f"Did not pass test 1:\n\tExpected {output}, returned {res}")
    else:
        print("Passed test 1!")

    output = 36
    res: int = solution("./test_2")
    
    if res != output:
        print(f"Did not pass test 2:\n\tExpected {output}, returned {res}")
    else:
        print("Passed test 2!")

    res = solution("./input")
    print(f"\nSolution for input: {res}")
