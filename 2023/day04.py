
import re


with open('2023/inputs/day04.txt') as f:
    lines = f.read().strip().split('\n')


def part1(s):
    total = 0
    for line in s:
        group = line.split(":")[1].split("|")
        def nums(s): return [int(n) for n in s.split(" ") if n]
        if matches := set(nums(group[0])) & set(nums(group[1])):
            total += 2 ** (len(matches) - 1)
    return total


print(part1(lines))


def part2(s):
    copies = [1] * len(s)
    for line in s:
        m = re.match("Card +(\d+):((?:  ?\d+)+) \|((?:  ?\d+)+)", line)
        def nums(s): return [int(n) for n in s.split(" ") if n]
        if matches := set(nums(m.group(2))) & set(nums(m.group(3))):
            card = int(m.group(1))
            for i in range(len(matches)):
                copies[card + i] += copies[card - 1]
    return sum(copies)


print(part2(lines))
