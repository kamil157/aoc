from functools import reduce

with open('2023/inputs/day15.txt') as f:
    s = f.read().strip().split(',')


def hash(s):
    return reduce(lambda h, c: 17 * (h + ord(c)) % 256, s, 0)


def part1():
    return sum(map(hash, s))


print(part1())


def part2():
    boxes = [{} for _ in range(256)]
    for step in s:
        if '-' in step:
            label = step[:-1]

            boxes[hash(label)].pop(label, 0)
        else:
            label = step[:-2]
            lens = int(step[-1])

            boxes[hash(label)][label] = lens

    return sum(i * j * lens
               for i, box in enumerate(boxes, start=1)
               for j, lens in enumerate(box.values(), start=1))


print(part2())
