from collections import Counter
from parse import search

with open('2021/inputs/day22.txt', encoding="utf-8") as f:
    lines = f.read().strip().splitlines()


def part1():
    grid = set()
    for line in lines:
        on = line.startswith("on")
        cube = search("x={:d}..{:d},y={:d}..{:d},z={:d}..{:d}", line)

        if all(-50 <= n <= 50 for n in cube):
            for x in range(cube[0], cube[1] + 1):
                for y in range(cube[2], cube[3] + 1):
                    for z in range(cube[4], cube[5] + 1):
                        if on:
                            grid.add((x, y, z))
                        else:
                            grid.discard((x, y, z))
    return len(grid)


print(part1())


def part2():
    cubes = Counter()
    for line in lines:
        current = Counter()
        sign = 1 if line.startswith("on") else -1
        cube = search("x={:d}..{:d},y={:d}..{:d},z={:d}..{:d}", line)

        for prev, prev_sign in cubes.items():
            i = (
                max(prev[0], cube[0]), min(prev[1], cube[1]),
                max(prev[2], cube[2]), min(prev[3], cube[3]),
                max(prev[4], cube[4]), min(prev[5], cube[5])
            )
            if i[0] <= i[1] and i[2] <= i[3] and i[4] <= i[5]:
                current[i] -= prev_sign
        if sign == 1:
            current[cube] += sign
        cubes.update(current)

    return sum((c[1] - c[0] + 1) * (c[3] - c[2] + 1) * (c[5] - c[4] + 1) * count for c, count in cubes.items())


print(part2())
