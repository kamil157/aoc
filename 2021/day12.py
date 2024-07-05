from collections import Counter, defaultdict


with open('2021/inputs/day12.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def small(node):
    return node.islower() and node not in ["start", "end"]


def part1(limit):
    graph = defaultdict(list)
    for line in lines:
        a, b = line.split("-")
        graph[a].append(b)
        graph[b].append(a)

    paths = 0
    s = [("start", ["start"])]
    while s:
        node, path = s.pop()
        if node == "end":
            paths += 1
            continue

        count = Counter((n for n in path if small(n) and node != n))
        count_ok = count.most_common(1)[0][1] <= 1 if count else True

        if node not in path[:-1] or node.isupper() or (small(node) and path.count(node) <= limit and count_ok):
            for neighbor in graph[node]:
                s.append((neighbor, path + [neighbor]))
    return paths


print(part1(1))
print(part1(2))
