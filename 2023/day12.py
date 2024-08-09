from functools import cache


with open('2023/inputs/day12.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def part1(mul):
    total = 0
    for line in lines:
        springs, sizes = line.split()
        springs += "?"
        springs *= mul
        sizes = [int(n) for n in sizes.split(",")] * mul

        @cache
        def count(p, s, result=0):
            if p == len(springs):
                return s == len(sizes)

            if springs[p] in ".?":
                result += count(p+1, s)

            if s < len(sizes):
                end = p + sizes[s]
                if end < len(springs) and "." not in springs[p:end] and springs[end] != "#":
                    result += count(end + 1, s + 1)

            return result

        total += count(0, 0)
    return total


print(part1(1))
print(part1(5))
