with open('2021/inputs/day11.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def parse():
    grid = {}
    for y, line in enumerate(lines):
        for x, n in enumerate(line):
            grid[x + y*1j] = int(n)
    return grid


def step(grid):
    stack = []
    for k, v in grid.items():
        grid[k] += 1
        if grid[k] > 9:
            stack.append(k)

    visited = set()
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)

        for d in [-1, 1, -1j, 1j, -1-1j, -1+1j, 1-1j, 1+1j]:
            neighbor = node + d
            if neighbor in grid:
                grid[neighbor] += 1
                if grid[neighbor] > 9:
                    stack.append(neighbor)

    for k, v in grid.items():
        if v > 9:
            grid[k] = 0


def part1():
    grid = parse()
    total = 0
    for _ in range(100):
        step(grid)
        total += list(grid.values()).count(0)
    return total


print(part1())


def part2():
    grid = parse()
    t = 0
    while not all(n == 0 for n in grid.values()):
        step(grid)
        t += 1
    return t


print(part2())
