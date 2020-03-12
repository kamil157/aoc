from copy import deepcopy

input = open('2015/inputs/day18.txt').read()

ON = '#'
OFF = '.'


def get_corners(grid):
    return {(0, 0), (0, len(grid[0]) - 1), (len(grid) - 1, 0), (len(grid) - 1, len(grid[0]) - 1)}


def count_neighbors_on(grid, i, j):
    count = 0
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if (di, dj) != (0, 0) \
                    and 0 <= i + di < len(grid) \
                    and 0 <= j + dj < len(grid[i]) \
                    and grid[i + di][j + dj] == ON:
                count += 1
    return count


def animate(grid, is_part2):
    new_grid = deepcopy(grid)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if is_part2 and (i, j) in get_corners(grid):
                continue
            neighbors_on = count_neighbors_on(grid, i, j)
            if grid[i][j] == ON and neighbors_on not in {2, 3}:
                new_grid[i][j] = OFF
            elif grid[i][j] == OFF and neighbors_on == 3:
                new_grid[i][j] = ON

    return new_grid


def part1(s, is_part2):
    grid = [list(line) for line in s.split()]

    if is_part2:
        for i, j in get_corners(grid):
            grid[i][j] = ON

    for _ in range(100):
        grid = animate(grid, is_part2)

    return sum(line.count(ON) for line in grid)


print(part1(input, False))
print(part1(input, True))
