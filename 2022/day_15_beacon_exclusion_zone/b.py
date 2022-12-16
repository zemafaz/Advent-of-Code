import re

def solution(file_path: str, limit: int) -> int:
    with open(file_path, "r") as file:
        sensors: dict[tuple[int, int], int] = {}
        pos_coef: set[int] = set()
        neg_coef: set[int] = set()
        for line in file:
            coordinates: list[str] = [re.findall(r"-?\d+", w)[0] for w in filter(lambda w: w[1] == "=", line.split())]
            sensor: tuple[int, int] = (int(coordinates[0]), int(coordinates[1]))
            beacon: tuple[int, int] = (int(coordinates[2]), int(coordinates[3]))
            distance: int = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
            
            sensors[sensor] = distance
            pos_coef.add(sensor[1] - sensor[0] - distance - 1)
            pos_coef.add(sensor[1] - sensor[0] + distance + 1)
            neg_coef.add(sensor[1] + sensor[0] + distance + 1)
            pos_coef.add(sensor[1] + sensor[0] - distance - 1)
            
        for pos in pos_coef:
            for neg in neg_coef:
                interception: tuple[int, int] = ((neg - pos) // 2, (neg + pos) // 2)
                if all(0 <= coord <= limit for coord in interception):
                    if all(abs(sensor[0] - interception[0]) + abs(sensor[1] - interception[1]) > sensors[sensor] for sensor in sensors.keys()):
                        return 4_000_000 * interception[0] + interception[1]

                
        raise Exception("There is no undetected space")

if __name__ == "__main__":
    output: int = 56000011
    res: int = solution("./test", 20)
    
    if res != output:
        print(f"\nDid not pass test:\n\tExpected {output}, returned {res}")
    else:
        print("\nPassed test!")

    res = solution("./input", 4_000_000)
    print(f"\nSolution for input: {res}")
