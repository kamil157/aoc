from intcode import Intcode

with open('2019/inputs/day13.txt') as f:
    input = f.read()


def arcade(s):
    intcode = Intcode(s)
    blocks = 0

    while True:
        try:
            # intcode.input(1)
            x = intcode.run()
            y = intcode.run()
            id = intcode.run()
            # print(x, y, id)
            if id == 2:
                blocks += 1
        except StopIteration:
            return blocks


print(arcade(input))
