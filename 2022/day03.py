import string

with open('2022/inputs/day03.txt') as f:
    lines = f.read().strip().split('\n')


def part1(s):
    total = 0
    for line in s:
        left, right = line[:len(line) // 2], line[len(line) // 2:]
        common = set(left).intersection(set(right))

        letter = list(common)[0]
        priority = string.ascii_letters.find(letter)
        total += priority + 1
    return total


def part2(s):
    total = 0
    for i in range(0, len(s), 3):
        common = set(s[i]).intersection(set(s[i + 1])).intersection(set(s[i + 2]))

        letter = list(common)[0]
        priority = string.ascii_letters.find(letter)
        total += priority + 1
    return total


print(part1(lines))
print(part2(lines))
