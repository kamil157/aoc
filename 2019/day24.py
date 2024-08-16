with open('2019/inputs/day24.txt', encoding="utf-8") as f:
    input = f.read()


ex1 = """....#
#..#.
#..##
..#..
#...."""


def bugs(s):
    state = s.splitlines()
    history = set()

    while True:
        new_state = []
        for i, row in enumerate(state):
            new_row = ''
            for j, tile in enumerate(row):
                adjacent_bugs = 0
                for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    neighbor = (i + d[0], j + d[1])
                    if 0 <= neighbor[0] < len(state) and 0 <= neighbor[1] < len(row) \
                            and state[neighbor[0]][neighbor[1]] == '#':
                        adjacent_bugs += 1
                if tile == '#':
                    new_row += '#' if adjacent_bugs == 1 else '.'
                if tile == '.':
                    new_row += '#' if adjacent_bugs in [1, 2] else '.'
            new_state.append(new_row)
        print()
        for line in state:
            print(line)

        state_str = ''.join(state)
        if state_str in history:
            print(state)
            diversity = sum(
                [2 ** i for i, tile in enumerate(state_str) if tile == '#'])
            return diversity
        state = new_state
        history.add(state_str)


# print(bugs(ex1))
print(bugs(input))
