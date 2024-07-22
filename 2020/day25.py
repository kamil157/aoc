from itertools import count

with open('2020/inputs/day25.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def loop_size(subject, public):
    value = 1
    for i in count(1):
        value = (value * subject) % 20201227
        if value == public:
            return i


def part1():
    card, door = [int(n) for n in lines]
    return pow(card, loop_size(7,  door), 20201227)


print(part1())
