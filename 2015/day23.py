with open('2015/inputs/day23.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def part1(a):
    r = {"a": a, "b": 0}
    offset = 0
    while offset < len(lines):
        op = lines[offset].replace(",", "").split()
        next_offset = offset + 1
        match op[0]:
            case "hlf":
                r[op[1]] //= 2
            case "tpl":
                r[op[1]] *= 3
            case "inc":
                r[op[1]] += 1
            case "jmp":
                next_offset = offset + int(op[1])
            case "jie":
                if r[op[1]] % 2 == 0:
                    next_offset = offset + int(op[2])
            case "jio":
                if r[op[1]] == 1:
                    next_offset = offset + int(op[2])
        offset = next_offset

    return r["b"]


print(part1(0))
print(part1(1))
