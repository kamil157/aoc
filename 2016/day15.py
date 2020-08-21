from itertools import count
import re

input = open('2016/inputs/day15.txt').read()

def add_disc(lengths, positions, goal, disc, length, pos):
    lengths.append(length)
    positions.append(pos)
    goal.append( (-disc) % length )

def read_input(s):
    lengths = []
    positions = []
    goal = []
    for line in s.split('\n'):
        m = re.search(r'Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+).', line)
        disc = int(m.group(1))
        length = int(m.group(2))
        pos = int(m.group(3))
        add_disc(lengths, positions, goal, disc, length, pos)
        
    return lengths, positions, goal

def simulate(lengths, positions, goal):
    for time in count():
        for d, p in enumerate(positions):
            positions[d] = (p + 1) % lengths[d]
        
        if positions == goal:
            return time

def part1(s):
    lengths, positions, goal = read_input(s)
    return simulate(lengths, positions, goal)

def part2(s):
    lengths, positions, goal = read_input(s)
    add_disc(lengths, positions, goal, 7, 11, 0)
    return simulate(lengths, positions, goal)

print(part1(input))
print(part2(input))
