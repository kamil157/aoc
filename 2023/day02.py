from math import prod


with open('2023/inputs/day02.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def solve():
    part1 = 0
    part2 = 0
    colors = {"red": 12, "green": 13, "blue": 14}
    for line in lines:
        valid = True
        max_cubes = {"red": 0, "green": 0, "blue": 0}
        game, cubes = line.split(": ")
        game = int(game[5:])
        for roll in cubes.split("; "):
            for cube in roll.split(", "):
                count, color = cube.split()
                count = int(count)
                if count > colors[color]:
                    valid = False
                max_cubes[color] = max(max_cubes[color], count)
        if valid:
            part1 += game
        part2 += prod(max_cubes.values())
    return part1, part2


print(solve())
