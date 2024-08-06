from collections import Counter, defaultdict
from math import prod

with open('2020/inputs/day20.txt', encoding="utf-8") as f:
    lines = f.read().split('\n\n')


def rotate(grid):
    return ["".join(l) for l in zip(*grid[::-1])]


def flip_horiz(grid):
    return [line[::-1] for line in grid]


def borders_with_flip(tile):
    result = borders(tile)
    result += [border[::-1] for border in result]
    return result


UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3


def borders(tile):
    t = rotate(tile)
    return [tile[0], t[0], tile[-1], t[-1]]


def variants(grid):
    keys = []
    for _ in range(4):
        grid = rotate(grid)
        keys.append(grid)
    grid = flip_horiz(grid)
    for _ in range(4):
        grid = rotate(grid)
        keys.append(grid)
    return keys


def monster_pattern():
    pattern = r"""                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.splitlines()
    return [(y, x) for y, line in enumerate(pattern) for x, c in enumerate(line) if c == "#"]


def find_monsters(image):
    monster = monster_pattern()
    pixels = set()
    for y in range(len(image)):
        for x in range(len(image[0])):
            is_monster = True
            for dy, dx in monster:
                if not (y + dy < len(image) and x + dx < len(image[0]) and image[y + dy][x + dx] == "#"):
                    is_monster = False
                    break
            if is_monster:
                for dy, dx in monster:
                    pixels.add((y + dy, x + dx))
    return pixels


def draw_image(grid):
    tile_size = 8
    image = [[" "] * (tile_size * len(grid[0]))
             for _ in range(tile_size * len(grid))]
    for ty, line in enumerate(grid):
        for tx, tile in enumerate(line):
            for y, tile_line in enumerate(tile[1:-1]):
                for x, c in enumerate(tile_line[1:-1]):
                    image[tile_size * ty + y][tile_size * tx + x] = c
    return image


def solve():
    tiles = {}
    for tile in lines:
        tile = tile.splitlines()
        n = int(tile[0][5:-1])
        tile = tile[1:]
        tiles[n] = tile

    count = Counter()
    for tile in tiles.values():
        for border in borders_with_flip(tile):
            count[border] += 1

    corners = [n for n, tile in tiles.items()
               if sum(1 for border in borders_with_flip(tile) if count[border] == 1) == 4]
    part1 = prod(corners)

    border_mapping = defaultdict(set)
    for tile_id, tile in tiles.items():
        for border in borders_with_flip(tile):
            border_mapping[border].add(tile_id)

    used = set()
    size = int(len(lines) ** 0.5)
    grid = [[None] * size for _ in range(size)]
    ids = [[None] * size for _ in range(size)]

    def border_count(tile):
        return [count[border] for border in borders(tile)]

    def place_tile(y, x, tile_id, condition):
        for tile in variants(tiles[tile_id]):
            if condition(tile):
                grid[y][x] = tile
                ids[y][x] = tile_id
                used.add(tile_id)
                break

    def is_corner(tile):
        return border_count(tile) == [1, 1, 2, 2]

    # first tile
    place_tile(0, 0, corners[0], is_corner)

    # first row
    for x in range(1, size):
        left = grid[0][x - 1]
        tile_id = list(border_mapping[borders(left)[RIGHT]] - used)[0]

        def is_top_border(tile):
            return borders(left)[RIGHT] == borders(tile)[LEFT] and border_count(tile)[UP] == 1

        place_tile(0, x, tile_id, is_top_border)

    # other rows
    for y in range(1, size):
        up = grid[y - 1][0]
        tile_id = list(border_mapping[borders(up)[DOWN]] - used)[0]

        def is_left_border(tile):
            return borders(up)[DOWN] == borders(tile)[UP] and border_count(tile)[LEFT] == 1

        place_tile(y, 0, tile_id, is_left_border)

        for x in range(1, size):
            up = grid[y - 1][x]
            left = grid[y][x - 1]
            tile_id = list(border_mapping[borders(up)[DOWN]] - used)[0]

            def is_next_piece(tile):
                return borders(up)[DOWN] == borders(tile)[UP] and borders(left)[RIGHT] == borders(tile)[LEFT]

            place_tile(y, x, tile_id, is_next_piece)

    for image in variants(draw_image(grid)):
        if monsters := find_monsters(image):
            result = sum(1 for y, line in enumerate(image) for x, c in enumerate(
                line) if c == "#" and (y, x) not in monsters)
            return part1, result


print(solve())
