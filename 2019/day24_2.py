with open('2019/inputs/day24_2.txt', encoding="utf-8") as f:
    input = f.read()


ex1 = """....#
#..#.
#.?##
..#..
#...."""


def count_adjacent(levels, level, l, row, y, x):
    adjacent_bugs = 0
    for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        neighbor = (y + d[0], x + d[1])
        is_inside = 0 <= neighbor[0] < len(
            level) and 0 <= neighbor[1] < len(row)
        if is_inside:
            neighbor_tile = level[neighbor[0]][neighbor[1]]
            if neighbor_tile == '#':
                adjacent_bugs += 1
            elif neighbor_tile == '?' and l + 1 < len(levels):
                # check inner level
                inner = levels[l + 1]
                if (y, x) == (2, 1):
                    adj = sum(1 for neighbor_tile in list(
                        zip(*inner))[0] if neighbor_tile == '#')
                elif (y, x) == (2, 3):
                    adj = sum(1 for neighbor_tile in list(
                        zip(*inner))[4] if neighbor_tile == '#')
                elif (y, x) == (1, 2):
                    adj = sum(
                        1 for neighbor_tile in inner[0] if neighbor_tile == '#')
                elif (y, x) == (3, 2):
                    adj = sum(
                        1 for neighbor_tile in inner[4] if neighbor_tile == '#')
                else:
                    assert False
                adjacent_bugs += adj
        else:
            if l - 1 > 0:
                # check outer level
                outer = levels[l - 1]

                if neighbor[0] < 0:
                    neighbor_tile = outer[1][2]
                elif neighbor[1] < 0:
                    neighbor_tile = outer[2][1]
                elif neighbor[0] >= len(level):
                    neighbor_tile = outer[3][2]
                elif neighbor[1] >= len(row):
                    neighbor_tile = outer[2][3]
                else:
                    assert False

                if neighbor_tile == '#':
                    adjacent_bugs += 1
    return adjacent_bugs


def bugs(s, time):
    empty = ['.....', '.....', '..?..', '.....', '.....']
    levels = [empty for _ in range(230)]
    levels[115] = s.splitlines()

    for _ in range(time):
        new_levels = []
        for l, level in enumerate(levels):
            new_state = []
            for y, row in enumerate(level):
                new_row = ''
                for x, tile in enumerate(row):
                    # count adjacent bugs
                    adjacent_bugs = count_adjacent(levels, level, l, row, y, x)
                    if tile == '#':
                        new_row += '#' if adjacent_bugs == 1 else '.'
                    elif tile == '.':
                        new_row += '#' if adjacent_bugs in [1, 2] else '.'
                    elif tile == '?':
                        new_row += '?'
                    else:
                        assert False
                new_state.append(new_row)

            new_levels.append(new_state)
        levels = new_levels

    return sum(1 for level in levels for row in level for tile in row if tile == '#')


# print(bugs(ex1, 10))
print(bugs(input, 200))
