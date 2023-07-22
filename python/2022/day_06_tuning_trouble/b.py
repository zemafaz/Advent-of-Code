from collections import deque

f = open("./input", "r")

i = 0

stack = deque([], 13)

while True:
    i += 1

    char = f.read(1)

    if char == "\n":
        break
    
    if len(stack) < 13:
        try:
            index = stack.index(char)
            while index >= 0:
                stack.popleft()
                index -= 1
            stack.append(char)
        except ValueError:
            stack.append(char)
    else:
        try:
            index = stack.index(char)
            while index >= 0:
                stack.popleft()
                index -= 1
            stack.append(char)
        except:
            break

print(i)

f.close()
