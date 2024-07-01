from collections import defaultdict
import copy

with open('2022/inputs/day17.txt', encoding="utf-8") as f:
    lines = f.read().strip()

rocks = """####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##""".split("\n\n")


def rock_shape(rock):
    shape = []
    for y, row in enumerate(rock):
        for x, tile in enumerate(row):
            if tile == "#":
                shape.append(x + (-len(rock) + 1 + y) * 1j)
    return shape


def has_collision(grid, shape):
    if any(int(tile.real) < 0 for tile in shape):
        return True
    if any(int(tile.real) >= len(grid[0]) for tile in shape):
        return True
    if any(int(tile.imag) > 0 for tile in shape):
        return True
    if any(grid[len(grid) - 1 + int(tile.imag)][int(tile.real)] == "#" for tile in shape):
        return True
    return False


def move(shape, diff):
    return [tile + diff for tile in shape]


def height(grid):
    for y, row in enumerate(grid):
        if "#" in row:
            return len(grid) - y
    return 0


def print_grid(grid, shape):
    grid2 = copy.deepcopy(grid)
    for tile in shape:
        grid2[len(grid) - 1 + int(tile.imag)][int(tile.real)] = "@"
    for line in grid2:
        print(line)
    print()


def part1(limit):
    pattern = lines
    grid = []
    width = 7
    visited = defaultdict(list)
    in_cycle = False
    jet = 0

    for i in range(limit):
        grid.insert(0, ["."] * width)
        grid.insert(0, ["."] * width)
        grid.insert(0, ["."] * width)
        grid.insert(0, ["."] * width)
        rock = rocks[i % len(rocks)]
        shape = rock_shape(rock.split('\n'))
        spawn = 2 - (height(grid) + 3) * 1j
        shape = move(shape, spawn)

        while not has_collision(grid, shape):
            dir = -1 if pattern[jet % len(pattern)] == "<" else 1
            if not has_collision(grid, move(shape, dir)):
                shape = move(shape, dir)

            shape = move(shape, 1j)
            jet += 1
        shape = move(shape, -1j)

        if in_cycle and limit % cycle_len == i % cycle_len:
            steps = (limit - i) // cycle_len
            return height(grid) + steps * h_diff

        key = (jet % len(pattern), i % len(rocks))
        if key in visited and i % len(rocks) == 0:
            prev_i, prev_h = visited[key][0]
            cycle_len = i - prev_i
            h_diff = height(grid) - prev_h
            in_cycle = True

        visited[key].append((i, height(grid)))

        for tile in shape:
            grid[len(grid) - 1 + int(tile.imag)][int(tile.real)] = "#"

    return height(grid)


print(part1(2022))
print(part1(1000000000000))
