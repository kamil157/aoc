with open('2017/inputs/day16.txt', encoding="utf-8") as f:
    lines = f.read().strip()


def dance(l):
    for move in lines.split(","):
        match move[0]:
            case "s":
                offset = -int(move[1:])
                l = l[offset:] + l[:offset]
            case "x":
                a, b = [int(n) for n in move[1:].split("/")]
                l[a], l[b] = l[b], l[a]
            case "p":
                a, b = [l.index(n) for n in move[1:].split("/")]
                l[a], l[b] = l[b], l[a]
    return l


def part1():
    l = [chr(ord("a") + i) for i in range(16)]
    return "".join(dance(l))


print(part1())


def part2():
    l = [chr(ord("a") + i) for i in range(16)]
    results = ["".join(l)]
    limit = 1000000000
    for i in range(1, limit + 1):
        l = dance(l)
        results.append("".join(l))
        if "".join(l) == results[0]:
            return "".join(results[limit % i])


print(part2())
