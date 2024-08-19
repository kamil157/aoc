with open('2018/inputs/day08.txt', encoding="utf-8") as f:
    lines = f.read().split()


def parse(p):
    child_count = int(lines[p])
    metadata_count = int(lines[p + 1])
    p += 2

    part1 = 0
    part2 = 0
    children = []
    for _ in range(child_count):
        child = parse(p)
        p = child[0]
        part1 += child[1]
        children.append(child[2])

    metadata = []
    for _ in range(metadata_count):
        part1 += int(lines[p])
        metadata.append(int(lines[p]))
        p += 1

    if child_count == 0:
        part2 = part1
    else:
        for index in metadata:
            if index <= child_count:
                part2 += children[index - 1]

    return p, part1, part2


print(parse(0)[1:])
