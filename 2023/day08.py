

import math


with open('2023/inputs/day08.txt') as f:
    lines = f.read().strip().split('\n')


def parse_network(lines):
    network = lines[2:]
    network_map = {}

    for node in network:
        start = node[0:3]
        left = node[7:10]
        right = node[12:15]

        network_map[start] = {"L": left, "R": right}
    return network_map


def part1(s):
    instructions = lines[0]
    network_map = parse_network(lines)

    steps = 0
    current = "AAA"

    while current != "ZZZ":
        current = network_map[current][instructions[steps % len(instructions)]]
        steps += 1

    return steps


print(part1(lines))


def part2(s):
    instructions = lines[0]
    network_map = parse_network(lines)

    steps = []
    starts = []
    for node in network_map:
        if node[2] == "A":
            steps.append(0)
            starts.append(node)

    for i, node in enumerate(starts):
        while node[2] != "Z":
            node = network_map[node][instructions[steps[i] %
                                                  len(instructions)]]
            steps[i] += 1

    return math.lcm(*steps)


print(part2(lines))
