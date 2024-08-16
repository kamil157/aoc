from collections import defaultdict
from math import sqrt, atan2, pi

with open('2019/inputs/day10.txt') as f:
    input = f.read()


def round(n):
    return float("{0:.3f}".format(n))


def part1(s):
    nodes = set()
    lines = s.split()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '#':
                nodes.add((j, i))

    angles = defaultdict(set)
    for node in nodes:
        for other in nodes:
            if node != other:
                x = node[0] - other[0]
                y = node[1] - other[1]
                d = sqrt(x * x + y * y)
                angle = (round(x / d), round(y / d))
                angles[node].add(angle)

    best = max(angles.values(), key=len)
    return len(best)


print(part1(input))


def part2(s):
    nodes = set()
    lines = s.split()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '#':
                nodes.add((j, i))

    angles = defaultdict(set)
    for node in nodes:
        for other in nodes:
            if node != other:
                x = node[0] - other[0]
                y = node[1] - other[1]
                angle = atan2(y, x)  # could divide by gcd(x,y) instead
                angles[node].add(angle)

    best = max(angles.items(), key=lambda s: len(s[1]))

    # start laser from best asteroid

    node = best[0]  # might be bugged

    targets = defaultdict(list)
    for other in nodes:
        if node != other:
            x = node[0] - other[0]
            y = node[1] - other[1]
            angle = atan2(y, x)
            targets[angle].append(other)

    def distance(p):
        x = node[0] - p[0]
        y = node[1] - p[1]
        d = sqrt(x * x + y * y)
        return d

    for angle, l in targets.items():
        targets[angle] = sorted(l, key=distance)

    ordered = []
    for angle, l in sorted(targets.items()):
        if angle >= pi / 2:
            ordered.append(l)

    for angle, l in sorted(targets.items()):
        if angle < pi / 2:
            ordered.append(l)

    for i in range(len(ordered)):
        ordered[i] = iter(ordered[i])
    destroyed = []
    i = 0
    while len(destroyed) < len(nodes) - 1:
        try:
            destroyed.append(next(ordered[i % len(ordered)]))
        except StopIteration:
            pass
        i += 1

    return destroyed[199][0] * 100 + destroyed[199][1]


print(part2(input))
