with open('2023/inputs/day11.txt') as f:
    lines = f.read().strip().split('\n')


def part2(age):
    space_map = []
    i = 1
    for y, row in enumerate(lines):
        for x, val in enumerate(row):
            if val == "#":
                space_map.append((y, x))
                i += 1

    def is_space(line): return all(c == "." for c in line)
    empty_rows = [i for i, line in enumerate(lines) if is_space(line)]
    empty_cols = [i for i, line in enumerate(
        list(zip(*lines))) if is_space(line)]
    empty = [empty_rows, empty_cols]

    total_dist = 0
    for i, galaxy in enumerate(space_map):
        for other in space_map[i:]:
            total_dist += abs(galaxy[0] - other[0]) + abs(galaxy[1] - other[1])
            for dim in [0, 1]:
                for space_index in empty[dim]:
                    low = min(galaxy[dim], other[dim])
                    high = max(galaxy[dim], other[dim])
                    if low < space_index < high:
                        total_dist += age - 1

    return total_dist


print(part2(2))
print(part2(1000000))
