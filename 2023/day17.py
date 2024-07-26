
from heapq import heappop, heappush
from math import inf

with open('2023/inputs/day17.txt') as f:
    lines = f.read().strip().split('\n')


def part2(least, most):
    g = [[int(n) for n in line] for line in lines]
    end = (len(lines) - 1, len(lines[0]) - 1)
    q = []
    dist = {}
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dy, dx in directions:
        start = (0, 0, dy, dx)
        dist[start] = 0
        heappush(q, (0, start))

    while q:
        cost, u = heappop(q)
        y, x, dy, dx = u
        if (y, x) == end:
            return cost

        alt = dist.get(u, inf)
        for i in range(1, most + 1):
            ny, nx = y + dy * i, x + dx * i
            if 0 <= ny < len(g) and 0 <= nx < len(g[0]):
                alt += g[ny][nx]
                if i >= least:
                    for ndy, ndx in [(dx, dy), (-dx, -dy)]:
                        v = (ny, nx, ndy, ndx)
                        if alt < dist.get(v, inf):
                            dist[v] = alt
                            heappush(q, (alt, v))


print(part2(1, 3))
print(part2(4, 10))
