def power(x, y):
    rack = x + 10
    p = rack * y
    p += 1955
    p *= rack
    p = p // 100 % 10
    p -= 5
    return p


def part2(sizes):
    best = 0
    result = (0, 0, 0)
    t = [[0] * 301 for _ in range(301)]

    for x in range(1, 301):
        for y in range(1, 301):
            t[y][x] = power(x, y) + t[y - 1][x] + t[y][x - 1] - t[y - 1][x - 1]

    for size in sizes:
        for x in range(1, 301 - size):
            for y in range(1, 301 - size):
                total = t[y + size][x + size] + t[y][x] - \
                    t[y + size][x] - t[y][x + size]
                if total > best:
                    best = total
                    result = x + 1, y + 1, size
    return result


print(part2([3]))
print(part2(range(1, 301)))
