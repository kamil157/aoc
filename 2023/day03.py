from collections import defaultdict
import re

with open('2023/inputs/day03.txt') as f:
    lines = f.read().strip().split('\n')


def extend_map(s):
    dotline = "." * len(s[0])
    extended = []
    extended.append(dotline)
    extended.extend(s)
    extended.append(dotline)
    for n, line in enumerate(extended):
        extended[n] = "." + line + "."
    return extended


def get_symbols(m, n, extended):
    symbols = []
    for i in range(m.start(0) - 1, m.end(0) + 1):
        for j in range(n - 1, n + 2):
            if not extended[j][i].isdigit():
                symbols.append((i, j))

    return symbols


def part1(s):
    total = 0

    extended = extend_map(s)
    for n, line in enumerate(extended):
        for m in re.finditer("\d+", line):
            symbols = get_symbols(m, n, extended)
            symbols = [(x, y) for (x, y) in symbols if extended[y][x] != "."]

            if len(symbols) > 0:
                total += int(m.group(0))

    return total


print(part1(lines))


def part2(s):
    total = 0
    gears = []
    extended = extend_map(s)

    for n, line in enumerate(extended):
        for m in re.finditer("\d+", line):
            symbols = get_symbols(m, n, extended)
            symbols = [(x, y) for (x, y) in symbols if extended[y][x] == "*"]

            for pos in symbols:
                gears.append((pos, int(m.group(0))))

    gear_map = defaultdict(list)
    for pos, n in gears:
        gear_map[pos].append(n)

    for gear in gear_map.values():
        if len(gear) == 2:
            total += gear[0] * gear[1]

    return total


print(part2(lines))
