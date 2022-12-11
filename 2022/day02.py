input = open('2022/inputs/day02.txt').readlines()


def match_score(opponent, me):
    if (me == 'X' and opponent == 'C') or (me == 'Y' and opponent == 'A') or (me == 'Z' and opponent == 'B'):
        return 6
    if (me == 'X' and opponent == 'A') or (me == 'Y' and opponent == 'B') or (me == 'Z' and opponent == 'C'):
        return 3
    return 0


def part1(s):
    score = 0

    scores = {'X': 1, 'Y': 2, 'Z': 3}
    for line in s:
        opponent, me = line.split()
        score += scores[me]
        score += match_score(opponent, me)

    return score


def choose(opponent, result):
    if (opponent == 'A' and result == 'Y') or (opponent == 'B' and result == 'X') or (
            opponent == 'C' and result == 'Z'):
        return 'X'
    if (opponent == 'A' and result == 'Z') or (opponent == 'B' and result == 'Y') or (
            opponent == 'C' and result == 'X'):
        return 'Y'
    return 'Z'


def part2(s):
    score = 0

    scores = {'X': 1, 'Y': 2, 'Z': 3}
    for line in s:
        opponent, result = line.split()

        me = choose(opponent, result)

        score += scores[me]
        score += match_score(opponent, me)

    return score


print(part1(input))
print(part2(input))
