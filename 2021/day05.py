from collections import defaultdict


with open('2021/inputs/day05.txt', encoding="utf-8") as f:
    lines = f.read().split('\n')


def part1(part2):
    grid = defaultdict(int)
    for line in lines:
        p1, p2 = line.split(' -> ')
        x1, y1 = [int(n) for n in p1.split(",")]
        x2, y2 = [int(n) for n in p2.split(",")]

        if x1 == x2:
            start, end = sorted([y1, y2])
            for y in range(start, end + 1):
                grid[x1, y] += 1

        elif y1 == y2:
            start, end = sorted([x1, x2])
            for x in range(start, end + 1):
                grid[x, y1] += 1

        elif part2:
            dx = - (x1 - x2) // abs(x1 - x2)
            dy = - (y1 - y2) // abs(y1 - y2)

            start = (x1, y1)
            end = (x2, y2)

            while start != end:
                grid[start] += 1
                start = (start[0] + dx, start[1] + dy)
            grid[end] += 1

    return len([n for n in grid.values() if n > 1])


print(part1(False))
print(part1(True))
