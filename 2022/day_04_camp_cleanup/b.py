
f = open("./input", "r")

res = 0

for line in f:
    s = list(map(lambda x: x.split("-"), line[:-1].split(",")))
    s = list(map(lambda x: [int(x[0]), int(x[1])], s))
    if ((s[0][0] >= s[1][0] and s[0][1] <= s[1][1]) or
            (s[1][0] >= s[0][0] and s[1][1] <= s[0][1]) or
            (s[0][0] <= s[1][0] <= s[0][1]) or
            (s[0][0] <= s[1][1] <= s[0][1])):
        res += 1

print(res)

f.close()
