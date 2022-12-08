file = open("./input", "r")

grid: list[list[int]] = []
grid_hidden: list[list[bool]] = []
max_top: list[int] = []

for line in file:

    line_int: list[int] = []
    line_hidden: list[bool] = []
    max_line: int = -1

    for i in range(len(line) - 1):

        tree: int = int(line[i])
        line_int.append(tree)

        if len(max_top) - 1 < i:
            max_top.append(-1)
        if tree <= max_line and tree <= max_top[i]:
            line_hidden.append(True)
        else:
            line_hidden.append(False)
            if tree > max_top[i]:
                max_top[i] = tree
            if tree > max_line:
                max_line = tree
    
    max_line = -1
    
    for i in range(len(line_int) - 1, -1, -1):
        tree: int = line_int[i]
        if tree <= max_line:
            line_hidden[i] = line_hidden[i] and True
        else:
            line_hidden[i] = False
            max_line = tree

    grid.append(line_int)
    grid_hidden.append(line_hidden)

res: int = 0

for j in range(len(grid[0])):
    max_line: int = -1
    for i in range(len(grid) - 1, -1, -1):
        tree: int = grid[i][j]
        if tree <= max_line:
            grid_hidden[i][j] = grid_hidden[i][j] and True
            if not grid_hidden[i][j]:
                res += 1
        else:
            grid_hidden[i][j] = False
            res += 1
            max_line = tree

print(res)

file.close()
