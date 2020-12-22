from collections import deque

import re

input = open('2020/inputs/day22.txt').read()

def part1(s):
    p1, p2 = s.split('\n\n')
    cards1 = deque(int(card) for card in p1.splitlines()[1:])
    cards2 = deque(int(card) for card in p2.splitlines()[1:])

    while cards1 and cards2:
        c1, c2 = cards1.popleft(), cards2.popleft()
        winner = cards1 if c1 > c2 else cards2
        winner.append(max(c1, c2))
        winner.append(min(c1, c2))

    return points(cards1 if cards1 else cards2)

def serialize(cards1, cards2):
    return tuple(cards1), tuple(cards2)

def points(cards):
    return sum(i * card for i, card in enumerate(reversed(cards), 1))

def recursive(cards1, cards2):
    cards1 = deque(cards1)
    cards2 = deque(cards2)

    visited = set()
    while cards1 and cards2:
        if serialize(cards1, cards2) in visited:
            return (1, cards1)
        
        visited.add(serialize(cards1, cards2))
        c1, c2 = cards1.popleft(), cards2.popleft()
        
        if len(cards1) >= c1 and len(cards2) >= c2:
            winner = recursive([cards1[i] for i in range(c1)],
                               [cards2[i] for i in range(c2)])[0]
        else:    
            winner = 1 if c1 > c2 else 2

        winner_cards = cards1 if winner == 1 else cards2
        winner_cards.append(c1 if winner == 1 else c2)
        winner_cards.append(c2 if winner == 1 else c1)

    return (1, cards1) if cards1 else (2, cards2)

def part2(s):
    p1, p2 = s.split('\n\n')
    cards1 = [int(card) for card in p1.splitlines()[1:]]
    cards2 = [int(card) for card in p2.splitlines()[1:]]
    return points(recursive(cards1, cards2)[1])


print(part1(input))
print(part2(input))
