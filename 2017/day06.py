with open('2017/inputs/day06.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def part1():
    banks = list(map(int, lines[0].split()))
    seen = {}
    t = 0

    while tuple(banks) not in seen:
        seen[tuple(banks)] = t
        i = banks.index(max(banks))
        blocks = banks[i]
        banks[i] = 0
        for j in range(i + 1, i + 1 + blocks):
            banks[j % len(banks)] += 1
        t += 1
    return len(seen), t - seen[tuple(banks)]


print(part1())
