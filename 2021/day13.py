with open('2021/inputs/day13.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def parse():
    grid = set()
    folds = []
    for line in lines:
        if "," in line:
            x, y = line.split(",")
            grid.add((int(x), int(y)))
        elif "fold" in line:
            fold = line.split()[2]
            folds.append((fold[0], int(fold[2:])))
    return grid, folds


def do_fold(grid, fold):
    new_grid = set()
    for x, y in grid:
        if fold[0] == "y" and y > fold[1]:
            y = 2 * fold[1] - y
        if fold[0] == "x" and x > fold[1]:
            x = 2 * fold[1] - x
        new_grid.add((x, y))
    return new_grid


def part1():
    grid, folds = parse()
    return len(do_fold(grid, folds[0]))


print(part1())


def part2():
    grid, folds = parse()

    for fold in folds:
        grid = do_fold(grid, fold)

    for y in range(max(pos[1] for pos in grid) + 1):
        line = ""
        for x in range(max(pos[0] for pos in grid) + 1):
            line += "##" if (x, y) in grid else ".."
        print(line)


part2()
