with open('2022/inputs/day21.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def part1():
    monkeys = {}

    while len(monkeys) < len(lines):
        for line in lines:

            key, value = line.split(": ")

            if key in monkeys:
                continue

            if value.isdigit():
                monkeys[key] = int(value)
            else:
                a, op, b = value.split()
                if a in monkeys and b in monkeys:
                    monkeys[key] = eval(f"monkeys['{a}'] {op} monkeys['{b}']")

    return int(monkeys["root"])


print(part1())


def part2():
    l = -10**15
    r = 10**15
    while l < r:
        humn = (l + r) // 2
        monkeys = {}
        while len(monkeys) < len(lines):
            for line in lines:
                key, value = line.split(": ")

                if key in monkeys:
                    continue

                if value.isdigit():
                    if key == "humn":
                        monkeys[key] = humn
                    else:
                        monkeys[key] = int(value)
                else:
                    a, op, b = value.split()
                    if a in monkeys and b in monkeys:
                        if key == "root":
                            if monkeys[a] > monkeys[b]:
                                l = humn
                            elif monkeys[a] < monkeys[b]:
                                r = humn
                            else:
                                return humn

                        monkeys[key] = eval(
                            f"monkeys['{a}'] {op} monkeys['{b}']")


print(part2())
