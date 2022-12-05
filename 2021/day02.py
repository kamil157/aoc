input = open('2021/inputs/day02.txt').readlines()

def part1(s):
    x = y = aim = 0
    for line in input:
        match line.split():
            case 'forward', n:
                x += int(n)
                y += int(n) * aim
            case 'down', n:
                aim += int(n)
            case 'up', n:
                aim -= int(n)
    return x * aim, x * y


print(part1(input))  # 2091984, 2086261056
