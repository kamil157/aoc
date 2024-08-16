from collections import defaultdict
from intcode import Intcode

with open('2019/inputs/day11.txt') as f:
    input = f.read()


def run(color):
    x, y = 0, 0
    dir = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    panels = defaultdict(int)
    panels[x, y] = color
    intcode = Intcode(input)

    while True:
        inp = panels[x, y]
        intcode.input(inp)

        try:
            color = intcode.run()
        except StopIteration:
            break
        panels[x, y] = color

        turn = intcode.run()

        dir += -1 if turn == 0 else 1
        x += directions[dir % 4][0]
        y += directions[dir % 4][1]

    return panels


print(len(run(0)))


def print_panels(panels):
    min_x = min(p[0] for p in panels.keys())
    max_x = max(p[0] for p in panels.keys())
    min_y = min(p[1] for p in panels.keys())
    max_y = max(p[1] for p in panels.keys())

    adjusted = {}
    for (x, y), color in panels.items():
        adjusted[(x - min_x, y - min_y)] = color

    image = [[0] * (max_x - min_x + 1) for y in range(max_y - min_y + 1)]
    for (x, y), color in adjusted.items():
        image[y][x] = color

    for row in image[::-1]:
        row_s = ''
        for pixel in row:
            if pixel == 0:
                row_s += '  '
            else:
                row_s += '# '
        print(row_s)


print_panels(run(1))
