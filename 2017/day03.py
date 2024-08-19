inp = 361527


def solve(part2):
    pos = 0
    value = 1
    grid = {pos: 1}
    step = 1
    dir = 1

    while value < inp:
        pos += dir
        if int(pos.real) == step and dir == 1:
            dir = -1j
        elif int(pos.imag) == -step and dir == -1j:
            dir = -1
        elif int(pos.real) == -step and dir == -1:
            dir = 1j
        elif int(pos.imag) == step and dir == 1j:
            dir = 1
            step += 1

        if part2:
            value = sum(grid.get(pos + d, 0)
                        for d in [1, 1j, -1, -1j, 1 - 1j, 1 + 1j, -1 - 1j, -1 + 1j])
        else:
            value += 1
        grid[pos] = value

    if part2:
        return value

    return int(abs(pos.real) + abs(pos.imag))


print(solve(False))
print(solve(True))
