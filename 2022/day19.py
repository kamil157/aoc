from collections import deque
from math import prod
from parse import parse

with open('2022/inputs/day19.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def build_bot(limit, i, cost, time, resources, bots, best):
    build = False
    for t in range(time + 1, limit + 1):
        if all(r >= c for r, c in zip(resources, cost)):
            build = True

        resources = tuple(r + b for r, b in zip(resources, bots))
        if build:
            bots = list(bots)
            bots[i] += 1
            bots = tuple(bots)
            resources = tuple(r - c for r, c in zip(resources, cost))

            time_left = limit - t
            if resources[3] + bots[3] * time_left + time_left * (time_left - 1) / 2 > best:
                return t, resources, bots


def next_states(limit, costs, time, resources, bots, best):
    for i, cost in enumerate(costs):
        res = build_bot(limit, i, cost, time, resources, bots, best)
        if res:
            yield res


def max_geodes(costs, limit):
    queue = deque([(0, (0, 0, 0, 0), (1, 0, 0, 0))])
    visited = set()
    best = 0
    while queue:
        state = queue.popleft()
        if state in visited:
            continue
        visited.add(state)

        time, resources, bots = state
        if resources[3] > best:
            best = resources[3] + bots[3] * (limit - time)

        for next_state in next_states(limit, costs, time, resources, bots, best):
            queue.append(next_state)

    return best


def parse_blueprint(line):
    number, ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian = parse(
        "Blueprint {:d}: Each ore robot costs {:d} ore. Each clay robot costs {:d} ore. Each obsidian robot costs {:d} ore and {:d} clay. Each geode robot costs {:d} ore and {:d} obsidian.", line)

    costs = ((ore_ore, 0, 0, 0),
             (clay_ore, 0, 0, 0),
             (obsidian_ore, obsidian_clay, 0, 0),
             (geode_ore, 0, geode_obsidian, 0))

    return number, costs


def part1():
    total = 0
    for line in lines:
        number, costs = parse_blueprint(line)
        total += number * max_geodes(costs, 24)
    return total


print(part1())


def part2():
    return prod(max_geodes(costs, 32) for costs in (parse_blueprint(line)[1] for line in lines[0:3]))


print(part2())
