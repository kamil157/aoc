import re

with open('2022/inputs/day15.txt') as f:
    lines = f.read().strip().split('\n')


def part1():
    y = 10
    row = set()
    for line in lines:
        number = "(-?\d+)"
        m = re.match(
            f"Sensor at x={number}, y={number}: closest beacon is at x={number}, y={number}", line)
        sx, sy, bx, by = [int(m.group(i)) for i in range(1, 5)]

        dist_sb = abs(sx - bx) + abs(sy - by)
        dist_sx = dist_sb - abs(sy - y)
        if dist_sx < 0:
            continue
        for x in range(sx - dist_sx, sx + dist_sx + 1):
            row.add(x)
        if by == y:
            row.remove(bx)
    return len(row)


print(part1())


def part2():
    beacons = []
    for line in lines:
        number = "(-?\d+)"
        m = re.match(
            f"Sensor at x={number}, y={number}: closest beacon is at x={number}, y={number}", line)
        sx, sy, bx, by = [int(m.group(i)) for i in range(1, 5)]
        beacons.append((sx, sy, bx, by))

    limit = 4000000
    for y in range(0, limit + 1):
        row = []
        for sx, sy, bx, by in beacons:
            dist_sb = abs(sx - bx) + abs(sy - by)
            dist_sx = dist_sb - abs(sy - y)
            if dist_sx < 0:
                continue

            l = max(sx - dist_sx, 0)
            r = min(sx + dist_sx, limit)
            row.append((l, r))
        row = sorted(row)

        start = 0
        for l, r in row:
            if l > start:
                return start * 4000000 + y
            else:
                start = max(start, r + 1)


print(part2())
