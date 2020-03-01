from collections import defaultdict
from math import *

input = """##.###.#.......#.#....#....#..........#.
....#..#..#.....#.##.............#......
...#.#..###..#..#.....#........#......#.
#......#.....#.##.#.##.##...#...#......#
.............#....#.....#.#......#.#....
..##.....#..#..#.#.#....##.......#.....#
.#........#...#...#.#.....#.....#.#..#.#
...#...........#....#..#.#..#...##.#.#..
#.##.#.#...#..#...........#..........#..
........#.#..#..##.#.##......##.........
................#.##.#....##.......#....
#............#.........###...#...#.....#
#....#..#....##.#....#...#.....#......#.
.........#...#.#....#.#.....#...#...#...
.............###.....#.#...##...........
...#...#.......#....#.#...#....#...#....
.....#..#...#.#.........##....#...#.....
....##.........#......#...#...#....#..#.
#...#..#..#.#...##.#..#.............#.##
.....#...##..#....#.#.##..##.....#....#.
..#....#..#........#.#.......#.##..###..
...#....#..#.#.#........##..#..#..##....
.......#.##.....#.#.....#...#...........
........#.......#.#...........#..###..##
...#.....#..#.#.......##.###.###...#....
...............#..#....#.#....#....#.#..
#......#...#.....#.#........##.##.#.....
###.......#............#....#..#.#......
..###.#.#....##..#.......#.............#
##.#.#...#.#..........##.#..#...##......
..#......#..........#.#..#....##........
......##.##.#....#....#..........#...#..
#.#..#..#.#...........#..#.......#..#.#.
#.....#.#.........#............#.#..##.#
.....##....#.##....#.....#..##....#..#..
.#.......#......#.......#....#....#..#..
...#........#.#.##..#.#..#..#........#..
#........#.#......#..###....##..#......#
...#....#...#.....#.....#.##.#..#...#...
#.#.....##....#...........#.....#...#..."""


def asteroids(s):
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
                # print(node, other, x, y, angle)
                angles[node].add(angle)
        # print(len(angles[node]))

    best = max(angles.items(), key=lambda s: len(s[1]))
    print(best[0], len(best[1]))

    # start laser from best asteroid

    node = best[0]  # might be bugged
    # hack
    # node = (8, 3)

    targets = defaultdict(list)
    for other in nodes:
        if node != other:
            x = node[0] - other[0]
            y = node[1] - other[1]
            angle = atan2(y, x)
            # print(node, other, x, y, angle)
            targets[angle].append(other)

    def distance(p):
        x = node[0] - p[0]
        y = node[1] - p[1]
        d = sqrt(x * x + y * y)
        # print(p, d)
        return d

    print('targets', targets)
    for angle, l in targets.items():
        targets[angle] = sorted(l, key=distance)

    print('targets', targets)

    ordered = []
    for angle, l in sorted(targets.items()):
        if angle >= pi / 2:
            ordered.append(l)
            print(angle, l)

    for angle, l in sorted(targets.items()):
        if angle < pi / 2:
            ordered.append(l)
            print(angle, l)

    for i in range(len(ordered)):
        ordered[i] = iter(ordered[i])
    # print(ordered)
    destroyed = []
    i = 0
    while len(destroyed) < len(nodes) - 1:
        # print(len(destroyed))
        try:
            destroyed.append(next(ordered[i % len(ordered)]))
        except StopIteration:
            pass
        i += 1

    print('result:', destroyed)

    return destroyed


print(asteroids(""".#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.....X...###..
..#.#.....#....##"""))

print(asteroids(""".#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##""")[199])

print(asteroids(input)[199])