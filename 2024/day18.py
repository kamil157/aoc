import heapq
from math import inf


with open('2024/inputs/day18.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def dijkstra(obstacles, start, end, size):
    h = []
    dist = {start: 0}
    heapq.heappush(h, (0, start))

    while h:
        cost, pos = heapq.heappop(h)
        if pos[0] < 0 or pos[0] > size or pos[1] < 0 or pos[1] > size or pos in obstacles:
            continue
        if pos == end:
            return cost

        for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_pos, new_cost = (pos[0] + dir[0], pos[1] + dir[1]), 1
            alt = dist.get(pos, inf) + new_cost
            if alt < dist.get(new_pos, inf):
                dist[new_pos] = alt
                heapq.heappush(h, (alt, new_pos))
    return inf


def part1():
    size = 70
    obstacles = set()
    for line in lines[:1024]:
        obstacles.add(tuple(int(n) for n in line.split(",")))

    return dijkstra(obstacles, (0, 0), (size, size), size)


print(part1())


def part2():
    size = 70
    obstacles = set()
    for bytes, line in enumerate(lines):
        obstacles.add(tuple(int(n) for n in line.split(",")))
        if bytes > 1024 and dijkstra(obstacles, (0, 0), (size, size), size) == inf:
            return lines[bytes]


print(part2())
