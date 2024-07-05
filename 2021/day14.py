from itertools import pairwise
from typing import Counter


with open('2021/inputs/day14.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def part1(steps):
    polymer = lines[0]
    rules = {line[:2]: line[6] for line in lines[2:]}

    chars = Counter(polymer)
    pairs = Counter(["".join(p) for p in pairwise(polymer)])

    for _ in range(steps):
        new_pairs = Counter()
        for p, count in pairs.items():
            c = rules[p]
            chars[c] += count
            new_pairs[p[0] + c] += count
            new_pairs[c + p[1]] += count
        pairs = new_pairs
    return max(chars.values()) - min(chars.values())


print(part1(10))
print(part1(40))
