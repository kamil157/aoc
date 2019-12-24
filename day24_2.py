input = """.#.##
.#.#.
##.#.
####.
#.###"""

ex1 = """....#
#..#.
#.?##
..#..
#...."""


def bugs(s, time):
    empty = ['.....', '.....', '..?..', '.....', '.....']
    levels = [empty for _ in range(200)]
    levels[100] = s.splitlines()

    for t in range(time):
        new_levels = []
        for l, level in enumerate(levels):
            new_state = []
            for i, row in enumerate(level):
                new_row = ''
                for j, tile in enumerate(row):
                    # count adjacent bugs
                    adjacent_bugs = 0
                    for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        neighbor = (i + d[0], j + d[1])
                        is_inside = 0 <= neighbor[0] < len(level) and 0 <= neighbor[1] < len(row)
                        if is_inside:
                            neighbor_tile = level[neighbor[0]][neighbor[1]]
                            if neighbor_tile == '#':
                                adjacent_bugs += 1
                            elif neighbor_tile == '?' and l + 1 < len(levels):
                                # check inner level
                                inner = levels[l + 1]
                                if (i, j) == (2, 1):
                                    adjacent_bugs += sum(1 for neighbor_tile in inner[1] if
                                                         neighbor_tile == '#')  # TODO verify x y order
                                elif (i, j) == (2, 3):
                                    adjacent_bugs += sum(1 for neighbor_tile in inner[3] if neighbor_tile == '#')
                                elif (i, j) == (1, 2):
                                    adjacent_bugs += sum(1 for i, col in enumerate(inner) for neighbor_tile in col if
                                                         neighbor_tile == '#' and i == 1)
                                elif (i, j) == (3, 2):
                                    adjacent_bugs += sum(1 for i, col in enumerate(inner) for neighbor_tile in col if
                                                         neighbor_tile == '#' and i == 3)
                                else:
                                    assert False
                        else:
                            if l - 1 > 0:
                                # check outer level
                                outer = levels[l - 1]

                                if neighbor[0] < 0:
                                    neighbor_tile = outer[2][1]  # TODO verify x y order
                                elif neighbor[1] < 0:
                                    neighbor_tile = outer[1][2]
                                elif neighbor[0] >= len(level):
                                    neighbor_tile = outer[2][3]
                                elif neighbor[1] >= len(row):
                                    neighbor_tile = outer[3][2]
                                else:
                                    assert False

                                if neighbor_tile == '#':
                                    adjacent_bugs += 1

                    if tile == '#':
                        new_row += '#' if adjacent_bugs == 1 else '.'
                    elif tile == '.':
                        new_row += '#' if adjacent_bugs in [1, 2] else '.'
                    elif tile == '?':
                        new_row += '?'
                    else:
                        assert False
                new_state.append(new_row)

            # if l == 100:
            #     print()
            #     for line in level:
            #         print(line)

            new_levels.append(new_state)
        levels = new_levels

    # print(levels[100])
    print('after 10')
    for l in range(95, 106):
        print(l)
        for line in levels[l]:
            print(line)

    # levels[l] = new_state

    return sum(1 for level in levels for row in level for tile in row if tile == '#')


print(bugs(ex1, 1))
# print(bugs(input, 200))
