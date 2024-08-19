from itertools import permutations


with open('2017/inputs/day02.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def part1():
    checksum = 0
    for line in lines:
        nums = list(map(int, line.split()))
        checksum += max(nums) - min(nums)
    return checksum


print(part1())


def part2():
    result = 0
    for line in lines:
        nums = list(map(int, line.split()))
        for i, j in permutations(nums, 2):
            if i % j == 0:
                result += i // j
    return result


print(part2())
