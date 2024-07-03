with open('2021/inputs/day07.txt', encoding="utf-8") as f:
    lines = f.read()


def fuel1(pos, crab):
    return abs(pos - crab)


def fuel2(pos, crab):
    n = abs(pos - crab)
    return n * (n + 1) // 2


def part2(fuel):
    crabs = [int(n) for n in lines.split(",")]
    return min(sum(fuel(pos, crab) for crab in crabs) for pos in range(min(crabs), max(crabs) + 1))


print(part2(fuel1))
print(part2(fuel2))
