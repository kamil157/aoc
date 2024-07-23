from operator import itemgetter
from parse import findall

with open('2018/inputs/day23.txt', encoding="utf-8") as f:
    lines = f.read().strip()


def part1():
    nanobots = list(findall("pos=<{:d},{:d},{:d}>, r={:d}", lines))
    sx, sy, sz, sr = max(nanobots, key=itemgetter(3))
    return sum(abs(x - sx) + abs(y - sy) + abs(z - sz) <= sr for x, y, z, _ in nanobots)


print(part1())
