from collections import Counter

with open('2024/inputs/day04.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def find(target, lines, word, y, x, dy, dx, visited):
    if word == target:
        return visited[1]
    if y < 0 or x < 0 or y >= len(lines) or x >= len(lines[0]) or not target.startswith(word):
        return None
    return find(target, lines, word + lines[y][x], y + dy, x + dx, dy, dx, visited + [(y, x)])


def part1():
    count = 0
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if find("XMAS", lines, "", y, x, dy, dx, []):
                        count += 1
    return count


print(part1())


def part2():
    midpoints = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            for dy, dx in [(-1, -1), (1, 1), (-1, 1), (1, -1)]:
                if res := find("MAS", lines, "", y, x, dy, dx, []):
                    midpoints.append(res)

    return sum(v > 1 for v in Counter(midpoints).values())


print(part2())
