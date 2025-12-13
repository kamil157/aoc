import math

with open('2025/inputs/day06.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def part1():
    problems = []
    for line in lines:
        problems.append(line.split())
    problems = list(zip(*problems))

    total = 0
    for p in problems:
        f = sum if p[-1] == "+" else math.prod
        total += f(int (n) for n in p[:-1])
    return total

def part2():
    total = 0
    nums = []
    for i in range(len(lines[0]) - 1, -1, -1):
        digits = ""
        result = 0
        for j in range(len(lines)):
            c = lines[j][i]
            if j == len(lines) - 1:
                if digits:
                    nums.append(int(digits))
                if c in "+*":
                    f = sum if c == "+" else math.prod
                    result += f(nums)
                    nums = []
            elif c != " ":
                digits += c
        total += result
    return total
        
print(part1())
print(part2())
