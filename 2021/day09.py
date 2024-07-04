from collections import deque


with open('2021/inputs/day09.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


diffs = [-1, 1, 1j, -1j]


def parse():
    return {x + y*1j: int(d)
            for y, line in enumerate(lines)
            for x, d in enumerate(line)}


def part1():
    grid = parse()
    risk = 0
    for pos, n in grid.items():
        neighbors = [grid.get(pos + d, 10) for d in diffs]
        if n < min(neighbors):
            risk += n + 1

    return risk


print(part1())


def basin_size(grid, pos):
    size = 0
    visited = set()
    stack = deque([pos])
    while stack:
        pos = stack.popleft()
        if pos in visited:
            continue
        visited.add(pos)
        if grid[pos] < 9:
            size += 1
        for d in diffs:
            if grid.get(pos + d, 9) < 9:
                stack.append(pos + d)
    return size


def part2():
    grid = parse()
    basins = []
    for pos, n in grid.items():
        neighbors = [grid.get(pos + d, 10) for d in diffs]
        if n < min(neighbors):
            basins.append(basin_size(grid, pos))

    basins = sorted(basins)
    return basins[-1] * basins[-2] * basins[-3]


print(part2())
