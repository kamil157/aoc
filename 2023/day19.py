
import math


with open('2023/inputs/day19.txt') as f:
    s = f.read().strip().split('\n\n')


def parse_workflows(workflows):
    workflows = workflows.split('\n')
    parsed_workflows = {}
    for workflow in workflows:
        [name, rules] = workflow.split("{")
        rules = rules[:-1].split(',')
        parsed_workflows[name] = rules
    return parsed_workflows


def part1():
    [workflows, parts] = s
    parsed_workflows = parse_workflows(workflows)
    parts = parts.split('\n')

    total = 0
    for part in parts:
        ratings = {rating[0]: int(rating[2:])
                   for rating in part[1:-1].split(",")}

        current = "in"
        while current not in ["A", "R"]:
            workflow = parsed_workflows[current]

            for rule in workflow:
                if ":" in rule:
                    cond, dest = rule.split(":")
                    var, op, val = cond[0], cond[1], int(cond[2:])

                    if op == ">":
                        if ratings[var] > val:
                            current = dest
                            break
                    else:
                        if ratings[var] < val:
                            current = dest
                            break
                else:
                    current = rule

        if current == "A":
            total += sum(ratings.values())

    return total


print(part1())


def part2():
    parsed_workflows = parse_workflows(s[0])

    total = 0
    ranges = [({"x": range(1, 4001), "m": range(1, 4001),
               "a": range(1, 4001), "s": range(1, 4001)}, "in")]
    while ranges:
        r, current = ranges.pop(0)
        while current not in ["A", "R"]:
            workflow = parsed_workflows[current]

            for rule in workflow:
                if ":" in rule:
                    cond, dest = rule.split(":")
                    var, op, val = cond[0], cond[1], int(cond[2:])

                    if op == ">":
                        new_r = r.copy()
                        new_r[var] = range(val + 1, r[var][-1] + 1)
                        r[var] = range(r[var][0], val + 1)
                    else:
                        new_r = r.copy()
                        new_r[var] = range(r[var][0], val)
                        r[var] = range(val, r[var][-1] + 1)
                    ranges.append((new_r, dest))

                else:
                    current = rule

        if current == "A":
            total += math.prod(len(val) for val in r.values())
    return total


print(part2())
