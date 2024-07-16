input = 3014387


def part1(s):
    return int(bin(s)[3:] + bin(s)[2], 2)


print(part1(input))


# def part2(n):
#     elves = list(range(1, n + 1))
#     while len(elves) > 1:
#         print(elves)
#         target = len(elves) // 2
#         elves.pop(target)
#         elves = elves[1:] + elves[:1]
#     return elves[0]

def part2(n):
    if n == 1:
        return 1
    k = 1
    while k * 3 < n:
        k *= 3
    if n > 2 * k:
        guess = 2 * n - 3 * k
    else:
        guess = n - k
    return guess


print(part2(input))
