from operator import and_, lshift, or_, rshift

with open('2015/inputs/day07.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def part1(values):
    def value(s):
        op = s.split(" ")
        if len(op) == 1:
            return values[s] if s in values else int(s)
        if len(op) == 2 and op[0] == "NOT":
            values[right] = value(op[1]) ^ 0xFFFF
        if len(op) == 3:
            for name, fn in operators.items():
                if op[1] == name:
                    values[right] = fn(value(op[0]), value(op[2]))
        raise ValueError

    operators = {"AND": and_, "OR": or_, "LSHIFT": lshift, "RSHIFT": rshift}

    while "a" not in values:
        for line in lines:
            left, right = line.split(" -> ")
            if right not in values:
                try:
                    values[right] = value(left)
                except ValueError:
                    continue

    return values["a"]


result = part1({})
print(result)
print(part1({"b": result}))
