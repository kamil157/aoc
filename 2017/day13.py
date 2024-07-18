from itertools import count


with open('2017/inputs/day13.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def parse():
    ranges = {}
    for line in lines:
        depth, range_ = line.split(": ")
        ranges[int(depth)] = int(range_)
    return ranges


def scanner_hit(pos, height):
    return pos % (2 * (height - 1)) == 0


def part1():
    return sum(pos * height for pos, height in parse().items() if scanner_hit(pos, height))


print(part1())


def part2():
    ranges = parse()
    for delay in count():
        if not any(scanner_hit(pos + delay, height) for pos, height in ranges.items()):
            return delay


print(part2())
