from parse import parse
from collections import deque

with open('2018/inputs/day09.txt', encoding="utf-8") as f:
    lines = f.read().strip()


def part1(mult):
    players, points = parse(
        "{:d} players; last marble is worth {:d} points", lines)

    circle = deque([0])
    scores = [0] * players
    for marble in range(1, points * mult):
        player = marble % players
        if marble % 23 == 0:
            circle.rotate(7)
            scores[player] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores)


print(part1(1))
print(part1(100))
