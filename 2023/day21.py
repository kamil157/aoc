from collections import deque


with open('2023/inputs/day21.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def part1():
    g = set()
    for y, line in enumerate(lines):
        for x, node in enumerate(line):
            if node == "S":
                start = x+y*1j
            if node in "S.":
                g.add(x+y*1j)

    q = deque([(start, 0)])
    seen = set()
    result = 0
    while q:
        node, dist = q.popleft()
        if node in seen:
            continue
        seen.add(node)

        if dist % 2 == 0 and dist <= 64:
            result += 1

        for d in [-1, 1, -1j, 1j]:
            if node + d in g:
                q.append((node + d, dist + 1))

    return result


print(part1())
