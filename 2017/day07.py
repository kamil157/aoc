from collections import deque
from typing import Counter


with open('2017/inputs/day07.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def part1():
    names = set()
    for line in lines:
        if "->" in line:
            left, right = line.split(' -> ')
            names |= set(right.split(', '))

    for line in lines:
        if "->" in line:
            left, right = line.split(' -> ')
        else:
            left = line
        name = left.split()[0]
        if name not in names:
            return name


print(part1())


def part2():
    weights = {}
    initial = {}
    queue = deque()
    for line in lines:
        if "->" in line:
            left, right = line.split(' -> ')
            name, weight = left.split()
            queue.append((name, int(weight[1:-1]), right.split(', ')))
        else:
            name, weight = line.split()
            weights[name] = int(weight[1:-1])
        initial[name] = int(weight[1:-1])

    while queue:
        name, weight, programs = queue.popleft()

        if all(p in weights for p in programs):
            c = Counter(weights[p] for p in programs)
            if len(c) == 1:
                weights[name] = weight + sum(weights[p] for p in programs)
            else:
                m = c.most_common()
                for p in programs:
                    if weights[p] == m[-1][0]:
                        return initial[p] + m[0][0] - m[1][0]
        else:
            queue.append((name, weight, programs))
    return


print(part2())
