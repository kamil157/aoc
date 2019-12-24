input = """deal with increment 34
deal into new stack
cut 1712
deal into new stack
cut 1984
deal with increment 62
deal into new stack
deal with increment 13
deal into new stack
deal with increment 67
cut -5590
deal with increment 63
cut -1086
deal with increment 52
cut 7894
deal with increment 71
cut -864
deal into new stack
cut 239
deal with increment 17
cut -7187
deal with increment 62
deal into new stack
cut -7380
deal with increment 14
cut 3842
deal into new stack
cut -5258
deal with increment 40
deal into new stack
deal with increment 45
cut -6026
deal with increment 21
cut 3600
deal with increment 56
cut 2329
deal into new stack
deal with increment 13
cut -2409
deal with increment 49
cut 294
deal into new stack
cut 4776
deal with increment 17
cut 5801
deal with increment 43
cut 8999
deal with increment 46
cut -8527
deal with increment 4
deal into new stack
cut -6767
deal into new stack
deal with increment 33
cut -532
deal with increment 29
deal into new stack
deal with increment 56
cut 6867
deal with increment 70
cut 4276
deal into new stack
cut -5621
deal with increment 56
cut -2966
deal with increment 70
deal into new stack
deal with increment 51
cut -4097
deal with increment 42
deal into new stack
cut -5180
deal with increment 61
deal into new stack
cut 5367
deal with increment 50
cut 3191
deal with increment 75
cut 915
deal with increment 72
cut -3893
deal with increment 22
cut -3405
deal with increment 30
cut -6509
deal with increment 31
cut -7220
deal with increment 45
cut 6489
deal with increment 70
cut -4047
deal into new stack
deal with increment 75
cut 3980
deal with increment 10
cut 9677
deal into new stack
deal with increment 45
cut -6969
deal into new stack"""

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
                new_deck[(i *  increment) % len(deck)] = deck[i]
            deck = new_deck
        print(deck, 'after', command)

    return deck


def shuffle(s, n):
    return shuffle_deck(s, list(range(n)))
    

assert (shuffle(ex1, 10)) == [0, 3, 6, 9, 2, 5, 8, 1, 4, 7]
# assert (shuffle(ex2, 10)) == [3, 0, 7, 4, 1, 8, 5, 2, 9, 6]
# assert (shuffle(ex3, 10)) == [6, 3, 0, 7, 4, 1, 8, 5, 2, 9]
# assert (shuffle(ex4, 10)) == [9, 2, 5, 8, 1, 4, 7, 0, 3, 6]
# print(shuffle(input, 10007).index(2019))  # 5540
# print(shuffle(input, 10007)[2020])


def shuffle_smart(s, n, pos):
    commands = reversed(s.splitlines())
    for command in commands:
        print(pos, 'before', command)
        if command == 'deal into new stack':
            pos = -pos  
        elif command.startswith('cut '):
            split = int(command.replace('cut ', ''))
            pos = (pos + split) % n
            # deck = deck[split:] + deck[:split]
        elif command.startswith('deal with increment '):
            increment = int(command.replace('deal with increment ', ''))
            pos = (increment * pos) % n
            # new_deck = deck.copy()
            # for i in range(len(deck)):
            #     new_deck[(i *  increment) % len(deck)] = deck[i]
            # deck = new_deck
    return pos

print(shuffle_smart(ex1, 10, 1))
# print(shuffle_smart(input, 10007, 2020))
# print(shuffle_smart(input, 119315717514047, 2020))