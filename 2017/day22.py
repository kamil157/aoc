with open('2017/inputs/day22.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def part1():
    infected = {x+y*1j for y, row in enumerate(lines)
                for x, tile in enumerate(row) if tile == "#"}

    bursts = 0
    pos = len(lines[0]) // 2 + len(lines) // 2 * 1j
    d = -1j
    for _ in range(10000):
        if pos in infected:
            d *= 1j
            infected.remove(pos)
        else:
            d *= -1j
            infected.add(pos)
            bursts += 1
        pos += d
    return bursts


print(part1())


def part2():
    grid = {x+y*1j: "i" for y, row in enumerate(lines)
            for x, tile in enumerate(row) if tile == "#"}

    bursts = 0
    pos = len(lines[0]) // 2 + len(lines) // 2 * 1j
    d = -1j
    for _ in range(10000000):
        tile = grid.get(pos, "c")
        if tile == "i":
            d *= 1j
            grid[pos] = "f"
        elif tile == "f":
            d *= -1
            grid[pos] = "c"
        elif tile == "w":
            grid[pos] = "i"
            bursts += 1
        elif tile == "c":
            d *= -1j
            grid[pos] = "w"
        pos += d
    return bursts


print(part2())
