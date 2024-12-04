from itertools import pairwise

with open('2024/inputs/day02.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def safe(line):
    diffs = []
    for n, m in pairwise(line):
        diffs.append(m - n)

    return all(1 <= diff <= 3 for diff in diffs) or all(-3 <= diff <= -1 for diff in diffs)


def solve():
    part1 = part2 = 0
    for line in lines:
        line = list(map(int, line.split()))
        if safe(line):
            part1 += 1
            part2 += 1
        else:
            for i in range(len(line)):
                l = list(line)
                del l[i]
                if safe(l):
                    part2 += 1
                    break

    return part1, part2


print(solve())
