
from parse import parse

with open('2021/inputs/day17.txt', encoding="utf-8") as f:
    lines = f.read().strip()

min_x, max_x, min_y, max_y = parse(
    "target area: x={:d}..{:d}, y={:d}..{:d}", lines)


def shoot(velocity):
    x, y = (0, 0)
    dx, dy = velocity

    highest = 0
    while x <= max_x and y >= min_y:
        x += dx
        y += dy
        highest = max(highest, y)
        if dx > 0:
            dx -= 1
        if dx < 0:
            dx += 1
        dy -= 1
        if min_x <= x <= max_x and min_y <= y <= max_y:
            return True, highest
    return False, 0


def part1():
    return max(shoot((x, y))[1] for x in range(100) for y in range(100))


print(part1())


def part2():
    return sum(shoot((x, y))[0] for x in range(1000) for y in range(-100, 100))


print(part2())
