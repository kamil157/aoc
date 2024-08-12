from collections import defaultdict
from functools import cache
from itertools import product


with open('2023/inputs/day22.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


@cache
def projection(brick):
    result = set()
    for x in range(brick[0][0], brick[1][0] + 1):
        for y in range(brick[0][1], brick[1][1] + 1):
            result.add((x, y))
    return result


def settle(bricks):
    heights = defaultdict(int)
    dropped = []

    for brick in bricks:
        (x0, y0, z0), (x1, y1, z1) = brick

        h = max(heights[p] for p in projection(brick))
        end_h = h + z1 - z0 + 1
        brick_dropped = (x0, y0, h + 1), (x1, y1, end_h)
        for p in projection(brick):
            heights[p] = end_h

        dropped.append(brick_dropped)

    return dropped


def parse():
    bricks = []
    for line in lines:
        left, right = line.split("~")
        start = tuple(int(n) for n in left.split(","))
        end = tuple(int(n) for n in right.split(","))
        bricks.append((start, end))
    return sorted(bricks, key=lambda b: b[0][2])


def graph(bricks):
    supported_by = {d: set() for d in bricks}
    supports = {d: set() for d in bricks}
    for brick, other in product(bricks, repeat=2):
        if brick[0][2] - 1 == other[1][2] and projection(brick) & projection(other):
            supported_by[brick].add(other)
            supports[other].add(brick)
    return supported_by, supports


def part1():
    bricks = parse()
    bricks = settle(bricks)
    supported_by, supports = graph(bricks)

    def dfs():
        removed = set()
        queue = [start]
        while queue:
            brick = queue.pop()
            removed.add(brick)

            for other in supports[brick]:
                if supported_by[other] and supported_by[other] <= removed:
                    queue.append(other)

        return removed

    safe = 0
    chain = 0
    for start in bricks:
        removed = dfs()
        if len(removed) == 1:
            safe += 1
        chain += len(removed) - 1
    return safe, chain


print(part1())
