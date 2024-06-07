

from collections import Counter, defaultdict


with open('2023/inputs/day07.txt') as f:
    lines = f.read().strip().split('\n')


def get_type1(hand):
    count = Counter(hand).most_common()
    if count[0][1] == 5:
        return 0
    if count[0][1] == 4:
        return 1
    if count[0][1] == 3 and count[1][1] == 2:
        return 2
    if count[0][1] == 3:
        return 3
    if count[0][1] == 2 and count[1][1] == 2:
        return 4
    if count[0][1] == 2:
        return 5
    return 6


def part1(cards, get_type, s):
    scores = defaultdict(list)
    for line in lines:
        hand, bid = line.split()
        bid = int(bid)
        type = get_type(hand)
        scores[type].append((hand, bid))

    total = 0
    rank = 1
    for score in sorted(scores, reverse=True):
        hands = scores[score]
        hands.sort(key=lambda hand: sum((len(cards) - cards.index(c))
                   * len(cards) ** (len(hand) - n) for n, c in enumerate(hand[0])))
        for (hand, bid) in hands:
            total += rank * bid
            rank += 1
    return total


print(part1("AKQJT98765432", get_type1, lines))


def get_type2(hand):
    counter = Counter(hand)
    counter['J'] = 0
    count = counter.most_common()
    jokers = hand.count('J')

    if count[0][1] + jokers >= 5:
        return 0
    if count[0][1] + jokers == 4:
        return 1
    if count[0][1] + jokers == 3 and count[1][1] == 2:
        return 2
    if count[0][1] + jokers == 3:
        return 3
    if count[0][1] + jokers == 2 and count[1][1] == 2:
        return 4
    if count[0][1] + jokers == 2:
        return 5
    return 6


print(part1("AKQT98765432J", get_type2, lines))
