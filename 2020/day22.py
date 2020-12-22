from collections import deque

import re

input = open('2020/inputs/day22.txt').read()

def part1(s):
    p1, p2 = s.split('\n\n')
    cards1 = deque(int(card) for card in p1.splitlines()[1:])
    cards2 = deque(int(card) for card in p2.splitlines()[1:])

    while cards1 and cards2:
        c1, c2 = cards1.popleft(), cards2.popleft()
        if c1 > c2:
            cards1.append(c1)
            cards1.append(c2)
        elif c2 > c1:
            cards2.append(c2)
            cards2.append(c1)
        else:
            assert False

    winner = reversed(cards1 if cards1 else cards2)
    return sum(i * card for i, card in enumerate(winner, 1))


print(part1(input))
