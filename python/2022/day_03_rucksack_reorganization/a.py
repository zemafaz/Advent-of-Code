f = open("./input", "r")

sum = 0

for line in f:
    part_1 = set(line[:len(line)//2])
    part_2 = set(line[len(line)//2:-1])
    inter = part_1.intersection(part_2)
    # print(f"Line: {line[:-1]}\nPart_1: {part_1}\nPart_2: {part_2}\nInterseption: {inter}")
    for i in inter:
        if ord(i) >= ord("a"):
            sum += ord(i) - ord("a") + 1
        else:
            sum += ord(i) - ord("A") + 27

f.close()

print(sum)
