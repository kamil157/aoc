from functools import reduce
from operator import xor


with open('2017/inputs/day10.txt', encoding="utf-8") as f:
    lines = f.read().strip()


def knot(l, skip, start, lengths):
    for length in lengths:
        l[:length] = l[:length][::-1]
        move = (length + skip) % len(l)
        start = (start - move) % len(l)
        l = l[move:] + l[:move]
        skip += 1
    return l, skip, start


def part1():
    lengths = [int(n) for n in lines.split(",")]
    l, _, start = knot(list(range(256)), 0, 0, lengths)
    l = l[start:] + l[:start]
    return l[0] * l[1]


print(part1())


def part2():
    lengths = [ord(n) for n in lines] + [17, 31, 73, 47, 23]
    l = list(range(256))
    start = 0
    skip = 0
    for _ in range(64):
        l, skip, start = knot(l, skip, start, lengths)

    sparse = l[start:] + l[:start]
    dense = [reduce(xor, sparse[16*i:16*(i+1)]) for i in range(16)]
    return "".join(f"{n:02x}" for n in dense)


print(part2())
