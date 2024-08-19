from string import ascii_lowercase


with open('2018/inputs/day05.txt', encoding="utf-8") as f:
    lines = f.read()


def solve(polymer):
    reduced = []
    for a in polymer:
        if reduced and (a.islower() and a.upper() == reduced[-1] or a.isupper() and a.lower() == reduced[-1]):
            reduced.pop()
        else:
            reduced.append(a)

    return len(reduced)


print(solve(lines))


def part2():
    return min(solve(lines.replace(c, '').replace(c.upper(), '')) for c in ascii_lowercase)


print(part2())
