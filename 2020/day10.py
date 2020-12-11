from collections import Counter

input = open('2020/inputs/day10.txt').readlines()

def part1(s):
    nums = [int(line) for line in s]
    c = Counter({3: 1})

    current = 0
    for joltage in sorted(nums):
        diff = joltage - current
        c[diff] += 1
        current = joltage

    return c[1] * c[3]

def tribbonacci(n):
    if n == 0: return 1
    if n == 1: return 1
    if n == 2: return 2
    if n == 3: return 4
    if n == 4: return 7

def part2(s):
    nums = [int(line) for line in s]
    nums.append(max(nums) + 3)

    total = 1
    current = 0
    previous = 0
    for joltage in sorted(nums):
        if joltage - current == 3:
            total *= tribbonacci(current - previous)
            previous = joltage

        current = joltage

    return total

print(part1(input))
print(part2(input))
