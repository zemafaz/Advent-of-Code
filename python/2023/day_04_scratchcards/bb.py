import re
from collections import defaultdict

def main() -> int:

    with open("./input") as file:
        counter: defaultdict = defaultdict(lambda: 1)

        for line in file:
            card = int(re.match(r"Card +(\d+):", line).group(1))

            line = line[line.index(":") + 1:]
            line = line.partition("|")
            winning_set: set[int] = set(map(lambda x: int(x),
                                        re.split("\s+", line[0].strip())))
            my_hand: set[int] = set(map(lambda x: int(x),
                                    re.split("\s+", line[2].strip())))
            common: int = len(winning_set.intersection(my_hand))
            print("-------")
            print(f"Card {card}:\n\tWon {common} cards")
            for i in range(card + 1, card + common + 1):
                counter[i] += counter[card]


    return sum(counter.values())


if __name__ == "__main__":
    print(main())
