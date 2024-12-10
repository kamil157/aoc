with open('2024/inputs/day10.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def dfs(lines, x, y, height, goals):
    if x < 0 or x >= len(lines[0]) or y < 0 or y >= len(lines) or int(lines[y][x]) != height:
        return 0
    if height == 9:
        goals.add((y, x))
        return 1
    count = 0
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        count += dfs(lines, x + dx, y + dy, height + 1, goals)
    return count


def solve():
    part1 = part2 = 0
    for y, line in enumerate(lines):
        for x, tile in enumerate(line):
            goals = set()
            part2 += dfs(lines, x, y, 0, goals)
            part1 += len(goals)

    return part1, part2


print(solve())
