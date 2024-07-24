with open('2021/inputs/day20.txt', encoding="utf-8") as f:
    lines = f.read().strip().splitlines()


def part1(iterations):
    algorithm = lines[0]
    image = lines[2:]

    g = {}
    for y, line in enumerate(image):
        for x, pixel in enumerate(line):
            g[x + y*1j] = pixel

    start = 0
    end = len(image) - 1

    background = "."
    for _ in range(iterations):
        start -= 1
        end += 1
        for j in range(start, end + 1):
            g[start + j*1j] = background
            g[end + j*1j] = background
            g[j + start*1j] = background
            g[j + end*1j] = background

        next_g = {}
        for pos, pixel in g.items():
            binary = ""
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    neighbor = g.get(pos + dx + dy*1j, background)
                    binary += "1" if neighbor == "#" else "0"
            next_g[pos] = algorithm[int(binary, 2)]
        g = next_g

        if background == ".":
            background = algorithm[0]
        else:
            background = algorithm[-1]

    return list(g.values()).count("#")


print(part1(2))
print(part1(50))
