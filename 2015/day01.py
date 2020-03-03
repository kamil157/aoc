input = open('2015/inputs/day01.txt').read()

def part1(s):
    return s.count('(') - s.count(')')

def part2(s):
    floor = 0
    for i, c in enumerate(s, 1):
        floor += 1 if c == '(' else -1
        if floor == -1:
            return i


print(part1(input))
print(part2(input))
