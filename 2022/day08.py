with open('2022/inputs/day08.txt') as f:
    lines = f.read().split('\n')


def part1():
    trees = [[int(h) for h in line] for line in lines]
    transposed = [*zip(*trees)]
    count = 0
    for j in range(len(trees)):
        for i in range(len(trees[j])):
            horizontal = trees[j][i] > max(trees[j][:i], default=-1) or trees[j][i] > max(trees[j][i + 1:], default=-1)
            vertical = transposed[i][j] > max(transposed[i][:j], default=-1) or transposed[i][j] > max(
                transposed[i][j + 1:], default=-1)
            if horizontal or vertical:
                count += 1
    return count


def scenic(trees, j, i, start, end, step):
    distance = 0
    for x in range(start, end, step):
        distance += 1
        if trees[j][x] >= trees[j][i]:
            break
    return distance


def part2():
    trees = [[int(h) for h in line] for line in lines]
    transposed = [*zip(*trees)]
    scores = []
    for j in range(len(trees)):
        for i in range(len(trees[j])):
            score = scenic(trees, j, i, i + 1, len(trees[j]), 1)
            score *= scenic(trees, j, i, i - 1, -1, -1)
            score *= scenic(transposed, i, j, j + 1, len(trees), 1)
            score *= scenic(transposed, i, j, j - 1, -1, -1)
            scores.append(score)
    return max(scores)


print(part1())
print(part2())
