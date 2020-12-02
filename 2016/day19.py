input = 3014387

# def part1(s):
#     elves = {i: (i + 1) % s for i in range(s)}
#     i = 0
#     while len(elves) > 1:
#         target = elves[i]
#         elves[i] = elves[target]
#         del elves[target]
#         i = elves[i]
#     return next(iter(elves)) + 1

def part1(s):
    return int(bin(s)[3:] + bin(s)[2], 2)

# def part2(s):
    # elves = {i: (i + s // 2) % s for i in range(s)}
    # i = 0
    # target = (i + len(elves) // 2) % len(elves)
    # while len(elves) > 1:
    #     print(elves)
    #     target = elves[i]
    #     elves[i] = (i + len(elves) // 2) % len(elves)
    #     del elves[target]
    #     i = elves[i]
    # return next(iter(elves)) + 1

print(part1(input))
# print(part2(5))
