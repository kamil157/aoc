with open('2023/inputs/day12.txt') as f:
    lines = f.read().strip().split('\n')


def generate(springs):
    result = []
    for a in springs:
        if "?" in a:
            arrangement1 = a.replace("?", "#", 1)
            arrangement2 = a.replace("?", ".", 1)
            result.append(arrangement1)
            result.append(arrangement2)
        else:
            result.append(a)
    if len(result) == len(springs):
        return result
    return generate(result)


def part1():
    total = 0
    for line in lines:
        [springs, sizes] = line.split()
        sizes = [int(n) for n in sizes.split(",")]

        for arrangement in generate([springs]):
            match_sizes = [len(s)
                           for s in arrangement.split(".") if len(s) > 0]
            if match_sizes == sizes:
                total += 1

    return total


print(part1())
