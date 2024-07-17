# from collections import Counter


with open('2017/inputs/day11.txt', encoding="utf-8") as f:
    lines = f.read().strip()


# def part1():
#     c = Counter(lines.split(","))
#     n, nw, sw = (c["n"] - c["s"], c["nw"] - c["se"], c["sw"] - c["ne"])
#     return nw + sw


# print(part1())


# def part2():
#     steps = lines.split(",")

#     furthest = 0
#     c = Counter()
#     for d in steps:
#         c[d] += 1
#         for i in range(6):
#             dirs = [c["n"], c["ne"], c["se"], c["s"], c["sw"], c["nw"]]
#             nw, n, ne = (dirs[(i + 0) % 6] - dirs[(i + 3) % 6], dirs[(i + 1) %
#                          6] - dirs[(i + 4) % 6], dirs[(i + 2) % 6] - dirs[(i + 5) % 6])
#             dist = n + max(ne, nw)
#             furthest = max(furthest, dist)
#     return furthest


# print(part2())

def part2():
    steps = lines.split(",")
    furthest = 0
    q = r = s = 0
    for d in steps:
        match d:
            case "n":
                s += 1
                r -= 1
            case "ne":
                r -= 1
                q += 1
            case "se":
                q += 1
                s -= 1
            case "s":
                s -= 1
                r += 1
            case "sw":
                r += 1
                q -= 1
            case "nw":
                q -= 1
                s += 1

        dist = max(abs(q), abs(r), abs(s))
        furthest = max(furthest, dist)
    return dist, furthest


print(part2())
