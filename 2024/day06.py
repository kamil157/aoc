with open('2024/inputs/day06.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def walk(pos, obstacle):
    direction = -1j
    visited = {(pos, direction)}
    while True:
        next_pos = pos + direction
        if (next_pos, direction) in visited and obstacle is not None:
            return None
        if not (0 <= next_pos.real < len(lines[0]) and 0 <= next_pos.imag < len(lines)):
            return visited

        next_tile = lines[int(next_pos.imag)][int(next_pos.real)]
        if next_tile != '#' and next_pos != obstacle:
            pos = next_pos
        else:
            direction *= 1j
        visited.add((pos, direction))


def solve():
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '^':
                pos = x + y * 1j

    visited = walk(pos, None)
    path = set(pos for pos, _ in visited)
    print(len(path))

    return sum(1 for obstacle in path if not walk(pos, obstacle))


print(solve())
