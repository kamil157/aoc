from collections import defaultdict
from itertools import combinations

with open('2024/inputs/day08.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def solve():
    antennas = defaultdict(list)
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != '.':
                antennas[char].append(x + y*1j)

    antinodes1 = set()
    antinodes2 = set()
    for char, positions in antennas.items():
        for a, b in combinations(positions, 2):
            d = a - b
            for p in [a-d, a+d, b-d, b+d]:
                if 0 <= p.real < len(lines[0]) and 0 <= p.imag < len(lines) and p != a and p != b:
                    antinodes1.add(p)

            for direction in [-d, +d]:
                p = a
                while 0 <= p.real < len(lines[0]) and 0 <= p.imag < len(lines):
                    antinodes2.add(p)
                    p += direction

    return len(antinodes1), len(antinodes2)


print(solve())
