from itertools import permutations
from typing import Counter


with open('2018/inputs/day02.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def part1():
    twice = 0
    thrice = 0
    for line in lines:
        c = Counter(line)
        if 2 in c.values():
            twice += 1
        if 3 in c.values():
            thrice += 1

    return twice * thrice


print(part1())


def part2():
    for a, b in permutations(lines, 2):
        diff = 0
        result = ""
        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1
            else:
                result += a[i]
        if diff == 1:
            return result


print(part2())
