file = open("./input", "r")

class View:

    def __init__(self):
        self.top: int = 0
        self.bottom: int = 0
        self.left: int = 0
        self.right: int = 0

    def __repr__(self):
        return f"{{top: {self.top}, bottom: {self.bottom}, left: {self.left}, right: {self.right}}}"

    def __str__(self):
        return f"{{top: {self.top}, bottom: {self.bottom}, left: {self.left}, right: {self.right}}}"

grid: list[list[int]] = []
grid_hidden: list[list[View]] = []

i: int = 0
for line in file:
    grid.append([])
    grid_hidden.append([])
    for j in range(len(line) - 1):
        
        tree: int = int(line[j])
        grid[i].append(tree)
        grid_hidden[i].append(View())
        
        for k in range(j - 1, -1, -1):
            grid_hidden[i][j].left += 1
            if grid[i][k] >= tree:
                break

        for k in range(i - 1, -1, -1):
            grid_hidden[i][j].top += 1
            if grid[k][j] >= tree:
                break

    for j in range(len(grid[i]) - 1, -1, -1):
        tree: int = int(grid[i][j])
        for k in range(j + 1, len(grid[i])):
            grid_hidden[i][j].right += 1
            if grid[i][k] >= tree:
                break
    i += 1

res: int = 0
pos_i: int = -1
pos_j: int = -1

for j in range(len(grid[0])):
    for i in range(len(grid) - 1, -1, -1):
        tree: int = grid[i][j]

        for k in range(i + 1, len(grid)):
            grid_hidden[i][j].bottom += 1
            if grid[k][j] >= tree:
                break
        score = grid_hidden[i][j].top * grid_hidden[i][j].bottom * grid_hidden[i][j].right * grid_hidden[i][j].left
        if res < score:
            res = score
            pos_i = i
            pos_j = j

print(res)

file.close()
