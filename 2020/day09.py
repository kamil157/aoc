from collections import deque

input = open('2020/inputs/day09.txt').readlines()

preamble = 25

def is_valid(n, previous):
    nums = set(previous)
    for m in nums:
        if n - m in nums:
            return True
    return False

def part1(s):
    nums = [int(line) for line in s]

    previous = deque()

    for i, n in enumerate(nums):
        if i >= preamble and not is_valid(n, previous):
            return n

        if len(previous) >= preamble:
            previous.popleft()

        previous.append(n)

def part2(s):
    p = part1(s)
    nums = [int(line) for line in s]

    previous = deque()

    for n in nums:
        while sum(previous) >= p:
            if len(previous) >= 2 and sum(previous) == p:
                return min(previous) + max(previous)
            previous.popleft()

        previous.append(n)

print(part1(input))
print(part2(input))
