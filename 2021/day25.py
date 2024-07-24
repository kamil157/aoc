from copy import deepcopy
from itertools import count

with open('2021/inputs/day25.txt', encoding="utf-8") as f:
    lines = f.read().strip().splitlines()


def part1():
    grid = [list(line) for line in lines]
    h = len(grid)
    w = len(grid[0])

    for steps in count(1):
        moved = False

        new_grid = deepcopy(grid)
        for y, line in enumerate(grid):
            for x, fish in enumerate(line):
                if fish == ">":
                    if grid[y][(x + 1) % w] == ".":
                        moved = True
                        new_grid[y][(x + 1) % w] = ">"
                        new_grid[y][x] = "."
        grid = new_grid

        new_grid = deepcopy(grid)
        for y, line in enumerate(grid):
            for x, fish in enumerate(line):
                if fish == "v":
                    if grid[(y + 1) % h][x] == ".":
                        moved = True
                        new_grid[(y + 1) % h][x] = "v"
                        new_grid[y][x] = "."

        if not moved:
            return steps
        grid = new_grid


print(part1())
