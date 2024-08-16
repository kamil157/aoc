from intcode import Intcode


with open('2019/inputs/day19.txt', encoding="utf-8") as f:
    input = f.read()


def inside_beam(s, x, y):
    intcode = Intcode(s)
    intcode.input(x)
    intcode.input(y)
    return intcode.run()


def beam_size(s):
    return sum([inside_beam(s, x, y) for y in range(50) for x in range(50)])


print(beam_size(input))  # 231


def fit_square(s, size):
    x = y = 0
    while True:
        y_in_range = inside_beam(s, x + size - 1, y)
        x_in_range = inside_beam(s, x, y + size - 1)
        if x_in_range and y_in_range:
            return x * 10000 + y
        if not y_in_range:
            y += 1
        if not x_in_range:
            x += 1


print(fit_square(input, 100))  # 9210745
