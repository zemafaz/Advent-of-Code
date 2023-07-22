stacks = [
        ["T", "D", "W", "Z", "V","P"],
        ["L", "S", "W", "V", "F", "J", "D"],
        ["Z", "M", "L", "S", "V", "T", "B", "H"],
        ["R", "S", "J"],
        ["C", "Z", "B", "G", "F", "M", "L", "W"],
        ["Q", "W", "V", "H", "Z", "R", "G", "B"],
        ["V", "J", "P", "C", "B", "D", "N"],
        ["P", "T", "B", "Q"],
        ["H", "G", "Z", "R", "C"]
        ]

f = open("./input", "r")

for line in f:
    line_split = line.split()
    line_split = [int(line_split[1]), int(line_split[3]) - 1, int(line_split[5]) - 1]
    stacks[line_split[2]].extend(stacks[line_split[1]][-line_split[0]:])
    del stacks[line_split[1]][-line_split[0]:]

res = ""

for s in stacks:
    res += s[-1]

print(res)

f.close()
