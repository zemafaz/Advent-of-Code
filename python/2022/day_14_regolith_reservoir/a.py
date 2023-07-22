
def solution(file_path: str) -> int:
    with open(file_path, "r") as file:

        start_pos = (500, 0)

        min_i: int = start_pos[1]
        max_i: int = start_pos[1]
        min_j: int = start_pos[0] 
        max_j: int = start_pos[0] 
        
        # Reading file
        rocks: list[list[tuple[int, int]]] = []
        for line in file:
            rock: list[tuple[int, int]] = []
            for j, i in map(lambda x: x.split(","), line[:-1].split("->")):
                rock.append((int(j),int(i)))
                min_i = min(int(i), min_i) 
                max_i = max(int(i), max_i) 
                min_j = min(int(j), min_j) 
                max_j = max(int(j), max_j) 
            rocks.append(rock)

        if min_j == None or max_j == None or min_i == None or max_i == None:
            raise Exception()

        file.close()
        
        # Building cave layout
        start_pos = (start_pos[0] - min_j, start_pos[1] - min_i)
        cave_layout: list[list[str]] = [["."] * (max_j - min_j + 1) for _ in range(max_i - min_i + 1)]
        for rock in rocks:
            start: tuple[int,int] = (rock[0][0] - min_j, rock[0][1] - min_i)
            for rem in rock[1:]:
                rem = (rem[0] - min_j, rem[1] - min_i)
                if rem[1] == start[1]:
                    i: int = start[1]
                    for j in range(min(rem[0], start[0]), max(rem[0], start[0]) + 1):
                        cave_layout[i][j] = "#"
                elif rem[0] == start[0]:
                    j: int = start[0]
                    for i in range(min(rem[1], start[1]), max(rem[1], start[1]) + 1):
                        cave_layout[i][j] = "#"
                else:
                    raise Exception()
                start = rem
        
        # Solving Problem
        res: int = 0
        i: int = start_pos[1]
        j: int = start_pos[0]
        
        while True:
            if i + 1 == len(cave_layout):
                return res
            if cave_layout[i+1][j] == ".":
                i += 1
                continue
            if j - 1 < 0:
                return res
            if cave_layout[i+1][j-1] == ".":
                i += 1
                j -= 1
                continue
            if j + 1 == len(cave_layout[0]):
                return res
            if cave_layout[i+1][j+1] == ".":
                i += 1
                j += 1
                continue
            cave_layout[i][j] = "o"
            res += 1
            i = start_pos[1]
            j = start_pos[0]

if __name__ == "__main__":
    output: int = 24
    res: int = solution("./test")
    
    if res != output:
        print(f"\nDid not pass test:\n\tExpected {output}, returned {res}")
    else:
        print("\nPassed test!")

    res = solution("./input")
    print(f"\nSolution for input: {res}")
