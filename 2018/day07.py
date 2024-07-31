from collections import defaultdict
from parse import parse

with open('2018/inputs/day07.txt', encoding="utf-8") as f:
    lines = f.read().strip().splitlines()


def part2():
    deps = defaultdict(set)
    steps = set()
    for line in lines:
        dep, step = parse(
            "Step {} must be finished before step {} can begin.", line)
        deps[step].add(dep)
        steps.add(dep)
        steps.add(step)

    for step in steps:
        if step not in deps:
            deps[step] = set()

    q = []
    for step, d in deps.items():
        if not d:
            q.append(step)
            steps.remove(step)

    workers = [None] * 5
    t = 0
    q.sort()
    while True:
        for i, w in enumerate(workers):
            if w:
                step, left = w
                if left > 0:
                    workers[i] = step, left - 1
                else:
                    workers[i] = None
                    for other_step, d in deps.items():
                        d.discard(step)
                        if not d and other_step in steps:
                            q.append(other_step)
                            q.sort()
                            steps.remove(other_step)

        for i, w in enumerate(workers):
            if q and not w:
                step = q.pop(0)
                workers[i] = (step, 60 + ord(step) - ord("A"))

        if not (q or any(workers)):
            return t

        t += 1


print(part2())
