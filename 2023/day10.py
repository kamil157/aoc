

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


def border(y, x):
    result = "|LJ"
    if (y - 1, x) in neighbors(y, x):
        result += "S"
    return result


def part1():
    for y, line in enumerate(lines):
        for x, tile in enumerate(line):
            if tile == 'S':
                start = (y, x)

    queue = deque([(*start, 0)])
    distances = {}
    while queue:
        y, x, dist = queue.popleft()
        distances[(y, x)] = dist

        for neighbor in neighbors(y, x):
            if neighbor not in distances:
                queue.append((*(neighbor), dist + 1))

    borders = border(*start)
    count = 0
    for y, line in enumerate(lines):
        inside = False
        for x, tile in enumerate(line):
            if (y, x) in distances and tile in borders:
                inside = not inside
            if (y, x) not in distances and inside:
                count += 1

    return max(distances.values()), count


print(part1())
