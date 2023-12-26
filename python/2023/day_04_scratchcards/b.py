import re
from heapq import heappush, heappop

def main() -> int:

    with open("./input") as file:
        res: int = 0
        stack: list[int] = [1]

        for line in file:
            card = int(re.match(r"Card +(\d+):", line).group(1))
            common: int | None = None
            
            while len(stack) != 0 and card == stack[0]:
                res += 1
                print("--------")
                print(f"Playing card {card}")
                heappop(stack)
                if common is not None:
                    res += common
                    for i in range(card + 1, card + common + 1):
                        print(f"\tPushed {i}")
                        heappush(stack, i)
                    continue
                round = line[line.index(":") + 1:]
                round = round.partition("|")
                winning_set: set[int] = set(map(lambda x: int(x),
                                            re.split("\s+", round[0].strip())))
                my_hand: set[int] = set(map(lambda x: int(x),
                                        re.split("\s+", round[2].strip())))
                common: int = len(winning_set.intersection(my_hand))
                print(f"\tNumber of cards added: {common}")
                if common != 0:
                    for i in range(card + 1, card + common + 1):
                        print(f"\tPushed {i}")
                        heappush(stack, i)

    return res


if __name__ == "__main__":
    print(main())
