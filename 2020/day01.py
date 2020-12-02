input = open('2020/inputs/day01.txt').readlines()

def part1(s):
    nums = set(int(n) for n in input)
    for n in nums:
        if 2020 - n in nums:
            return n * (2020 - n)

def part2(s):
    nums = [int(n) for n in input]
    s = set(nums)
    for i, n in enumerate(nums):
        for m in nums[i:]:
            if 2020 - n - m in s:
                return n * m * (2020 - n - m)

print(part1(input))
print(part2(input))
