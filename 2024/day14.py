from functools import reduce
from operator import mul
from parse import parse

with open('2024/inputs/day14.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def solve():
    part1 = 0
    w = 101
    h = 103

    robots = [parse("p={:d},{:d} v={:d},{:d}", line) for line in lines]

    for i in range(1, 1000000):
        robots = [((px + vx) % w, (py + vy) % h, vx, vy)
                  for px, py, vx, vy in robots]

        quadrants = [[] for _ in range(4)]
        mirrored = [set() for _ in range(4)]
        for px, py, _, _ in robots:
            if px < w // 2:
                if py < h // 2:
                    quadrants[0].append((px, py))
                    mirrored[0].add((px, py))
                if py > h // 2:
                    quadrants[1].append((px, py))
                    mirrored[1].add((px, py))
            if px > w // 2:
                if py < h // 2:
                    quadrants[2].append((px, py))
                    mirrored[2].add((w - 1 - px, py))
                if py > h // 2:
                    quadrants[3].append((px, py))
                    mirrored[3].add((w - 1 - px, py))

        if i == 100:
            part1 = reduce(mul, (len(q) for q in quadrants))

        if len(mirrored[0].intersection(mirrored[2])) > 20 and len(mirrored[1].intersection(mirrored[3])) > 20:
            for py in range(h):
                for px in range(w):
                    if any(r[0] == px and r[1] == py for r in robots):
                        print('#', end='')
                    else:
                        print('.', end='')
                print()

            return part1, i

    return reduce(mul, (len(q) for q in quadrants))


print(solve())
