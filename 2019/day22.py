with open('2019/inputs/day22.txt', encoding="utf-8") as f:
    input = f.read()


ex1 = """deal with increment 7
deal into new stack
deal into new stack"""

ex2 = """cut 6
deal with increment 7
deal into new stack"""

ex3 = """deal with increment 7
deal with increment 9
cut -2"""

ex4 = """deal into new stack
cut -2
deal with increment 7
cut 8
cut -4
deal with increment 7
cut 3
deal with increment 9
deal with increment 3
cut -1"""


def shuffle_deck(s, deck):
    commands = s.splitlines()

    for command in commands:
        if command == 'deal into new stack':
            deck.reverse()
        elif command.startswith('cut '):
            split = int(command.replace('cut ', ''))
            deck = deck[split:] + deck[:split]
        elif command.startswith('deal with increment '):
            increment = int(command.replace('deal with increment ', ''))
            new_deck = deck.copy()
            for i in range(len(deck)):
                new_deck[(i * increment) % len(deck)] = deck[i]
            deck = new_deck

    return deck


def shuffle(s, n):
    return shuffle_deck(s, list(range(n)))


assert (shuffle(ex1, 10)) == [0, 3, 6, 9, 2, 5, 8, 1, 4, 7]
assert (shuffle(ex2, 10)) == [3, 0, 7, 4, 1, 8, 5, 2, 9, 6]
assert (shuffle(ex3, 10)) == [6, 3, 0, 7, 4, 1, 8, 5, 2, 9]
assert (shuffle(ex4, 10)) == [9, 2, 5, 8, 1, 4, 7, 0, 3, 6]
print(shuffle(input, 10007).index(2019))  # 5540


def inv(n, m):
    return pow(n, m - 2, m)


def shuffle_smart(s, m, iterations, pos):
    commands = s.splitlines()
    offset = 0
    increment = 1
    for command in commands:
        if command == 'deal into new stack':
            increment *= -1
            increment %= m
            offset += increment
            offset %= m
        elif command.startswith('cut '):
            n = int(command.replace('cut ', ''))
            offset += increment * n
            offset %= m
        elif command.startswith('deal with increment '):
            n = int(command.replace('deal with increment ', ''))
            increment *= inv(n, m)
            increment %= m

    total_increment = pow(increment, iterations, m)
    total_offset = offset * (1 - total_increment) * inv((1 - increment), m) % m
    return (total_offset + total_increment * pos) % m


print(shuffle_smart(input, 119315717514047, 101741582076661, 2020))
