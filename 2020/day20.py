from collections import Counter
from math import prod

input = open('2020/inputs/day20.txt').read()

def transpose(tile):
    return [''.join(line) for line in zip(*tile)]

def borders(tile):
    t = transpose(tile)
    result = [tile[0], tile[-1], t[0], t[-1]]
    result += [border[::-1] for border in result]
    return result

def part1(s):
    raw_tiles = input.split('\n\n')

    tiles = {}    
    for raw_tile in raw_tiles:
        raw_tile = raw_tile.splitlines()
        n = int(raw_tile[0][5:-1])
        tile = raw_tile[1:]
        tiles[n] = tile

    c = Counter()
    for tile in tiles.values():
        for border in borders(tile):
            c[border] += 1

    corners = [n for n, tile in tiles.items()
               if sum(1 for border in borders(tile) if c[border] == 1) == 4]

    return prod(corners)

print(part1(input))
