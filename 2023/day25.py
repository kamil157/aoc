from collections import Counter, defaultdict, deque


with open('2023/inputs/day25.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def hottest(g):
    counter = Counter()
    for start in g:
        seen = set()
        q = deque()
        for edge in g[start]:
            q.append((start, edge))
        while q:
            edge, node = q.popleft()
            if node in seen:
                continue
            seen.add(node)
            e = "/".join(sorted([node, edge]))
            counter[e] += 1

            for edge in g[node]:
                q.append((node, edge))

    return [h[0] for h in counter.most_common(3)]


def part1():
    g = defaultdict(list)
    for line in lines:
        left, right = line.split(": ")
        for node in right.split():
            g[left].append(node)
            g[node].append(left)

    cut = hottest(g)
    groups = []
    seen = set()
    for start in g:
        size = 0
        q = deque()
        if start in seen:
            continue
        for edge in g[start]:
            q.append((start, edge))
        while q:
            edge, node = q.popleft()
            if node in seen:
                continue
            size += 1
            seen.add(node)

            for edge in g[node]:
                e = "/".join(sorted([node, edge]))
                if e in cut:
                    continue
                q.append((node, edge))
        groups.append(size)
    return groups[0] * groups[1]


print(part1())
