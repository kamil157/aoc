
with open('2022/inputs/day12.txt') as f:
    lines = f.read().strip().split('\n')


def solve(starts, hill, end):
    paths = []
    for start in starts:
        q = [(start[0], start[1], 0)]
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()

        while q:
            y, x, steps = q.pop(0)

            if (y, x) in visited:
                continue
            visited.add((y, x))

            if (y, x) == end:
                paths.append(steps)
                break

            for dy, dx in dirs:
                if (y + dy, x + dx) in hill:
                    if ord(hill[(y + dy, x + dx)]) - ord(hill[(y, x)]) <= 1:
                        q.append((y + dy, x + dx, steps + 1))
    return min(paths)


def part1(part2):
    hill = {}
    start = []
    end = None
    for y, line in enumerate(lines):
        for x, elevation in enumerate(line):
            hill[(y, x)] = elevation
            if elevation == "S":
                start.append((y, x))
                hill[(y, x)] = "a"
            if elevation == "E":
                end = (y, x)
                hill[(y, x)] = "z"
            if part2 and elevation == "a":
                start.append((y, x))
    return solve(start, hill, end)


print(part1(False))
print(part1(True))
