from parse import parse

with open('2018/inputs/day10.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def part1():
    points = []
    for line in lines:
        px, py, vx, vy = parse(
            "position=<{:d}, {:d}> velocity=<{:d}, {:d}>", line)
        points.append((px, py, vx, vy))

    t = 1
    while True:
        for p in range(len(points)):
            px, py, vx, vy = points[p]
            points[p] = px + vx, py + vy, vx, vy

        min_x = min(p[0] for p in points)
        min_y = min(p[1] for p in points)
        max_y = max(p[1] for p in points)

        if max_y - min_y < 10:
            grid = [[".."] * 62 for _ in range(10)]
            for px, py, _, _ in points:
                grid[py - min_y][px - min_x] = "##"

            for line in grid:
                print("".join(line))
            return t
        t += 1


print(part1())
