with open('2024/inputs/day07.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def calc(params, i, acc, results, concat):
    if i == len(params):
        results.add(acc)
    else:
        calc(params, i + 1, acc + params[i], results, concat)
        calc(params, i + 1, acc * params[i], results, concat)
        if concat:
            calc(params, i + 1, int(str(acc) +
                 str(params[i])), results, concat)


def solve(concat):
    total = 0
    for line in lines:
        left, right = line.split(": ")
        result = int(left)
        params = [int(n) for n in right.split(" ")]

        results = set([params[0]])
        calc(params, 1, params[0], results, concat)
        if result in results:
            total += result
    return total


print(solve(False))
print(solve(True))
