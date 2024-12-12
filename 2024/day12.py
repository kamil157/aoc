from collections import defaultdict
from math import inf

with open('2024/inputs/day12.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def dfs(lines, y, x, visited, c, area, perimeter):
    if (y, x) in visited or lines[y][x] != c:
        return
    visited.add((y, x))
    area.add((y, x))
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if y + dy < 0 or y + dy >= len(lines) or x + dx < 0 or x + dx >= len(lines[0]):
            perimeter.add((y + dy, x + dx, (dy, dx)))
        else:
            if lines[y + dy][x + dx] != c:
                perimeter.add((y + dy, x + dx, (dy, dx)))
            dfs(lines, y + dy, x + dx, visited, c, area, perimeter)


def sides(perimeter):
    by_direction = defaultdict(list)
    for y, x, (dy, dx) in perimeter:
        if dx == 0:
            by_direction[(dy, dx, y)].append(x)
        else:
            by_direction[(dy, dx, x)].append(y)

    count = 0
    for points in by_direction.values():
        current = -inf
        for n in sorted(points):
            if n != current + 1:
                count += 1
            current = n
    return count


def solve():
    visited = set()
    part1 = part2 = 0
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if (y, x) in visited:
                continue
            area = set()
            perimeter = set()
            dfs(lines, y, x, visited, c, area, perimeter)
            part1 += len(area) * len(perimeter)
            part2 += len(area) * sides(perimeter)
    return part1, part2


print(solve())
