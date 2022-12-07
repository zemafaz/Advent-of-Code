
f = open("./input", "r")

sum = 0

while True:
    part_1 = set(f.readline()[:-1])
    if not part_1:
        break
    part_2 = set(f.readline()[:-1])
    part_3 = set(f.readline()[:-1])
    
    inter = part_1.intersection(part_2).intersection(part_3)
    # print(f"Part_1: {part_1}\nPart_2: {part_2}\nPart_3: {part_3}\nInter: {inter}")
    
    if len(inter) != 1:
        raise Exception("Interception Error")
    i = inter.pop()
    if ord(i) >= ord("a"):
        sum += ord(i) - ord("a") + 1
    else:
        sum += ord(i) - ord("A") + 27

f.close()

print(sum)
