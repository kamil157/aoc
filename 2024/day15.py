with open('2024/inputs/day15.txt', encoding="utf-8") as f:
    lines = f.read().split('\n\n')


def solve():
    grid, moves = lines
    grid = [list(line) for line in grid.split('\n')]
    moves = ''.join(moves.split('\n'))

    robot = next((y, x) for y, line in enumerate(grid)
                 for x, c in enumerate(line) if c == "@")

    for move in moves:
        dir = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}[move]

        target = (robot[0] + dir[0], robot[1] + dir[1])

        boxes = 0
        while grid[target[0]][target[1]] == "O":
            boxes += 1
            target = (target[0] + dir[0], target[1] + dir[1])

        if grid[target[0]][target[1]] == "#":
            continue

        robot = (robot[0] + dir[0], robot[1] + dir[1])
        grid[robot[0]][robot[1]] = "."
        robot = target
        grid[robot[0]][robot[1]] = "@"

        if boxes > 0:
            grid[target[0] + boxes * dir[0]][target[1] + boxes * dir[1]] = "O"

    return sum(y * 100 + x for y, line in enumerate(grid) for x, c in enumerate(line) if c == "O")


print(solve())
