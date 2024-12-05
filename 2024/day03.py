from re import findall

with open('2024/inputs/day03.txt', encoding="utf-8") as f:
    lines = f.read()


def solve():
    m = findall(r"mul\((\d+),(\d+)\)", lines)
    part1 = sum([int(a) * int(b) for a, b in m])

    part2 = 0
    do = True
    m = findall(r"(mul)\((\d+),(\d+)\)|(do)\(\)|(don't)\(\)", lines)
    for instr in m:
        if "do" in instr:
            do = True
        elif "don't" in instr:
            do = False
        elif "mul" in instr and do:
            part2 += int(instr[1]) * int(instr[2])
    return part1, part2


print(solve())
