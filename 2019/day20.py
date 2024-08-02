from collections import defaultdict, deque
from string import ascii_uppercase


with open('2019/inputs/day20.txt', encoding="utf-8") as f:
    lines = f.read().split('\n')


def part2(level_diff):
    g = defaultdict(list)
    portals = defaultdict(list)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == ".":
                for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if lines[y + dy][x + dx] == ".":
                        g[(y, x)].append((y + dy, x + dx))
                    if lines[y + dy][x + dx] in ascii_uppercase:
                        name = "".join(sorted(lines[y + dy][x + dx] +
                                              lines[y + 2*dy][x + 2*dx]))
                        portals[name].append((y, x))
                        if name == "AA":
                            start = (y, x)
                        elif name == "ZZ":
                            end = (y, x)

    outside = {}
    inside = {}
    for name, portal in portals.items():
        if name not in ["AA", "ZZ"]:
            assert len(portal) == 2
            if portal[0][0] == 2 or portal[0][1] == 2 or portal[0][0] == len(lines) - 3 or portal[0][1] == len(lines[0]) - 3:
                outside[portal[0]] = portal[1]
                inside[portal[1]] = portal[0]
            else:
                inside[portal[0]] = portal[1]
                outside[portal[1]] = portal[0]

    q = deque([(start, 0, 0)])
    seen = set()
    while q:
        pos, steps, level = q.popleft()
        if (pos, level) in seen:
            continue
        seen.add((pos, level))

        if pos == end and level == 0:
            return steps

        for neighbor in g[pos]:
            q.append((neighbor, steps + 1, level))

        if pos in inside:
            q.append((inside[pos], steps + 1, level + level_diff))

        if level != 0:
            if pos in outside:
                q.append((outside[pos], steps + 1, level - level_diff))


print(part2(0))
print(part2(1))
