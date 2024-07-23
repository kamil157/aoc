from heapq import heappop, heappush
from math import inf
from parse import parse

with open('2018/inputs/day22.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def cave(depth, w, h, tx, ty):
    grid = [[""] * w for _ in range(h)]
    geologic = [[0] * w for _ in range(h)]

    def erosion(y, x):
        return (geologic[y][x] + depth) % 20183

    for y in range(h):
        for x in range(w):
            if x == 0 and y == 0:
                geologic[y][x] = 0
            elif x == tx and y == ty:
                geologic[y][x] = 0
            elif y == 0:
                geologic[y][x] = x * 16807
            elif x == 0:
                geologic[y][x] = y * 48271
            else:
                geologic[y][x] = erosion(y, x - 1) * erosion(y - 1, x)

            e = erosion(y, x)
            if e % 3 == 0:
                grid[y][x] = "."
            elif e == 1:
                grid[y][x] = "="
            elif e == 2:
                grid[y][x] = "|"
    return grid


def part1():
    depth = parse("depth: {:d}", lines[0])[0]
    tx, ty = parse("target: {:d},{:d}", lines[1])
    w = tx + 1
    h = ty + 1

    risk = 0
    grid = cave(depth, w, h, tx, ty)

    for y in range(h):
        for x in range(w):
            if grid[y][x] == "=":
                risk += 1
            elif grid[y][x] == "|":
                risk += 2

    return risk


print(part1())


def tools(node):
    if node == ".":
        return ["climb", "torch"]
    elif node == "=":
        return ["climb", "neither"]
    else:
        return ["torch", "neither"]


def dijkstra(g, start, end):
    height = len(g)
    width = len(g[0])
    h = []
    dist = {start: 0}
    heappush(h, (0, start))
    for y in range(height):
        for x in range(width):
            for tool in ["climb", "torch", "neither"]:
                if (y, x, tool) != start:
                    dist[(y, x, tool)] = inf
                    heappush(h, (inf, (y, x, tool)))

    while h[0][1:] != end:
        _, state = heappop(h)
        if state == end:
            return dist[end]

        y, x, tool = state
        neighbors = []
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny, nx = y + d[0], x + d[1]
            if 0 <= ny < height and 0 <= nx < width and tool in tools(g[ny][nx]):
                neighbors.append((dist[state] + 1, (ny, nx, tool)))

        for new_tool in ["climb", "torch", "neither"]:
            if new_tool != tool:
                neighbors.append((dist[state] + 7, (y, x, new_tool)))

        for alt, new_state in neighbors:
            if alt < dist[new_state]:
                dist[new_state] = alt
                heappush(h, (alt, new_state))

    return dist[end]


def part2():
    depth = parse("depth: {:d}", lines[0])[0]
    tx, ty = parse("target: {:d},{:d}", lines[1])

    w = tx * 3
    h = ty * 3

    start = (0, 0, "torch")
    end = (ty, tx, "torch")
    return dijkstra(cave(depth, w, h, tx, ty), start, end)


print(part2())
