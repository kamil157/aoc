from collections import deque


with open('2023/inputs/day23.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def part1():
    dirs = {"<": -1, ">": 1, "^": -1j, "v": 1j}
    g = {}
    for y, line in enumerate(lines):
        for x, node in enumerate(line):
            g[x+y*1j] = node

    end = len(lines[0]) - 2 + (len(lines[0]) - 1) * 1j
    q = deque([(1, set())])
    results = []
    while q:
        pos, path = q.pop()
        if pos in path:
            continue

        if pos == end:
            results.append(len(path))

        tile = g.get(pos, "#")
        if tile == ".":
            for d in [-1, 1, -1j, 1j]:
                if g.get(pos+d, "#") != "#":
                    q.append((pos+d, path | {pos}))
        elif tile in dirs:
            q.append((pos+dirs[tile], path | {pos}))

    return max(results)


print(part1())


def part2():
    g = {}
    for y, line in enumerate(lines):
        for x, node in enumerate(line):
            g[x+y*1j] = node

    adj = {}
    for y, line in enumerate(lines):
        for x, tile in enumerate(line):
            pos = x+y*1j
            if tile != "#":
                neighbors = {}
                for d in [-1, 1, -1j, 1j]:
                    if g.get(pos+d, "#") != "#":
                        neighbors[pos + d] = 1
                adj[pos] = neighbors

    while any(len(neighbors) == 2 for neighbors in adj.values()):
        for node, neighbors in adj.items():
            if len(neighbors) == 2:
                a, b = neighbors.items()
                adj[a[0]][b[0]] = a[1] + b[1]
                del adj[a[0]][node]
                adj[b[0]][a[0]] = a[1] + b[1]
                del adj[b[0]][node]
                del adj[node]
                break

    best = 0
    end = len(lines[0]) - 2 + (len(lines[0]) - 1) * 1j
    q = deque([(1, set(), 0)])

    while q:
        pos, path, dist = q.pop()
        if pos in path:
            continue

        if pos == end:
            best = max(best, dist)

        for neighbor in adj[pos]:
            q.append((neighbor, path | {pos}, dist + adj[pos][neighbor]))

    return best


print(part2())
