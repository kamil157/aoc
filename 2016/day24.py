from collections import deque
from itertools import pairwise, permutations


with open('2016/inputs/day24.txt', encoding="utf-8") as f:
    lines = f.read().strip().split("\n")


def part1(finish):
    grid = {}
    numbers = {}
    for y, row in enumerate(lines):
        for x, tile in enumerate(row):
            grid[x+y*1j] = tile
            if tile.isdigit():
                numbers[x+y*1j] = int(tile)
                grid[x+y*1j] = int(tile)

    distances = {}
    for start, value in numbers.items():
        queue = deque([(start, 0)])
        visited = set()
        while queue:
            pos, dist = queue.popleft()
            if pos in visited:
                continue
            visited.add(pos)
            if pos in numbers:
                if pos != start:
                    distances[(grid[pos], value)] = dist
            for d in [-1, 1, -1j, 1j]:
                n = pos + d
                if grid.get(n, "#") != "#":
                    queue.append((n, dist + 1))

    results = []
    for p in permutations(range(1, max(numbers.values()) + 1)):
        steps = 0
        for n, m in pairwise([0] + list(p) + finish):
            steps += distances[(n, m)]
        results.append(steps)

    return min(results)


print(part1([]))
print(part1([0]))
