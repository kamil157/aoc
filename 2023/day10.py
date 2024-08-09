

from collections import deque


with open('2023/inputs/day10.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def neighbors(y, x):
    def helper(y, x):
        up, down, left, right = (y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)

        match lines[y][x]:
            case 'S': return {up, down, left, right}
            case '|': return {up, down}
            case '-': return {left, right}
            case 'L': return {up, right}
            case 'J': return {left, up}
            case '7': return {left, down}
            case 'F': return {down, right}
            case '.': return {}

    valid = set()
    for neighbor in helper(y, x):
        if (y, x) in helper(*neighbor):
            valid.add(neighbor)
    return valid


def part1():
    queue = deque()
    for y, line in enumerate(lines):
        for x, tile in enumerate(line):
            if tile == 'S':
                queue.append((y, x, 0))

    distances = {}
    while queue:
        y, x, dist = queue.popleft()
        distances[(y, x)] = dist

        for neighbor in neighbors(y, x):
            if neighbor not in distances:
                queue.append((*(neighbor), dist + 1))

    return max(distances.values())


print(part1())
