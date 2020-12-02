import re

input = open('2020/inputs/day02.txt').readlines()

def validateRange(min, max, letter, password):
    return min <= password.count(letter) <= max

def validatePosition(pos0, pos1, letter, password):
    pos0ok = password[pos0 - 1] == letter
    pos1ok = password[pos1 - 1] == letter
    return pos0ok and not pos1ok or pos1ok and not pos0ok

def part1(s, validate):
    count = 0
    for line in input:
         m = re.search(r'(\d+)-(\d+) (\w): (\w+)', line)
         a, b, letter, password = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
         if validate(a, b, letter, password):
            count += 1

    return count

print(part1(input, validateRange))
print(part1(input, validatePosition))
