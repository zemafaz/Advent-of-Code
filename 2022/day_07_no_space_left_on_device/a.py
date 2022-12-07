from __future__ import annotations

file = open("./input", "r")

class Directory:

    def __init__(self, name: str):
        self.name: str= name
        self.size: int = 0
        self.subd: dict[str, Directory] = {}
        self.processed: bool = False

    def get_total_size_at_most(self, at_most: int) -> int:
        res: int = 0
        if self.size <= at_most:
            res += self.size
        for dir in self.subd:
            res += self.subd[dir].get_total_size_at_most(at_most)
        return res


root: Directory = Directory("/")
stack: list[Directory] = [root]
ls_mode: bool = False
current_size: int = 0

for line in file:
    split: list[str] = line[:-1].split(" ")
    current_dir: Directory = stack[-1]
    if split[0] == "$":

        if ls_mode:
            if not current_dir.processed:
                for dir in stack:
                    dir.size += current_size
                current_size = 0
                current_dir.processed = True
            ls_mode = False

        if split[1] == "cd":
            if split[2] == "/":
                stack = [root]
            if split[2] == "..":
                stack.pop()
            else:
                if split[2] not in current_dir.subd:
                    current_dir.subd[split[2]] = Directory(split[2])
                stack.append(current_dir.subd[split[2]])
        if split[1] == "ls":
            ls_mode = True
    elif ls_mode and not current_dir.processed:
        if split[0] == "dir":
            current_dir.subd[split[1]] = Directory(split[1])
        else:
            current_size += int(split[0])
    else:
        continue

current_dir: Directory = stack[-1]
if ls_mode and not current_dir.processed:
        for dir in stack:
            dir.size += current_size
        current_size = 0
        current_dir.processed = True

print(root.get_total_size_at_most(100000))

file.close()
