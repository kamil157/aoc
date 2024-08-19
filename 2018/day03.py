from parse import findall

with open('2018/inputs/day03.txt', encoding="utf-8") as f:
    lines = f.read()


def mark_claims():
    grid = [[0] * 1000 for _ in range(1000)]
    claims = list(findall("#{:d} @ {:d},{:d}: {:d}x{:d}", lines))

    for id, x, y, w, h in claims:
        for i in range(x, x + w):
            for j in range(y, y + h):
                grid[i][j] += 1
    return grid, claims


def part1():
    grid, _ = mark_claims()
    return sum(cell > 1 for row in grid for cell in row)


print(part1())


def part2():
    grid, claims = mark_claims()
    for id, x, y, w, h in claims:
        if all(grid[i][j] == 1 for i in range(x, x + w) for j in range(y, y + h)):
            return id


print(part2())
