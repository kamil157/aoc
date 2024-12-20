from math import inf


with open('2024/inputs/day20.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def bfs(start, end, grid):
    queue = [(start, 0)]
    visited = {start}
    while queue:
        (y, x), dist = queue.pop(0)
        if (y, x) == end:
            return dist
        visited.add((y, x))
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and (ny, nx) not in visited and grid[ny][nx] != "#":
                queue.append(((ny, nx), dist + 1))
    return inf


def solve():
    start = end = (0, 0)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "S":
                start = (y, x)
            elif c == "E":
                end = (y, x)

    grid = [list(line) for line in lines]

    default = bfs(start, end, grid)

    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "#":
                grid[y][x] = "."
                if default - bfs(start, end, grid) >= 100:
                    count += 1
                grid[y][x] = "#"

    return count


print(solve())
