with open('2023/inputs/day13.txt') as f:
    lines = f.read().strip().split('\n\n')


def find_mirror(pattern, weight, smudges):
    for i in range(1, len(pattern)):
        a = pattern[:i]
        b = pattern[i:2*i]

        if len(a) > len(b):
            a = a[len(a) - len(b):]
        a = "".join(a)
        b = "".join(b[::-1])

        if sum(a[i] != b[i] for i in range(len(a))) == smudges:
            return weight * i
    return 0


def part1(smudges):
    total = 0
    for pattern in lines:
        pattern = pattern.split('\n')
        total += find_mirror(pattern, 100, smudges)
        total += find_mirror(["".join(row)
                             for row in zip(*pattern)], 1, smudges)
    return total


print(part1(0))
print(part1(1))
