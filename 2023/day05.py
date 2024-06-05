

import re


with open('2023/inputs/day05.txt') as f:
    lines = f.read().strip()


def seed_to_location(maps, value):
    for m in maps[1:]:
        for range in m.split('\n')[1:]:
            dst, src, len = map(int, range.split())
            if src <= value < src + len:
                value = value + dst - src
                break
    return value


def part1(s):
    maps = lines.split('\n\n')
    seeds = re.findall("\d+", maps[0])
    return min(seed_to_location(maps, int(seed)) for seed in seeds)


print(part1(lines))
