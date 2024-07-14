from itertools import combinations
from math import prod


with open('2015/inputs/day24.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def v1(groups):
    packages = [int(n) for n in lines]
    target = sum(packages) // groups

    def pick(packages, target, current):
        result = []
        for i, n in enumerate(packages):
            if n == target:
                result.append(current + [n])
            if n < target:
                result.extend(
                    pick(packages[i + 1:], target - n, current + [n]))
        return result

    options = pick(packages, target, [])
    return min((len(l), prod(l)) for l in options)[1]


def part1(groups):
    packages = [int(n) for n in lines]
    target = sum(packages) // groups

    for i in range(len(packages)):
        for c in combinations(packages, i):
            if sum(c) == target:
                return prod(c)


print(part1(3))
print(part1(4))
