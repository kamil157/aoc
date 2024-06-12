

with open('2023/inputs/day10.txt') as f:
    lines = f.read().strip().split('\n')


def neighbors(y, x, lines):
    def helper(y, x, lines):
        up, down, left, right = (y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)

        if lines[y][x] == 'S':
            return {up, down, left, right}
        if lines[y][x] == '|':
            return {up, down}
        if lines[y][x] == '-':
            return {left, right}
        if lines[y][x] == 'L':
            return {up, right}
        if lines[y][x] == 'J':
            return {left, up}
        if lines[y][x] == '7':
            return {left, down}
        if lines[y][x] == 'F':
            return {down, right}
        if lines[y][x] == '.':
            return {}

    valid = set()
    for neighbor in helper(y, x, lines):
        if (y, x) in helper(*neighbor, lines):
            valid.add(neighbor)
    return valid


def part1():
    queue = []
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == 'S':
                queue.append((y, x, 0))

    distances = {}
    while queue:
        y, x, dist = queue.pop(0)
        distances[(y, x)] = dist

        for neighbor in neighbors(y, x, lines):
            if neighbor not in distances:
                queue.append((*(neighbor), dist + 1))

    return max(distances.values())


print(part1())
