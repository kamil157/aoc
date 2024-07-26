from collections import Counter, deque


with open('2022/inputs/day23.txt', encoding="utf-8") as f:
    lines = f.read().split('\n')


def solve(limit):
    elves = set()
    for y, line in enumerate(lines):
        for x, tile in enumerate(line):
            if tile == "#":
                elves.add(x+y*1j)

    order = deque([-1j, 1j, -1, 1])
    for part2 in range(1, limit + 1):
        proposed = {}
        for elf in elves:
            proposed[elf] = elf
            if any(elf + d in elves for d in [-1-1j, -1, -1+1j, -1j, 1j, 1-1j, 1, 1+1j]):
                for d in order:
                    if not any(elf + neighbor in elves for neighbor in [d-d*1j, d, d+d*1j]):
                        proposed[elf] = elf + d
                        break

        collisions = set(pos for pos, count in Counter(
            proposed.values()).items() if count > 1)

        new_elves = set(pos if pos not in collisions else elf
                        for elf, pos in proposed.items())
        if new_elves == elves:
            return part2
        elves = new_elves

        order.rotate(-1)

    part1 = 0
    for y in range(min(int(pos.imag) for pos in elves), max(int(pos.imag) for pos in elves) + 1):
        for x in range(min(int(pos.real) for pos in elves), max(int(pos.real) for pos in elves) + 1):
            if x+y*1j not in elves:
                part1 += 1
    return part1


print(solve(10))
print(solve(1000))
