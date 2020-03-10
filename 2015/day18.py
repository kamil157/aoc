from copy import deepcopy

input = open('2015/inputs/day18.txt').read()

def count_neighbors_on(grid, i, j):
    count = 0
    for di, dj in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        if 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[i]) and grid[i + di][j + dj] == '#':
            count += 1
    return count

def animate(grid, is_part2):
    new_grid = deepcopy(grid)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if is_part2 and (i, j) in {(0, 0), (0, len(grid[i]) - 1), (len(grid) - 1, 0), (len(grid) - 1, len(grid[i]) - 1)}:
                new_grid[i][j] = '#'
                continue
            neighbors_on = count_neighbors_on(grid, i, j)
            if grid[i][j] == '#' and neighbors_on not in { 2, 3 }:
                new_grid[i][j] = '.'
            elif grid[i][j] == '.' and neighbors_on == 3:
                new_grid[i][j] = '#'

    return new_grid

def part1(s, is_part2):
    grid = [list(s) for s in input.split()]

    if is_part2:
        grid[0][0] = '#'
        grid[-1][0] = '#'
        grid[0][-1] = '#'
        grid[-1][-1] = '#'

    for _ in range(100):
        grid = animate(grid, is_part2)
    
    return sum(line.count('#') for line in grid)

print(part1(input, False))
print(part1(input, True))