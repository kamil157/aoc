from collections import deque


with open('2022/inputs/day18.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def parse():
    return set(tuple(int(n) for n in line.split(',')) for line in lines)


def neighbors(node):
    x, y, z = node
    return [(x, y, z - 1), (x, y, z + 1), (x, y - 1, z), (x, y + 1, z), (x - 1, y, z), (x + 1, y, z)]


def part1():
    cubes = parse()
    return sum(neighbor not in cubes for node in cubes for neighbor in neighbors(node))


print(part1())


def part2():
    cubes = parse()
    total = 0
    start = min(min(d for d in cube) for cube in cubes) - 1
    end = max(max(d for d in cube) for cube in cubes) + 1
    queue = deque([(start, start, start)])
    visited = set()

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)

        for neighbor in neighbors(node):
            if neighbor in cubes:
                total += 1
            elif all(start <= d <= end for d in neighbor):
                queue.append(neighbor)
    return total


print(part2())
