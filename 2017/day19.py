from string import ascii_uppercase


with open('2017/inputs/day19.txt', encoding="utf-8") as f:
    lines = f.read().split('\n')


def part1():
    path = ""
    x = lines[0].index("|")
    y = 0

    dx = 0
    dy = 1
    steps = 1
    while lines[y + dy][x + dx] != " ":
        while (tile := lines[y][x]) != "+":
            if tile in ascii_uppercase:
                path += tile
                if lines[y + dy][x + dx] == " ":
                    return path, steps
            y += dy
            x += dx
            steps += 1
        dx, dy = dy, dx
        if lines[y + dy][x + dx] == " ":
            dx, dy = -dx, -dy
        y += dy
        x += dx
        steps += 1
    return path, steps


print(part1())
