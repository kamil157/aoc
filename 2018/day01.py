with open('2018/inputs/day01.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def part1():
    return sum([int(line) for line in lines])


print(part1())


def part2():
    freq = 0
    seen = set()
    while True:
        for line in lines:
            if freq in seen:
                return freq
            seen.add(freq)
            freq += int(line)


print(part2())
