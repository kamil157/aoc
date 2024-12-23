from collections import defaultdict


with open('2024/inputs/day23.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def solve():
    g = defaultdict(list)
    for line in lines:
        c = line.split("-")
        g[c[0]].append(c[1])
        g[c[1]].append(c[0])

    part1 = set()
    for a, v in g.items():
        for b in v:
            for c in g[b]:
                if c in v and (a.startswith("t") or b.startswith("t") or c.startswith("t")):
                    part1.add(tuple(sorted((a, b, c))))

    return len(part1)


print(solve())
