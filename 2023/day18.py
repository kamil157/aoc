with open('2023/inputs/day18.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


dirs = {"R": (1, 0), "D": (0, 1), "L": (-1, 0), "U": (0, -1)}


def part1(line):
    [direction, dist, _] = line.split()
    return dirs[direction], int(dist)


def part2(line):
    [_, _, color] = line.split()
    direction = list(dirs.values())[int(color[7])]
    dist = int(color[2:7], 16)
    return direction, dist


def solve(parse):
    x = area = 0

    for line in lines:
        (dx, dy), dist = parse(line)
        x += dist * dx
        area += x * dist * dy + dist // 2 + 1

    return area


print(solve(part1))
print(solve(part2))
