from collections import deque

def solution(file_path: str) -> int:

    with open(file_path, "r") as file:
        height_map: list[list[int]] = []
        start_pos: tuple[int, int] = (-1, -1)
        end_pos: tuple[int, int] = (-1, -1)
        
        i: int = 0

        for line in file:
            current_row: list[int] = []
            for j in range(len(line) - 1):
                if line[j] == "S":
                    start_pos = (i, j)
                    current_row.append(ord("a"))
                elif line[j] == "E":
                    end_pos = (i, j)
                    current_row.append(ord("z"))
                else:
                    current_row.append(ord(line[j]))
            height_map.append(current_row)
            i += 1
        
        stack: deque[tuple[int, int]] = deque([start_pos])
        res: int = 0
        
        while stack:
            next_iter: deque[tuple[int, int]] = deque()
            while stack:
                i, j = stack.popleft()
                if i == end_pos[0] and j == end_pos[1]:
                    return res
                current: int = height_map[i][j]
                if current == ord("V"):
                    continue
                height_map[i][j] = ord("V")
                if i - 1 >= 0 and height_map[i-1][j] <= current + 1:
                    next_iter.append((i-1, j))
                if i + 1 < len(height_map) and height_map[i+1][j] <= current + 1:
                    next_iter.append((i+1, j))
                if j - 1 >= 0 and height_map[i][j-1] <= current + 1:
                    next_iter.append((i, j-1))
                if j + 1 < len(height_map[0]) and height_map[i][j+1] <= current + 1:
                    next_iter.append((i, j+1))
            stack = next_iter
            res += 1

        return -1

if __name__ == "__main__":
    output: int = 31
    res: int = solution("./test")
    
    if res != output:
        print(f"\nDid not pass test:\n\tExpected {output}, returned {res}")
    else:
        print("\nPassed test!")

    res = solution("./input")
    print(f"\nSolution for input: {res}")
