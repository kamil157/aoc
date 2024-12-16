import heapq
from math import inf


with open('2024/inputs/day16.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def dijkstra(lines, start, end):
    h = []
    dist = {(start[0], start[1]): 0}
    heapq.heappush(h, (0, start[0], start[1]))

    while h:
        cost, pos, dir = heapq.heappop(h)
        if lines[pos[0]][pos[1]] == "#":
            continue
        if pos == end:
            return cost

        for move in [
            ((pos[0] + dir[0], pos[1] + dir[1]), dir, 1),
            (pos, (dir[1], dir[0]), 1000),
            (pos, (-dir[1], -dir[0]), 1000)
        ]:
            new_pos, new_dir, new_cost = move
            alt = dist.get((pos, dir), inf) + new_cost
            if alt < dist.get((new_pos, new_dir), inf):
                dist[(new_pos, new_dir)] = alt
                heapq.heappush(h, (alt, new_pos, new_dir))


def solve():
    start_pos = end_pos = 0
    start_dir = (0, 1)
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "S":
                start_pos = (y, x)
            if char == "E":
                end_pos = (y, x)

    return dijkstra(lines, (start_pos, start_dir), end_pos)


print(solve())
