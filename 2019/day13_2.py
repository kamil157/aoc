from intcode import Intcode
from math import copysign

with open('2019/inputs/day13.txt') as f:
    input = f.read()


def arcade(s):
    intcode = Intcode(s)
    intcode.memory[0] = 2
    # tiles = ['  ', 'X ', '# ', '__', 'o ']

    # map = [[''] * 44 for i in range(20)]
    ball = 0
    paddle = 0
    while True:
        try:
            x = intcode.run()
            y = intcode.run()
            id = intcode.run()

            if x == -1 and y == 0:
                score = id
                continue

            # map[y][x] = tiles[id]

            if id == 3:
                paddle = x
            if id == 4:
                ball = x

            def sign(ball, paddle):
                return (ball > paddle) - (ball < paddle)

            intcode.replace_input(sign(ball, paddle))

        except StopIteration:
            return score
            # for row in map:
            # print(''.join(row))


print(arcade(input))  # 10547
