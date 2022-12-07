
f = open("./input", "r")
max_calories = 0

current = 0

for line in f:
    if line == "\n":
        max_calories = max(max_calories, current)
        current = 0
    else:
        current += int(line)

print(max_calories)

f.close()
