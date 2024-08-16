import itertools

from intcode import Intcode

with open('2019/inputs/day07.txt') as f:
    input = f.read()


def thrusters(s):
    perm = itertools.permutations(range(5, 10))
    best = 0

    for p in perm:
        intcodes = []
        for i in range(5):
            intcode = Intcode(s)
            intcodes.append(intcode)
            intcode.input(p[i])

        signal = 0
        i = 0
        while True:
            intcodes[i % 5].input(signal)
            try:
                signal = intcodes[i % 5].run()
            except StopIteration:
                best = max(best, signal)
                break
            i += 1

    return best


if __name__ == "__main__":
    assert thrusters(
        '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5') == 139629729
    assert thrusters(
        '3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10') == 18216

    print(thrusters(input))  # 8754464
