with open('2025/inputs/day07.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def part1():
    m = [list(line) for line in lines]
    
    splits = 0
    for i in range(len(m) - 1):
        for j, c in enumerate(m[i]):
            if c in "S|":
                if m[i + 1][j] == ".":
                    m[i + 1][j] = "|"
                elif m[i + 1][j] == "^":
                    splits += 1
                    m[i + 1][j - 1] = "|"
                    m[i + 1][j + 1] = "|"
    return splits

def part2():
    m = [list(line) for line in lines]
    
    splits = [0] * len(m[0])
    for i in range(len(m) - 1):
        for j, c in enumerate(m[i]):
            if c == "S":
                splits[j] = 1
            if c in "S|":
                if m[i + 1][j] == ".":
                    m[i + 1][j] = "|"
                elif m[i + 1][j] == "^":
                    m[i + 1][j - 1] = "|"
                    m[i + 1][j + 1] = "|"
                    splits[j - 1] += splits[j]
                    splits[j + 1] += splits[j]
                    splits[j] = 0
    return sum(splits)
        
print(part1())
print(part2())
