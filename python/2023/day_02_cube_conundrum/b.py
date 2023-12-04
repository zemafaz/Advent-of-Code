def parse_draw(draw: str) -> dict[str, int]:
    draw = draw.split(",")
    draw_details = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for ball in draw:
        info = ball.strip().partition(" ")
        draw_details[info[2]] = int(info[0])
    return draw_details


def parse_line(draws: str) -> dict:
    balls: dict[str, int] = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    while True:
        draws = draws.partition(";")
        draw = parse_draw(draws[0])
        for color in balls:
            if draw[color] > balls[color]:
                balls[color] = draw[color]
        if draws[1] == "":
            break
        draws = draws[2]
    return balls["red"] * balls["green"] * balls["blue"]


with open("./input") as file:
    res: int = 0

    while line := file.readline():
        game_rest: list[str] = line.partition(":")
        res += parse_line(game_rest[2])

    print(res)
