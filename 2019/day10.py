from collections import defaultdict
from math import sqrt, atan2

with open('2019/inputs/day10.txt') as f:
    input = f.read()


def round(n):
    return float("{0:.3f}".format(n))


def asteroids(s):
    nodes = set()
    lines = s.split()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            # print(i, j)
            if lines[i][j] == '#':
                nodes.add((j, i))
    print(nodes)

    angles = defaultdict(set)
    for node in nodes:
        for other in nodes:
            if node != other:
                # try:
                #     angle = (node[0] - other[0] / node[0] - other[0], node[1] - other[1] / node[0] - other[0])
                # except ZeroDivisionError:
                #     angle = (node[0] - other[0] / node[1] - other[1], node[1] - other[1] / node[1] - other[1])
                # print(node[0], other[0], node[1], other[1])
                x = node[0] - other[0]
                y = node[1] - other[1]

                # better normalization:
                # d = sqrt(x * x + y * y)
                # (x / d, y / d)

                d = sqrt(x * x + y * y)

                angle = (round(x / d), round(y / d))

                # try:
                #     angle = (x / y, node[1] > other[1])
                # except ZeroDivisionError:
                #     angle = inf if node[0] - other[0] > 0 else -inf

                print(node, other, angle, atan2(x, y))
                angles[node].add(angle)
        print(len(angles[node]))

    best = max(angles.values(), key=len)
    # for b in sorted(best):
    #     print(b)
    print(len(best), best)
    return len(best)


assert asteroids(""".#..#
.....
#####
....#
...##""") == 8

assert asteroids("""......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####""") == 33

assert asteroids("""#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.""") == 35

assert asteroids(""".#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..""") == 41

assert asteroids(""".#..##.###...#######
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
###.##.####.##.#..##""") == 210

print(asteroids(input))
