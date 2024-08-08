from collections import deque
from functools import cache
from itertools import combinations, permutations, product


with open('2021/inputs/day19.txt', encoding="utf-8") as f:
    lines = f.read().split('\n\n')


def parse():
    scanners = []
    for scanner in lines:
        coords = scanner.splitlines()[1:]
        beacons = {tuple(int(n) for n in line.split(",")) for line in coords}
        scanners.append(frozenset(beacons))
    return scanners


@cache
def variants(scanner):
    result = []
    for d in product([-1, 1], repeat=3):
        for perm in permutations([0, 1, 2]):
            result.append({tuple(p[perm[i]] * d[perm[i]]
                          for i in range(3)) for p in scanner})
    return result


def match(scanner, beacons):
    for scanner_variant in variants(scanner):
        for b in beacons:
            for c in scanner_variant:
                offset = [(c[i] - b[i]) for i in range(3)]
                candidates = {tuple(p[i] + offset[i]
                                    for i in range(3)) for p in beacons}
                if len(candidates & scanner_variant) >= 12:
                    return scanner_variant, offset
    return False


def manhattan(p1, p2):
    return sum(abs(p1[i] - p2[i]) for i in range(3))


def part1():
    scanners = parse()
    q = deque(scanners[1:])
    beacons = set(scanners[0])
    offsets = [(0, 0, 0)]
    while q:
        scanner = q.popleft()
        m = match(scanner, beacons)
        if m:
            variant, offset = m
            print(len(q), len(beacons), offset)
            new_beacons = {tuple(p[i] - offset[i]
                                 for i in range(3)) for p in variant}
            beacons.update(new_beacons)
            offsets.append(offset)
        else:
            q.append(scanner)

    distances = [manhattan(s1, s2) for s1, s2 in combinations(offsets, 2)]
    return len(beacons), max(distances)


print(part1())
