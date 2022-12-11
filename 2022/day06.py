with open('2022/inputs/day06.txt') as f:
    lines = f.read().split('\n')


def part1(marker):
    signal = lines[0]
    for i in range(len(signal)):
        s = set(signal[i:i + marker])
        if len(s) == marker:
            return i + marker


print(part1(4))
print(part1(14))
