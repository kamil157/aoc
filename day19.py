from intcode import Intcode

input = "109,424,203,1,21101,11,0,0,1106,0,282,21102,18,1,0,1106,0,259,2101,0,1,221,203,1,21101,31,0,0,1106,0,282,21102,1,38,0,1106,0,259,21002,23,1,2,22102,1,1,3,21102,1,1,1,21101,57,0,0,1106,0,303,2101,0,1,222,21002,221,1,3,21001,221,0,2,21102,259,1,1,21102,80,1,0,1106,0,225,21102,1,79,2,21101,0,91,0,1106,0,303,2102,1,1,223,21001,222,0,4,21102,259,1,3,21101,225,0,2,21102,1,225,1,21101,0,118,0,1105,1,225,21002,222,1,3,21101,118,0,2,21101,0,133,0,1106,0,303,21202,1,-1,1,22001,223,1,1,21102,1,148,0,1105,1,259,1202,1,1,223,20102,1,221,4,20101,0,222,3,21102,1,22,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21102,1,195,0,105,1,109,20207,1,223,2,21002,23,1,1,21101,-1,0,3,21102,214,1,0,1106,0,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,2101,0,-4,249,22101,0,-3,1,22102,1,-2,2,21201,-1,0,3,21101,0,250,0,1105,1,225,22101,0,1,-4,109,-5,2105,1,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2106,0,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,22102,1,-2,-2,109,-3,2106,0,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,22102,1,-2,3,21102,343,1,0,1106,0,303,1105,1,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,21201,-4,0,1,21102,384,1,0,1105,1,303,1106,0,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,22101,0,1,-4,109,-5,2106,0,0"


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
