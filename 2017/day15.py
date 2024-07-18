with open('2017/inputs/day15.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def generate(n, mul, mod):
    n = (n * mul) % 2147483647
    while n % mod != 0:
        n = (n * mul) % 2147483647
    return n


def part2(limit, moda, modb):
    a = int(lines[0].split()[-1])
    b = int(lines[1].split()[-1])

    score = 0
    for _ in range(limit):
        a = generate(a, 16807, moda)
        b = generate(b, 48271, modb)

        if a & 0xFFFF == b & 0xFFFF:
            score += 1
    return score


print(part2(40_000_000, 1, 1))
print(part2(5_000_000, 4, 8))
