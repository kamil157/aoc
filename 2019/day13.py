from intcode import Intcode

with open('2019/inputs/day13.txt') as f:
    input = f.read()


def part1(s):
    intcode = Intcode(s)
    blocks = 0

    while True:
        try:
            x = intcode.run()
            y = intcode.run()
            id = intcode.run()
            if id == 2:
                blocks += 1
        except StopIteration:
            return blocks


print(part1(input))


def part2(s):
    intcode = Intcode(s)
    intcode.memory[0] = 2

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

            if id == 3:
                paddle = x
            if id == 4:
                ball = x

            def sign(ball, paddle):
                return (ball > paddle) - (ball < paddle)

            intcode.replace_input(sign(ball, paddle))

        except StopIteration:
            return score


print(part2(input))
