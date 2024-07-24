from collections import deque


with open('2018/inputs/day25.txt', encoding="utf-8") as f:
    lines = f.read().strip().splitlines()


def dist(p1, p2):
    return sum(abs(p1[i] - p2[i]) for i in range(len(p1)))


def part1():
    g = {}
    points = [tuple(int(n) for n in line.split(",")) for line in lines]
    for p1 in points:
        g[p1] = []
        for p2 in points:
            if p1 != p2 and dist(p1, p2) <= 3:
                g[p1].append(p2)

    seen = set()
    count = 0
    for start in g:
        if start in seen:
            continue

        count += 1
        q = deque([start])
        while q:
            node = q.popleft()
            if node in seen:
                continue

            seen.add(node)
            for neighbor in g[node]:
                q.append(neighbor)

    return count


print(part1())
