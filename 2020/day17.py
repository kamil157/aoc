from itertools import product

input = open('2020/inputs/day17.txt').read()

def neighbors(i, j, k, state):
    adjacent = 0
    for di, dj, dk in product([-1, 0, 1], repeat=3):
        if di == 0 and dj == 0 and dk == 0:
            continue
        neighbor = (i + di, j + dj, k + dk)
        if neighbor[0] in range(len(state)) \
                and neighbor[1] in range(len(state[0])) \
                and neighbor[2] in range(len(state[0][0])) \
                and state[neighbor[0]][neighbor[1]][neighbor[2]] == '#':
            adjacent += 1
    return adjacent

def part1(s):
    state = [s.splitlines()]

    for time in range(6):
        new_state = []
        for i in range(-1, len(state) + 1):
            new_dim = []
            for j in range(-1, len(state[0]) + 1):                
                new_row = ''
                for k in range(-1, len(state[0][0]) + 1):
                    adjacent = neighbors(i, j, k, state)

                    if i in range(len(state)) and j in range(len(state[0])) and k in range(len(state[0][0])) and state[i][j][k] == '#':
                        new_row += '#' if adjacent in [2, 3] else '.'
                    else:
                        new_row += '#' if adjacent == 3 else '.'
                new_dim.append(new_row)
            new_state.append(new_dim)

        state = new_state

    return sum(line.count('#') for dim in state for line in dim)

def neighbors2(i, j, k, l, state):
    adjacent = 0
    for di, dj, dk, dl in product([-1, 0, 1], repeat=4):
        if di == 0 and dj == 0 and dk == 0 and dl == 0:
            continue
        neighbor = (i + di, j + dj, k + dk, l + dl)
        if neighbor[0] in range(len(state)) \
                and neighbor[1] in range(len(state[0])) \
                and neighbor[2] in range(len(state[0][0])) \
                and neighbor[3] in range(len(state[0][0][0])) \
                and state[neighbor[0]][neighbor[1]][neighbor[2]][neighbor[3]] == '#':
            adjacent += 1
    return adjacent

def part2(s):
    state = [s.splitlines()]

    for time in range(6):
        new_state = []
        for i in range(-1, len(state) + 1):
            new_dim = []
            for j in range(-1, len(state[0]) + 1):         
                new_dim2 = []
                for k in range(-1, len(state[0][0]) + 1):            
                    new_row = ''
                    for l in range(-1, len(state[0][0][0]) + 1):
                        adjacent = neighbors2(i, j, k, l, state)

                        if i in range(len(state)) and j in range(len(state[0])) and k in range(len(state[0][0])) and l in range(len(state[0][0][0])) and state[i][j][k][l] == '#':
                            new_row += '#' if adjacent in [2, 3] else '.'
                        else:
                            new_row += '#' if adjacent == 3 else '.'
                    new_dim2.append(new_row)
                new_dim.append(new_dim2)
            new_state.append(new_dim)

        state = new_state

    return sum(line.count('#') for dim2 in state for dim in dim2 for line in dim)

print(part1(input))
print(part2(input))
