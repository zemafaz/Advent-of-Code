results = [
            ["C", "A", "B"],
            ["A", "B", "C"],
            ["B", "C", "A"]
        ]

f = open("./input", "r")
total = 0

for l in f:
    s = l.split()
    i_0 = ord(s[0]) - ord("A")
    i_1 = ord(s[1]) - ord("X")
    my_choice = ord(results[i_1][i_0]) - ord("A") + 1
    print(my_choice)
    total += my_choice + 3 * i_1

print(total)
