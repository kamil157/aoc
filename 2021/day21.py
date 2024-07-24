from functools import cache
from itertools import product


with open('2021/inputs/day21.txt', encoding="utf-8") as f:
    lines = f.read().strip().splitlines()


def part1():
    p1 = int(lines[0][-1])
    p2 = int(lines[1][-1])

    pos = [p1, p2]
    scores = [0, 0]
    die = 1
    rolls = 0
    player = 0
    while max(scores) < 1000:
        move = 0
        for _ in range(3):
            move += die
            die = (die + 1) % 100
            rolls += 1

        pos[player] = (pos[player] + move) % 10
        scores[player] += pos[player] if pos[player] > 0 else 10
        player = (player + 1) % 2

    return rolls * min(scores)


print(part1())


def part2():
    p1 = int(lines[0][-1])
    p2 = int(lines[1][-1])

    @cache
    def helper(player, pos_, scores_):
        if scores_[0] >= 21:
            return 1, 0
        elif scores_[1] >= 21:
            return 0, 1

        result = [0, 0]
        for dice in product([1, 2, 3], repeat=3):
            pos = list(pos_)
            scores = list(scores_)
            pos[player] = (pos[player] + sum(dice)) % 10
            scores[player] += pos[player] if pos[player] > 0 else 10

            w1, w2 = helper((player + 1) % 2, tuple(pos), tuple(scores))
            result[0] += w1
            result[1] += w2
        return result

    player = 0
    pos = (p1, p2)
    scores = (0, 0)
    return max(helper(player, pos, scores))


print(part2())
