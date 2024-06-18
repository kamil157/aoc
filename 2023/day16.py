
with open('2023/inputs/day16.txt') as f:
    lines = f.read().strip().split('\n')


def part1(start):
    energized = [["."] * len(lines[0]) for _ in lines]
    visited = set()

    beams = [start]
    while beams:
        y, x, dy, dx = beams.pop(0)

        if (y, x, dy, dx) in visited:
            continue
        visited.add((y, x, dy, dx))

        if y < 0 or x < 0 or y >= len(lines) or x >= len(lines[0]):
            continue

        energized[y][x] = "#"

        forward = (y + dy, x + dx, dy, dx)
        mirror1 = (y - dx, x - dy, -dx, -dy)
        mirror2 = (y + dx, x + dy, dx, dy)

        match lines[y][x]:
            case ".":
                beams.append(forward)
            case "/":
                beams.append(mirror1)
            case "\\":
                beams.append(mirror2)
            case "|":
                if dy != 0:
                    beams.append(forward)
                else:
                    beams.append(mirror1)
                    beams.append(mirror2)
            case "-":
                if dy == 0:
                    beams.append(forward)
                else:
                    beams.append(mirror1)
                    beams.append(mirror2)

    return sum(line.count("#") for line in energized)


print(part1(((0, 0, 0, 1))))


def part2():
    best = 0
    for y in range(len(lines)):
        best = max(best, part1((y, 0, 0, 1)))  # left
        best = max(best, part1((y, len(lines[0]) - 1, 0, -1)))  # right
    for x in range(len(lines[0])):
        best = max(best, part1((0, x, 1, 0)))  # top
        best = max(best, part1((len(lines) - 1, x, -1, 0)))  # bot
    return best


print(part2())
