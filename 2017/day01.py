from itertools import pairwise


with open('2017/inputs/day01.txt', encoding="utf-8") as f:
    lines = f.read()


def part1():
    return sum((int(d[0]) for d in pairwise(lines + lines[0]) if d[0] == d[1]))


print(part1())


def part2():
    return sum(int(d[0]) for i, d in enumerate(lines) if d[0] == lines[(i + len(lines) // 2) % len(lines)])


print(part2())
