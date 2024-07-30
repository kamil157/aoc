from parse import parse

with open('2023/inputs/day24.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def part1():
    equations = []
    for line in lines:
        x1, y1, _, vx, vy, _ = parse(
            "{:d}, {:d}, {:d} @ {:d}, {:d}, {:d}", line)

        x2 = x1 + vx
        y2 = y1 + vy

        a = (y2 - y1) / (x2 - x1)
        b = y1 - a * x1
        direction = vx > 0
        equations.append((a, b, direction, x1))

    intersections = 0
    for i, line1 in enumerate(equations):
        for line2 in equations[i+1:]:
            a, c, dir1, x1 = line1
            b, d, dir2, x2 = line2
            if a != b:
                x = (d - c) / (a - b)
                y = a * x + c

                low = 200000000000000
                high = 400000000000000
                if low <= x <= high and low <= y <= high:
                    if (dir1 and x < x1) or (not dir1 and x > x1) or (dir2 and x < x2) or (not dir2 and x > x2):
                        continue

                    intersections += 1

    return intersections


print(part1())
