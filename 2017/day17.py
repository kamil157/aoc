from collections import deque


def part1():
    l = deque([0])
    for i in range(2017):
        offset = 329
        l.rotate(-offset)
        l.append(i + 1)
    return l[0]


print(part1())


def part2():
    pos = 0
    for i in range(1, 50000000 + 1):
        pos = (pos + 329) % i + 1
        if pos == 1:
            result = i
    return result


print(part2())
