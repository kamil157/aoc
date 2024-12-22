with open('2024/inputs/day22.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def prune(n):
    return n % 16777216


def mix(n, m):
    return n ^ m


def solve():
    total = 0
    for line in lines:
        n = int(line)
        for _ in range(2000):
            n = prune(mix(n, n * 64))
            n = prune(mix(n, n // 32))
            n = prune(mix(n, n * 2048))

        total += n
    return total


print(solve())
