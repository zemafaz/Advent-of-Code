import heapq

f = open("./day_1_input", "r")
max_calories = [0,0,0]
heapq.heapify(max_calories)
current = 0

for line in f:
    if line == "\n":
        heapq.heappushpop(max_calories, current)
        current = 0
    else:
        current += int(line)

print(max_calories)
print(sum(max_calories))

f.close()
