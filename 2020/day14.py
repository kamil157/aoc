import re
from itertools import product, combinations

input = open('2020/inputs/day14.txt').readlines()


def write1(memory, address, value, mask):
    value = format(int(value), '#038b')[2:]
    result = ''
    for i in range(36):
        result += value[i] if mask[i] == 'X' else mask[i]
    memory[address] = int(result, base=2)

def write2(memory, address, value, mask):
    address = format(int(address), '#038b')[2:]
    masked = ''
    for i in range(36):
        masked += address[i] if mask[i] == '0' else mask[i]

    floating = [i for i, c in enumerate(masked) if c == 'X']
    result = list(masked.replace('X', '0'))
    for r in range(len(floating) + 1):
        for c in combinations(floating, r):
            for pos in floating:
                result[pos] = '1' if pos in c else '0'
            memory[int(''.join(result))] = int(value)

def part1(s, write):
    memory = {}
    for line in s:
        if m := re.search(r'mask = ([01X]{36})', line):
            mask = m[1]
        elif m := re.search(r'mem\[(\d+)\] = (\d+)', line):
            address = m[1]
            value = m[2]
            write(memory, address, value, mask)

    return sum(memory.values())

print(part1(input, write1))
print(part1(input, write2))
