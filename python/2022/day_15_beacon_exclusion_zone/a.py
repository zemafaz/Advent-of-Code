import re

def solution(file_path: str, scan_y: int) -> int:
    with open(file_path, "r") as file:
        occupied: set[int] = set()
        
        for line in file:
            coordinates: list[str] = [re.findall(r"-?\d+", w)[0] for w in filter(lambda w: w[1] == "=", line.split())]
            sensor: tuple[int, int] = (int(coordinates[0]), int(coordinates[1]))
            beacon: tuple[int, int] = (int(coordinates[2]), int(coordinates[3]))
            distance: int = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

            if (sensor[1] + distance < scan_y and
                    sensor[1] - distance > scan_y):
                continue

            aditional_side: int = sensor[1] + distance - scan_y if scan_y > sensor[1] else scan_y - (sensor[1] - distance)
            occupied.update(x for x in range(sensor[0] - aditional_side, sensor[0] + aditional_side))

        return len(occupied)

if __name__ == "__main__":
    output: int = 26
    res: int = solution("./test", 10)
    
    if res != output:
        print(f"\nDid not pass test:\n\tExpected {output}, returned {res}")
    else:
        print("\nPassed test!")

    res = solution("./input", 2_000_000)
    print(f"\nSolution for input: {res}")
