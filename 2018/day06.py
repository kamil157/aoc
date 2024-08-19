from collections import defaultdict
from operator import itemgetter
from parse import findall

with open('2018/inputs/day06.txt', encoding="utf-8") as f:
    lines = f.read()


def solve():
    points = [(x, y) for (x, y) in findall("{:d}, {:d}", lines)]
    min_x = min(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_x = max(p[0] for p in points)
    max_y = max(p[1] for p in points)

    areas = defaultdict(list)
    infinite = defaultdict(bool)
    part2 = 0
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            distances = {p: abs(x - p[0]) + abs(y - p[1]) for p in points}
            closest = min(distances.items(), key=itemgetter(1))
            if x in [min_x, max_x] or y in [min_y, max_y]:
                infinite[closest[0]] = True

            if sum(distances.values()) < 10000:
                part2 += 1

            del distances[closest[0]]
            if closest[1] in distances.values():
                continue

            if not infinite[closest[0]]:
                areas[closest[0]].append((x, y))

    return max(len(area) for area in areas.values()), part2


print(solve())
