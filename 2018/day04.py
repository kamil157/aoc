from collections import defaultdict
from typing import Counter

with open('2018/inputs/day04.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def solve():
    guards = defaultdict(Counter)
    for line in sorted(lines):
        time, action = line.split('] ')

        if "Guard" in action:
            guard = int(action.split()[1][1:])
        elif action == "falls asleep":
            asleep = int(time[-2:])
        elif action == 'wakes up':
            for t in range(asleep, int(time[-2:])):
                guards[guard][t] += 1

    guard = max(guards, key=lambda x: sum(guards[x].values()))
    part1 = guard * guards[guard].most_common(1)[0][0]

    guard = max(guards, key=lambda x: guards[x].most_common(1)[0][1])
    part2 = guard * guards[guard].most_common(1)[0][0]
    return part1, part2


print(solve())
