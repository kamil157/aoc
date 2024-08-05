from collections import deque


with open('2019/inputs/day18.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def part2():
    target = 0
    start = []
    for y, line in enumerate(lines):
        for x, tile in enumerate(line):
            if tile == "@":
                start.append((y, x))
            if tile.islower():
                target += 1
    start = tuple(start)

    queue = deque()
    for i in range(4):
        queue.append((start, set(), 0, i))
    seen = set()
    while queue:
        pos, keys, steps, active = queue.popleft()
        if (pos, frozenset(keys), active) in seen:
            continue
        seen.add((pos, frozenset(keys), active))

        if len(keys) == target:
            return steps

        y, x = pos[active]
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            robots = list(pos)
            ny, nx = y + dy, x + dx
            robots[active] = (ny, nx)

            if lines[ny][nx].islower() and lines[ny][nx] not in keys:
                for i in range(4):
                    queue.append(
                        (tuple(robots), keys | {lines[ny][nx]}, steps + 1, i))
            elif not ((lines[ny][nx].isupper() and lines[ny][nx].lower() not in keys) or lines[ny][nx] == "#"):
                queue.append((tuple(robots), keys, steps + 1, active))


print(part2())
