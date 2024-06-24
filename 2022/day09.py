
with open('2022/inputs/day09.txt') as f:
    lines = f.read().strip().split('\n')


def part1(length):
    dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    tail_positions = set()
    rope = [(0, 0)] * length
    for line in lines:
        dir = line[0]
        dist = int(line[2:])

        for _ in range(dist):
            next_rope = []
            for i, (y, x) in enumerate(rope):
                if i == 0:  # head
                    dy, dx = dirs[dir]
                else:
                    ny, nx = next_rope[-1]
                    dy, dx = 0, 0
                    if abs(y - ny) > 1 or abs(x - nx) > 1:
                        if y == ny:  # move x
                            dx = 1 if (nx > x) else -1
                        elif x == nx:  # move y
                            dy = 1 if (ny > y) else -1
                        else:  # diagonal
                            dy = 1 if (ny > y) else -1
                            dx = 1 if (nx > x) else -1

                next_rope.append((y + dy, x + dx))

            rope = next_rope
            tail_positions.add(rope[-1])

    return len(tail_positions)


print(part1(2))
print(part1(10))
