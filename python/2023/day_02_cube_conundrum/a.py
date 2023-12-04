
RESULT = {
        "red": 12,
        "green": 13,
        "blue": 14
}


def parse_draw(draw: str) -> bool:
    draw = draw.split(",")

    for ball in draw:
        info = ball.strip().partition(" ")
        if int(info[0]) > RESULT[info[2]]:
            return False
    return True


def parse_line(draws: str) -> dict:

    while True:
        draws = draws.partition(";")
        if not parse_draw(draws[0]):
            return False
        if draws[1] == "":
            break
        draws = draws[2]
    return True


with open("./input") as file:
    res: int = 0

    while line := file.readline():
        game_rest: list[str] = line.partition(":")
        n_game: int = int(game_rest[0].partition(" ")[2])
        if parse_line(game_rest[2]):
            res += n_game

    print(res)
