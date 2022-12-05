input = open('2021/inputs/day01.txt').readlines()

def part1(s, step):
    return sum(int(x) < int(y) for x, y in zip(input, input[step:]))


print(part1(input, 1))  # 1696
print(part1(input, 3))  # 1737
