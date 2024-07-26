import re


with open('2022/inputs/day22.txt', encoding="utf-8") as f:
    lines = f.read().split('\n\n')


def print_grid(grid, maze, pos, direction):
    facing = {1: ">", 1j: "v", -1: "<", -1j: "^"}
    for y in range(len(maze)):
        line = ""
        for x in range(len(maze[0])):
            if x+y*1j == pos:
                line += facing[direction]
            else:
                line += grid.get(x+y*1j, " ")
        print(line)
    print()


def part1():
    maze, steps = lines
    maze = maze.splitlines()

    pos = None
    direction = 1
    grid = {}
    for y, line in enumerate(maze):
        for x, tile in enumerate(line):
            if tile != " ":
                grid[x+y*1j] = tile
                if not pos:
                    pos = x+y*1j

    turns = re.findall(r"(L|R)", steps)
    steps = re.findall(r"\d+", steps)

    def do_step(step, pos):
        for _ in range(step):
            next_pos = pos + direction
            while next_pos not in grid:
                y = int(next_pos.imag) % len(maze)
                x = int(next_pos.real) % len(maze[0])
                next_pos = x+y*1j
                next_pos += direction
            if grid[next_pos] == ".":
                pos = next_pos
        return pos

    for i, turn in enumerate(turns):
        pos = do_step(int(steps[i]), pos)
        direction *= -1j if turn == "L" else 1j
    pos = do_step(int(steps[-1]), pos)

    return (int(pos.imag) + 1) * 1000 + (int(pos.real) + 1) * 4 + [1, 1j, -1, -1j].index(direction)


print(part1())
