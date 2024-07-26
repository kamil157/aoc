from collections import deque
from functools import cache


with open('2022/inputs/day24.txt', encoding="utf-8") as f:
    lines = f.read().split('\n')


def init_blizzards():
    blizzards = []
    blizz_directions = {"<": (-1, 0), ">": (1, 0), "v": (0, 1), "^": (0, -1)}
    for y, line in enumerate(lines):
        for x, tile in enumerate(line):
            if tile in blizz_directions:
                blizzards.append(((x, y), blizz_directions[tile]))
    return blizzards


@cache
def get_blizzards(t):
    if t == 0:
        return init_blizzards()

    blizzards = []
    w = len(lines[0])
    h = len(lines)
    for (x, y), (dx, dy) in get_blizzards(t - 1):
        x += dx
        y += dy
        if x == 0:
            x = w - 2
        if x == w - 1:
            x = 1
        if y == 0:
            y = h - 2
        if y == h - 1:
            y = 1
        blizzards.append(((x, y), (dx, dy)))
    return blizzards


@cache
def safe_spots(t):
    safe = set()
    blizzards = [blizzard[0] for blizzard in get_blizzards(t)]
    for y, line in enumerate(lines):
        for x, tile in enumerate(line):
            if tile != "#":
                if (x, y) not in blizzards:
                    safe.add((x, y))
    return safe


def solve():
    w = len(lines[0])
    h = len(lines)

    def bfs(start, end, t):
        seen = set()
        q = deque([(start, t)])
        while q:
            pos, t = q.popleft()
            if (pos, t) in seen:
                continue
            seen.add((pos, t))

            if pos == end:
                return t - 1

            if pos not in safe_spots(t):
                continue

            x, y = pos
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1), (0, 0)]:
                if 0 <= x + dx < w and 0 <= y + dy < h and lines[y + dy][x + dx] != "#":
                    q.append(((x + dx, y + dy), t + 1))

    start = (1, 0)
    end = (w - 2, h - 1)
    t = 0
    part1 = t = bfs(start, end, t)
    t = bfs(end, start, t)
    t = bfs(start, end, t)
    return part1, t


print(solve())
