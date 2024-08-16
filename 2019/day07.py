import itertools

from intcode import Intcode

with open('2019/inputs/day07.txt') as f:
    input = f.read()


def thrusters(s):
    perm = itertools.permutations(range(5))
    best = 0

    for p in perm:
        inout = 0

        for i in range(5):
            phase = p[i]
            intcode = Intcode(s)
            intcode.input(phase)
            intcode.input(inout)
            inout = intcode.run()
            # print(phase, inout)

        best = max(best, inout)
    # print(best)
    return best


if __name__ == "__main__":
    assert thrusters('3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0') == 43210
    assert thrusters(
        '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0') == 54321
    assert thrusters(
        '3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0') == 65210

    print(thrusters(input))  # 99376
