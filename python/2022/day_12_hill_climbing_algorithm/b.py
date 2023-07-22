from collections import deque
from copy import deepcopy

def solution(file_path: str) -> int:

    with open(file_path, "r") as file:
        height_map_original: list[list[int]] = []
        start_positions: list[tuple[int, int]] = [] 
        end_pos: tuple[int, int] = (-1, -1)
        
        i: int = 0

        for line in file:
            current_row: list[int] = []
            for j in range(len(line) - 1):
                if line[j] == "S" or line[j] == "a":
                    start_positions.append((i, j))
                    current_row.append(ord("a"))
                elif line[j] == "E":
                    end_pos = (i, j)
                    current_row.append(ord("z"))
                else:
                    current_row.append(ord(line[j]))
            height_map_original.append(current_row)
            i += 1

        res: int = -1
        
        for start_pos in start_positions:
            height_map: list[list[int]] = deepcopy(height_map_original)
            stack: deque[tuple[int, int]] = deque([start_pos])
            iter: int = 0
            
            while stack:
                next_iter: deque[tuple[int, int]] = deque()
                while stack:
                    i, j = stack.popleft()
                    if i == end_pos[0] and j == end_pos[1]:
                        res = min(res, iter) if res != -1 else iter
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
                iter += 1

        return res

if __name__ == "__main__":
    output: int = 29
    res: int = solution("./test")
    
    if res != output:
        print(f"\nDid not pass test:\n\tExpected {output}, returned {res}")
    else:
        print("\nPassed test!")

    res = solution("./input")
    print(f"\nSolution for input: {res}")
