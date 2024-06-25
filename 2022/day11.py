
import math


with open('2022/inputs/day11.txt') as f:
    lines = f.read().strip().split('\n\n')


def part1(decrease, rounds):
    monkeys = []
    for monkey in lines:
        split = monkey.split('\n')
        items = list(map(int, split[1].split(":")[1].split(",")))
        op = eval("lambda old: " + split[2].split(":")[1].split("=")[1])
        test = int(split[3].split()[3])
        ifTrue = int(split[4].split()[5])
        ifFalse = int(split[5].split()[5])
        parsed = {"items": items, "op": op, "test": test,
                  "ifTrue": ifTrue, "ifFalse": ifFalse, "inspections": 0}
        monkeys.append(parsed)

    modulus = math.lcm(*(monkey["test"] for monkey in monkeys))
    for _ in range(rounds):
        for monkey in monkeys:
            for item in monkey["items"]:
                worry = monkey["op"](item)
                if decrease:
                    worry //= 3
                else:
                    worry = worry % modulus
                if worry % monkey["test"] == 0:
                    target = monkey["ifTrue"]
                else:
                    target = monkey["ifFalse"]
                monkeys[target]["items"].append(worry)
            monkey["inspections"] += len(monkey["items"])
            monkey["items"].clear()

    inspections = [monkey["inspections"] for monkey in monkeys]
    inspections = sorted(inspections, reverse=True)

    return inspections[0] * inspections[1]


print(part1(True, 20))
print(part1(False, 10000))
