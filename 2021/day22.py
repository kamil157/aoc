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
