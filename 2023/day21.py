from collections import deque


with open('2023/inputs/day21.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


l = len(lines)
mid = l // 2


def part1(steps):
    g = set()
    for y, line in enumerate(lines):
        for x, node in enumerate(line):
            if node == "S":
                start = x+y*1j
            if node in "S.":
                g.add((x+y*1j))

    q = deque([(start, 0)])
    seen = set()
    result = 0
    while q:
        node, dist = q.popleft()
        if node in seen:
            continue
        seen.add(node)

        if dist % 2 == steps % 2:
            result += 1

        for d in [-1, 1, -1j, 1j]:
            u = int((node + d).real % l) + int((node + d).imag % l) * 1j
            if u in g and dist < steps:
                q.append((node + d, dist + 1))

    return result


print(part1(64))


def part2():
    results = [part1(i * l + 65) for i in range(3)]
    n = (26501365 - mid) // l
    a, b, c = results
    d1, d2 = b - a, c - b
    return a + n * (d1 + (n - 1) * (d2 - d1) // 2)


print(part2())
