with open('2018/inputs/day18.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def serialize(g):
    out = ""
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            out += g[x + y * 1j]
    return out


def resource_value(g):
    return list(g.values()).count("|") * list(g.values()).count("#")


def part2(limit):
    g = {}
    for y, line in enumerate(lines):
        for x, node in enumerate(line):
            g[x + y * 1j] = node

    seen = {}
    values = []
    for i in range(limit):
        if serialize(g) in seen:
            period = i - seen[serialize(g)]
            cycles = (limit - i) // period
            return values[limit - cycles * period - period]

        seen[serialize(g)] = i
        values.append(resource_value(g))

        next_g = dict(g)
        for pos, node in g.items():
            directions = [-1-1j, -1, -1+1j, -1j, 1j, 1-1j, 1, 1+1j]
            adjacent = [g.get(pos + d, ".") for d in directions]

            if node == ".":
                if adjacent.count("|") >= 3:
                    next_g[pos] = "|"
            elif node == "|":
                if adjacent.count("#") >= 3:
                    next_g[pos] = "#"
            else:
                if not (adjacent.count("#") >= 1 and adjacent.count("|") >= 1):
                    next_g[pos] = "."

        g = next_g

    return resource_value(g)


print(part2(10))
print(part2(1000000000))
