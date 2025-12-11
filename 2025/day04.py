with open('2025/inputs/day04.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def part1():
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    accessible = 0
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "@":
                papers = 0
                for d in dirs:
                    a_y, a_x = y + d[0], x + d[1]
                    if 0 <= a_y < len(lines) and 0 <= a_x < len(lines[0]):
                        if lines[a_y][a_x] == "@":
                            papers += 1
                if papers < 4:
                    accessible += 1
    return accessible

def part2():
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    removed = set()
    change = False
    while True:
        accessible = 0
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == "@" and (y, x) not in removed:
                    papers = 0
                    forklifts = 0
                    for d in dirs:
                        a_y, a_x = y + d[0], x + d[1]
                        if 0 <= a_y < len(lines) and 0 <= a_x < len(lines[0]):
                            if lines[a_y][a_x] == "@" and (a_y, a_x) not in removed:
                                papers += 1
                    if papers < 4:
                        accessible += 1
                        removed.add(((y, x)))
        if not accessible:
            return len(removed)

        
print(part1())
print(part2())
