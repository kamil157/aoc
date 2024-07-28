from collections import deque
from itertools import count
from math import lcm


with open('2023/inputs/day20.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def solve():
    outputs = {}
    flip = {}
    conjunction = {}

    for line in lines:
        left, right = line.split(" -> ")
        dest = right.split(", ")
        if left == "broadcaster":
            outputs[left] = dest
        else:
            module, name = left[0], left[1:]
            if module == "%":
                outputs[name] = dest
                flip[name] = False
            else:
                outputs[name] = dest
                conjunction[name] = {}
                if "rx" in dest:
                    part2 = name

    for line in lines:
        left, right = line.split(" -> ")
        name = left[1:]
        dest = right.split(", ")
        for d in dest:
            if d in conjunction:
                conjunction[d][name] = False

    def send(name, value):
        for d in outputs[name]:
            q.append((name, d, value))

    part1 = {False: 0, True: 0}
    lowest = {}
    for i in count():
        if i == 1000:
            print(part1[True] * part1[False])
        q = deque([("button", "broadcaster", False)])
        while q:
            source, name, signal = q.popleft()
            part1[signal] += 1

            if name == part2 and signal:
                if source not in lowest:
                    lowest[source] = i + 1

                    if lowest.keys() == conjunction[part2].keys():
                        return lcm(*lowest.values())

            if name == "broadcaster":
                send(name, False)

            if name in flip and not signal:
                flip[name] = not flip[name]
                send(name, flip[name])

            if name in conjunction:
                conjunction[name][source] = signal
                send(name, not all(conjunction[name].values()))

    return part1[True] * part1[False]


print(solve())
