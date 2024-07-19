with open('2017/inputs/day21.txt', encoding="utf-8") as f:
    lines = f.read().split('\n')


def expand(s):
    return s.split("/")


def collapse(grid):
    return "/".join(grid)


def rotate(grid):
    return ["".join(l) for l in zip(*grid[::-1])]


def flip(grid):
    return [line[::-1] for line in grid]


def make_rules(grid):
    keys = []
    for _ in range(4):
        grid = rotate(grid)
        keys.append(grid)
    grid = flip(grid)
    for _ in range(4):
        grid = rotate(grid)
        keys.append(grid)
    return keys


def part1(t):
    pattern = expand(".#./..#/###")

    rules = {}
    for line in lines:
        left, right = line.split(" => ")
        for key in make_rules(expand(left)):
            rules[collapse(key)] = expand(right)

    for _ in range(t):
        if len(pattern) % 2 == 0:
            prev_size = 2
        else:
            prev_size = 3

        next_size = prev_size + 1
        size = len(pattern) * next_size // prev_size
        next_pattern = [[""] * size for _ in range(size)]
        for i in range(0, len(pattern), prev_size):
            for j in range(0, len(pattern), prev_size):
                # collect square
                square = []
                for di in range(prev_size):
                    line = ""
                    for dj in range(prev_size):
                        line += pattern[i + di][j + dj]
                    square.append(line)

                # transform square
                square = rules[collapse(square)]
                for di, row in enumerate(square):
                    for dj, tile in enumerate(row):
                        offset_i = i * next_size // prev_size
                        offset_j = j * next_size // prev_size
                        next_pattern[offset_i + di][offset_j + dj] = tile

        pattern = ["".join(line) for line in next_pattern]

    return sum(line.count("#") for line in pattern)


print(part1(5))
print(part1(18))
