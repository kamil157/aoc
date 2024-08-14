from collections import deque
from itertools import count
from math import inf


with open('2018/inputs/day15.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')

directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def enemy(c):
    return "E" if c == "G" else "G"


def find_targets(g, c):
    return [(y, x) for y, r in enumerate(g) for x, e in enumerate(r) if e == enemy(c)]


def already_in_range(y, x, enemies):
    return any((y + dy, x + dx) in enemies for dy, dx in directions)


def adjacent_enemies(g, y, x, c):
    return [(y + dy, x + dx) for dy, dx in directions if g[y + dy][x + dx] == enemy(c)]


def find_in_range(g, enemies):
    return {(y + dy, x + dx) for y, x in enemies for dy, dx in directions if g[y + dy][x + dx] == "."}


def find_nearest(g, y, x, in_range):
    shortest = inf
    reachable = {}
    queue = deque([(y, x, 0)])
    visited = set()
    while queue:
        y, x, d = queue.popleft()
        if (y, x) in visited:
            continue
        visited.add((y, x))

        if d > shortest:
            break

        if (y, x) in in_range:
            shortest = min(shortest, d)
            reachable[(y, x)] = d

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if g[ny][nx] == ".":
                queue.append((ny, nx, d + 1))

    return reachable


def find_first_step(g, uy, ux, chosen, steps):
    for sy, sx in directions:
        if g[uy + sy][ux + sx] != ".":
            continue

        queue = deque([(uy + sy, ux + sx, 0)])
        visited = set()
        while queue:
            y, x, d = queue.popleft()
            if (y, x) in visited:
                continue
            visited.add((y, x))

            if d == steps:
                break

            if (y, x) == chosen:
                return (uy + sy, ux + sx)

            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if g[ny][nx] == ".":
                    queue.append((ny, nx, d + 1))


def move(g, y, x, c, hp_map):
    enemies = find_targets(g, c)

    if already_in_range(y, x, enemies):
        return y, x

    if not (in_range := find_in_range(g, enemies)):
        return y, x

    if not (nearest := find_nearest(g, y, x, in_range)):
        return y, x

    chosen = min(nearest.keys())
    step_y, step_x = find_first_step(g, y, x, chosen, nearest[chosen])

    g[step_y][step_x], g[y][x] = g[y][x], g[step_y][step_x]
    hp_map[(step_y, step_x)] = hp_map[(y, x)]
    del hp_map[(y, x)]

    return step_y, step_x


def attack(g, y, x, c, hp_map, bonus, all_elves_alive):
    adjacent = adjacent_enemies(g, y, x, c)
    if not adjacent:
        return all_elves_alive

    target = min(adjacent, key=lambda enemy: (hp_map[enemy], enemy))

    damage = 3
    if c == "E":
        damage += bonus
    hp_map[target] -= damage

    if hp_map[target] <= 0:
        g[target[0]][target[1]] = "."
        del hp_map[target]
        if c == "G":
            return False
    return all_elves_alive


def part1(bonus=0):
    g = [list(line) for line in lines]
    all_elves_alive = True

    hp_map = {(y, x): 200 for y, r in enumerate(g)
              for x, e in enumerate(r) if e in "EG"}

    for i in count():
        queue = deque()
        for y, row in enumerate(g):
            for x, c in enumerate(row):
                if c in "EG":
                    queue.append((y, x, c))

        while queue:
            y, x, c = queue.popleft()
            if (y, x) not in hp_map:
                continue
            enemies = find_targets(g, c)
            if not enemies:
                return all_elves_alive, i * sum(hp_map.values())
            y, x = move(g, y, x, c, hp_map)
            all_elves_alive = attack(
                g, y, x, c, hp_map, bonus, all_elves_alive)


print(part1()[1])


def part2():
    for i in count():
        result = part1(i)
        if result[0]:
            return result[1]


print(part2())
