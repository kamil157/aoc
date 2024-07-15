
with open('2016/inputs/day20.txt', encoding="utf-8") as f:
    lines = f.read().strip().split("\n")


def parse():
    blocked = []
    for line in lines:
        start, end = line.split("-")
        blocked.append((int(start), int(end)))
    return sorted(blocked)


def part1():
    lowest = 0
    for start, end in parse():
        if start > lowest:
            return lowest
        lowest = max(end + 1, lowest)


print(part1())


def part2():
    allowed = 0
    lowest = 0
    for start, end in parse():
        if start > lowest:
            allowed += start - lowest
        lowest = max(end + 1, lowest)

    return allowed


print(part2())
