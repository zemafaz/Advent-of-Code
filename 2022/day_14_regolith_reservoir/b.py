
def solution(file_path: str) -> int:
    with open(file_path, "r") as file:

        start_pos = (500, 0)

        min_i: int = 0
        max_i: int = 0
        min_j: int = 0
        max_j: int = 0
        
        # Reading file
        rocks: list[list[tuple[int, int]]] = []
        for line in file:
            rock: list[tuple[int, int]] = []
            for j, i in map(lambda x: x.split(","), line[:-1].split("->")):
                rock.append((int(j) - start_pos[0], int(i) - start_pos[1]))
                min_i = min(int(i) - start_pos[1], min_i) 
                max_i = max(int(i) - start_pos[1], max_i) 
                min_j = min(int(j) - start_pos[0], min_j) 
                max_j = max(int(j) - start_pos[0], max_j) 
            rocks.append(rock)

        if min_j == None or max_j == None or min_i == None or max_i == None:
            raise Exception()

        file.close()
        
        # Building cave layout
        height: int = max_i + 1
        negative_adj: int = max(height + 1, -min_j)
        positive_adj: int = max(height + 1, max_j)
        start_pos = (negative_adj, start_pos[1])
        cave_layout: list[list[str]] = [["."] * (negative_adj + positive_adj + 1) for _ in range(height + 1)]
        cave_layout.append(["#"] * len(cave_layout[0]))
        for rock in rocks:
            start: tuple[int,int] = (rock[0][0] + negative_adj, rock[0][1])
            for rem in rock[1:]:
                rem = (rem[0] + negative_adj, rem[1])
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

        #Solving Problem
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
            if (j, i) == start_pos:
                return res + 1
            res += 1
            i = start_pos[1]
            j = start_pos[0]

if __name__ == "__main__":
    output: int = 93
    res: int = solution("./test")
    
    if res != output:
        print(f"\nDid not pass test:\n\tExpected {output}, returned {res}")
    else:
        print("\nPassed test!")

    res = solution("./input")
    print(f"\nSolution for input: {res}")
