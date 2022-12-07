points = {
        "X" : 1,
        "Y" : 2,
        "Z" : 3,
        }

results = {
        "X" : ["B", "A", "C"],
        "Y" : ["C", "B", "A"],
        "Z" : ["A", "C", "B"]
        }

f = open("./input", "r")
total = 0

for l in f:
    s = l.split()
    total += points[s[1]] + 3 * results[s[1]].index(s[0])

print(total)
