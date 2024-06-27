with open('2022/inputs/day14.txt') as f:
    lines = f.read().strip().split('\n')


def init_grid():
    grid = {}
    for line in lines:
        coords = []
        for pos in line.split(" -> "):
            [x, y] = map(int, pos.split(","))
            coords.append((x, y))

        for (x1, y1), (x2, y2) in zip(coords, coords[1:]):
            x1, x2 = sorted([x1, x2])
            y1, y2 = sorted([y1, y2])
            for y in range(y1, y2 + 1):
                grid[(x1, y)] = "#"
            for x in range(x1, x2 + 1):
                grid[(x, y1)] = "#"
    return grid


def draw_grid(grid, height):
    x_max = max(x for x, y in grid.keys())
    x_min = min(x for x, y in grid.keys())
    for y in range(height + 1):
        line = ""
        for x in range(x_min, x_max + 1):
            line += grid.get((x, y), ".")
        print(line)


def part1():
    grid = init_grid()
    height = max(y for x, y in grid.keys())

    source = (500, 0)
    grid[source] = "+"

    total = 0
    while True:
        x, y = source
        for _ in range(height):
            if (x, y + 1) not in grid:
                y += 1
            elif (x - 1, y + 1) not in grid:
                x -= 1
                y += 1
            elif (x + 1, y + 1) not in grid:
                x += 1
                y += 1
            else:
                grid[(x, y)] = "o"
                total += 1
                break
        else:
            break

    return total


print(part1())


def part2():
    grid = init_grid()
    height = max(y for x, y in grid.keys())
    floor = height + 2
    source = (500, 0)
    grid[source] = "+"

    for x in range(0, 1000):
        grid[(x, floor)] = "#"

    total = 0
    while grid[source] == "+":
        x, y = source
        for _ in range(floor):
            if (x, y + 1) not in grid:
                y += 1
            elif (x - 1, y + 1) not in grid:
                x -= 1
                y += 1
            elif (x + 1, y + 1) not in grid:
                x += 1
                y += 1
            else:
                grid[(x, y)] = "o"
                total += 1
                break

    return total


print(part2())
