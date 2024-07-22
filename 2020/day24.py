with open('2020/inputs/day24.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def parse_tile(s, init=(0, 0, 0)):
    i = 0
    x, y, z, = init
    while i < len(s):
        match s[i]:
            case "e":
                x += 1
                z += 1
            case "w":
                x -= 1
                z -= 1
            case "n":
                y -= 1
                i += 1
                match s[i]:
                    case "e":
                        z += 1
                match s[i]:
                    case "w":
                        x -= 1
            case "s":
                y += 1
                i += 1
                match s[i]:
                    case "e":
                        x += 1
                match s[i]:
                    case "w":
                        z -= 1
        i += 1
    return x, y, z


def solve():
    black = set()
    for line in lines:
        tile = parse_tile(line)
        if tile in black:
            black.remove(tile)
        else:
            black.add(tile)

    part1 = len(black)

    directions = ["e", "w", "ne", "nw", "se", "sw"]

    def black_neighbors(tile):
        result = 0
        for direction in directions:
            neighbor = parse_tile(direction, tile)
            if neighbor in black:
                result += 1
        return result

    def white():
        neighbors = set()
        for tile in black:
            for direction in directions:
                neighbors.add(parse_tile(direction, tile))
        return neighbors - black

    for _ in range(100):
        next_black = set(black)

        for tile in black:
            count = black_neighbors(tile)
            if count == 0 or count > 2:
                next_black.remove(tile)

        for tile in white():
            count = black_neighbors(tile)
            if count == 2:
                next_black.add(tile)

        black = next_black

    return part1, len(black)


print(solve())
