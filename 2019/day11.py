from collections import defaultdict
from intcode import Intcode

with open('2019/inputs/day11.txt') as f:
    input_raw = f.read()


def run(s):
    black, white = 0, 1
    x, y = 0, 0
    dir = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    panels = defaultdict(int)
    panels[x, y] = black
    intcode = Intcode(s)

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

    return len(panels)


if __name__ == "__main__":
    print(run(input_raw))  # 2255
