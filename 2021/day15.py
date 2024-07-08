import heapq
import math


with open('2021/inputs/day15.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def dijkstra(g, end):
    h = []
    inf = math.inf
    dist = {(0, 0): 0}
    heapq.heappush(h, (0, 0, 0))
    for (y, x) in g.keys():
        if (y, x) != (0, 0):
            dist[(y, x)] = inf
            heapq.heappush(h, (inf, y, x))

    while h:
        _, y, x = heapq.heappop(h)
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny, nx = y + d[0], x + d[1]
            if (ny, nx) in g:
                alt = dist[(y, x)] + g[(ny, nx)]
                if alt < dist[(ny, nx)]:
                    dist[(ny, nx)] = alt
                    heapq.heappush(h, (alt, ny, nx))

    return dist[end]


def part1(mult):
    g = {}
    h, w = len(lines), len(lines[0])
    for i in range(mult):
        for j in range(mult):
            for y, line in enumerate(lines):
                for x, risk in enumerate(line):
                    risk = (int(risk) + i + j)
                    if risk > 9:
                        risk -= 9
                    g[(i * h + y, j * w + x)] = risk

    return dijkstra(g, (h * mult - 1, w * mult - 1))


print(part1(1))
print(part1(5))
