import re

input = open('2020/inputs/day18.txt').readlines()

def calc_single(m):
    return str(int(m[1]) * int(m[3]) if m[2] == '*' else int(m[1]) + int(m[3]))

def calc_simple1(line):
    while '+' in line or '*' in line:
        line = re.sub(r'(\d+)(\+|\*)(\d+)', calc_single, line, count=1)
    return line

def calc_simple2(line):
    while '+' in line:
        line = re.sub(r'(\d+)(\+)(\d+)', calc_single, line, count=1)

    while '*' in line:
        line = re.sub(r'(\d+)(\*)(\d+)', calc_single, line, count=1)
    return line

def calc(m, calc_simple):
    return calc_simple(m[0])[1:-1]

def part1(s, calc_simple):
    total = 0
    for line in s:
        line = line.strip().replace(' ', '')

        while '(' in line:
            line = re.sub(r'\([^()]*\)', lambda s: calc(s, calc_simple), line)

        result = int(calc_simple(line))
        total += result
    return total

print(part1(input, calc_simple1))
print(part1(input, calc_simple2))
