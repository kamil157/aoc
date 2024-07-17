with open('2017/inputs/day09.txt', encoding="utf-8") as f:
    lines = f.read().strip()


def part1(s):
    level = 0
    score = 0
    i = 0
    garbage = False
    garbage_score = 0
    while i < len(s):
        c = s[i]
        if garbage:
            if c not in "!>":
                garbage_score += 1
        match c:
            case "{":
                if not garbage:
                    level += 1
            case "}":
                if not garbage:
                    score += level
                    level -= 1
            case "!":
                i += 1
            case "<":
                garbage = True
            case ">":
                garbage = False
        i += 1
    return score, garbage_score


tests1 = [
    ("<>", 0),
    ("<random characters>", 0),
    ("<<<<>", 0),
    ("<{!>}>", 0),
    ("<!!>", 0),
    ("<!!!>>", 0),
    ('<{o"i!a,<{i<a>', 0),
    ("{}", 1),
    ("{{{}}}", 6),
    ("{{},{}}", 5),
    ("{{{},{},{{}}}}", 16),
    ("{<a>,<a>,<a>,<a>}", 1),
    ("{{<ab>},{<ab>},{<ab>},{<ab>}}", 9),
    ("{{<!!>},{<!!>},{<!!>},{<!!>}}", 9),
    ("{{<a!>},{<a!>},{<a!>},{<ab>}}", 3),
]
for s, expected in tests1:
    assert part1(s)[0] == expected, (s, part1(s)[0])
print(part1(lines)[0])

tests2 = [
    ("<>", 0),
    ("<random characters>", 17),
    ("<<<<>", 3),
    ("<{!>}>", 2),
    ("<!!>", 0),
    ("<!!!>>", 0),
    ('<{o"i!a,<{i<a>,', 10),
]
for s, expected in tests2:
    assert part1(s)[1] == expected, (s, part1(s)[1])
print(part1(lines)[1])
