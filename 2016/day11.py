from collections import deque
from functools import cache
from itertools import combinations
from parse import findall

with open('2016/inputs/day11.txt', encoding="utf-8") as f:
    lines = f.read().strip().split("\n")


def part1(part2):
    floors = []
    count = 0
    elements = set()
    for line in lines:
        generators = set(m[0]
                         for m in (findall("{:w} generator", line)))
        microchips = set(m[0]
                         for m in (findall("{:w}-compatible microchip", line)))
        elements |= generators | microchips
    elements = [""] + list(elements)
    if part2:
        elements += ["elerium", "dilithium"]

    for line in lines:
        generators = set(elements.index(m[0])
                         for m in (findall("{:w} generator", line)))
        microchips = set(-elements.index(m[0])
                         for m in (findall("{:w}-compatible microchip", line)))
        if part2 and not floors:
            generators |= {elements.index(
                "elerium"), elements.index("dilithium")}
            microchips |= {-elements.index("elerium"), -
                           elements.index("dilithium")}
        count += len(generators) + len(microchips)
        items = frozenset(generators | microchips)
        floors.append(items)

    @cache
    def is_valid(floor):
        s = set(floor)
        for e in range(1, len(elements)):
            if e in s and -e in s:
                s.remove(e)
                s.remove(-e)
        return not (any(e < 0 for e in s) and any(e > 0 for e in floor))

    def step(state):
        elevator, floors, steps = state
        next_steps = []

        for payload in list(combinations(floors[elevator], 1)) + list(combinations(floors[elevator], 2)):
            for next_floor in [elevator - 1, elevator + 1]:
                if 0 <= next_floor < len(floors):
                    new_floors = list(floors)
                    new_floors[elevator] = floors[elevator] - set(payload)
                    new_floors[next_floor] = floors[next_floor] | set(payload)
                    new_floors = tuple(new_floors)

                    if is_valid(new_floors[next_floor]) and is_valid(new_floors[elevator]):
                        next_steps.append((next_floor, new_floors, steps + 1))

        return next_steps

    init = (0, tuple(floors), 0)
    visited = set()
    queue = deque([init])
    best = 0
    while queue:
        elevator, floors, steps = queue.popleft()
        if (elevator, floors) in visited:
            continue
        visited.add((elevator, floors))

        if (steps > best):
            best = steps
            print(best)
        if len(floors[-1]) == count:
            return steps

        for next_state in step((elevator, floors, steps)):
            queue.append(next_state)


print(part1(False))
print(part1(True))
