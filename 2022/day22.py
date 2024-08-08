import re


with open('2022/inputs/day22.txt', encoding="utf-8") as f:
    lines = f.read().split('\n\n')


def wrap1(pos, direction, maze):
    y = int(pos.imag) % len(maze)
    x = int(pos.real) % len(maze[0])
    pos = x+y*1j
    pos += direction
    return pos, direction


def wrap2(pos, direction):
    x, y = pos.real, pos.imag
    match direction, x // 50, y // 50:
        case 1j, 0, 3: return complex(x + 100, 0), 1j  # down 6 -> down 2
        case 1j, 1, 2: return complex(49, x + 100), -1  # down 5 -> left 6
        case 1j, 2, 0: return complex(99, x - 50), -1  # down 2 -> left 3

        case -1j, 0, 2: return complex(50, x + 50), 1  # up 4 -> right 3
        case -1j, 1, 0: return complex(0, x + 100), 1  # up 1 -> right 6
        case -1j, 2, 0: return complex(x - 100, 199), -1j  # up 2 -> up 6

        case -1, 1, 0: return complex(0, 149 - y), 1  # left 1 -> right 4
        case -1, 1, 1: return complex(y - 50, 100), 1j  # left 3 -> down 4
        case -1, 0, 2: return complex(50, 149 - y), 1  # left 4 -> right 1
        case -1, 0, 3: return complex(y - 100, 0), 1j  # left 6 -> down 1

        case 1, 2, 0: return complex(99, 149 - y), -1  # right 2 -> left 5
        case 1, 1, 1: return complex(y + 50, 49), -1j  # right 3 -> up 2
        case 1, 1, 2: return complex(149, 149 - y), -1  # right 5 -> left 2
        case 1, 0, 3: return complex(y - 100, 149), -1j  # right 6 -> up 5


def solve(part1):
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

    steps = re.findall(r"(L|R|\d+)", steps)

    for step in steps:
        if step == "L":
            direction *= -1j
        elif step == "R":
            direction *= 1j
        else:
            for _ in range(int(step)):
                next_pos = pos + direction
                next_dir = direction

                while next_pos not in grid:
                    if part1:
                        next_pos, next_dir = wrap1(next_pos, direction, maze)
                    else:
                        next_pos, next_dir = wrap2(pos, direction)

                if grid[next_pos] == ".":
                    pos = next_pos
                    direction = next_dir

    return (int(pos.imag) + 1) * 1000 + (int(pos.real) + 1) * 4 + [1, 1j, -1, -1j].index(direction)


print(solve(True))
print(solve(False))
