import re

def main() -> int:

    with open("./input") as file:
        res: int = 0
        i: int = 1

        for line in file:
            line = line[line.index(":") + 1:]
            line = line.partition("|")
            winning_set: set[int] = set(map(lambda x: int(x),
                                        re.split("\s+", line[0].strip())))
            my_hand: set[int] = set(map(lambda x: int(x),
                                    re.split("\s+", line[2].strip())))
            common: int = len(winning_set.intersection(my_hand))
            print("-------")
            print(f"Card {i}:\n\tWon {common} cards")
            res += 2 ** (common - 1) if common != 0 else 0
            i += 1

    return res


if __name__ == "__main__":
    print(main())
