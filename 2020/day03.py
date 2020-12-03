import math

input = open('2020/inputs/day03.txt').readlines()

def part1(s, dx, dy):
    x, y = 0, 0
    trees = 0

    while y < len(s):
        if s[y][x] == '#':
            trees += 1

        x += dx
        x %= len(s[0].strip())
        y += dy

    return trees

def part2(s):
    results = [part1(input, dx, dy) for dx, dy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]
    return math.prod(results)

print(part1(input, 3, 1))
print(part2(input))