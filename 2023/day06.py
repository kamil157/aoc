

import math


with open('2023/inputs/day06.txt') as f:
    lines = f.read().strip().split('\n')


def count_wins(time, best_distance):
    for time_held in range(time):
        time_left = time - time_held
        my_distance = time_left * time_held
        if my_distance > best_distance:
            return time - time_held * 2 + 1


def part1(s):
    times = [int(n) for n in s[0].split()[1:]]
    distances = [int(n) for n in s[1].split()[1:]]
    return math.prod(count_wins(times[race], distances[race]) for race in range(len(times)))


print(part1(lines))


def part2(s):
    time = int("".join(s[0].split()[1:]))
    distance = int("".join(s[1].split()[1:]))
    return count_wins(time, distance)


print(part2(lines))
