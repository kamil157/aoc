
from copy import deepcopy
from functools import cmp_to_key
with open('2022/inputs/day13.txt') as f:
    lines = f.read().strip().split('\n\n')


def cmp(left, right):
    left = deepcopy(left)
    right = deepcopy(right)
    match left, right:
        case int(), int():
            return left - right
        case list(), list():
            while left and right:
                if (c := cmp(left.pop(0), right.pop(0))) != 0:
                    return c
            return len(left) - len(right)
        case int(), list():
            return cmp([left], right)
        case list(), int():
            return cmp(left, [right])


def part1():
    result = 0
    for i, line in enumerate(lines, start=1):
        [a, b] = line.split()
        if cmp(eval(a),  eval(b)) <= 0:
            result += i

    return result


print(part1())


def part2():
    decoder1 = [[2]]
    decoder2 = [[6]]
    packets = [decoder1, decoder2]
    for line in lines:
        [a, b] = line.split()
        packets.append(eval(a))
        packets.append(eval(b))

    packets = sorted(packets, key=cmp_to_key(cmp))
    return (packets.index(decoder1) + 1) * (packets.index(decoder2) + 1)


print(part2())
