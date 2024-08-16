import itertools

from intcode import Intcode

with open('2019/inputs/day07.txt') as f:
    input = f.read()


def part1(s):
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

        best = max(best, inout)

    return best


def part2(s):
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


print(part1(input))
print(part2(input))
