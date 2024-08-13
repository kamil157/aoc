import z3
from operator import itemgetter
from parse import findall

with open('2018/inputs/day23.txt', encoding="utf-8") as f:
    lines = f.read().strip()


def part1():
    nanobots = list(findall("pos=<{:d},{:d},{:d}>, r={:d}", lines))
    sx, sy, sz, sr = max(nanobots, key=itemgetter(3))
    return sum(abs(x - sx) + abs(y - sy) + abs(z - sz) <= sr for x, y, z, _ in nanobots)


print(part1())


def z3abs(x):
    return z3.If(x >= 0, x, -x)


def z3dist(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return z3abs(x1 - x2) + z3abs(y1 - y2) + z3abs(z1 - z2)


def part2():
    nanobots = list(findall("pos=<{:d},{:d},{:d}>, r={:d}", lines))

    solver = z3.Optimize()
    pos = z3.IntVector('pos', 3)
    in_range = z3.IntVector('in_range', len(nanobots))
    dist = z3.Int('dist')

    for i, bot in enumerate(nanobots):
        solver.add(in_range[i] == z3.If(z3dist(pos, bot[:3]) <= bot[3], 1, 0))

    solver.maximize(z3.Sum(*in_range))
    solver.add(dist == z3dist(pos, (0, 0, 0)))
    solver.minimize(dist)
    solver.check()
    return solver.model().evaluate(dist)


print(part2())
