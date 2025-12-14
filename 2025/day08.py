from itertools import combinations
from math import prod

with open('2025/inputs/day08.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def part1():
    circuits = {}
    points = []
    for line in lines:
        p = tuple(int(n) for n in line.split(","))
        circuits[p] = {p}
        points.append(p)
    
    order = []
    for p1, p2 in combinations(points, 2):
        d = sum((p1[i] - p2[i]) ** 2 for i in range(3))
        order.append((d, (p1, p2)))
    order.sort()

    for i in range(1000):
        d, (p1, p2) = order[i]
        merged = circuits[p1] | circuits[p2]
        for p in merged:
            circuits[p] = merged

    unique = set(frozenset(circuit) for circuit in circuits.values())
    return prod(sorted((len(c) for c in unique), reverse=True)[:3])


def part2():
    circuits = {}
    points = []
    for line in lines:
        p = tuple(int(n) for n in line.split(","))
        circuits[p] = {p}
        points.append(p)
    
    order = []
    for p1, p2 in combinations(points, 2):
        d = sum((p1[i] - p2[i]) ** 2 for i in range(3))
        order.append((d, (p1, p2)))
    order.sort()

    for d, (p1, p2) in order:
        merged = circuits[p1] | circuits[p2]
        for p in merged:
            circuits[p] = merged
            if len(merged) == len(lines):
                return p1[0] * p2[0]


print(part1())
print(part2())
