import re

input = open('2015/inputs/day05.txt').readlines()

def part1(s):
    count = 0
    for string in s:
        vowels = re.search(r'([aeiou].*){3}', string)
        twice = re.search(r'([a-z])\1', string)
        contains = re.search(r'(ab|cd|pq|xy)', string)

        if vowels and twice and not contains:
            count += 1
    return count


def part2(s):
    count = 0
    for string in s:
        pair = re.search(r'([a-z]{2}).*\1', string)
        repeats = re.search(r'([a-z]).\1', string)

        if pair and repeats:
            count += 1
    return count


print(part1(input))
print(part2(input))
