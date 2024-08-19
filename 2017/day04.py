with open('2017/inputs/day04.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def part1():
    result = 0
    for line in lines:
        words = line.split()
        if len(words) == len(set(words)):
            result += 1
    return result


print(part1())


def part2():
    result = 0
    for line in lines:
        words = ["".join(sorted(word)) for word in line.split()]
        if len(words) == len(set(words)):
            result += 1
    return result


print(part2())
