with open('2022/inputs/day20.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def part1_(mul=1, iterations=1):
    init = [(i, int(n) * mul) for i, n in enumerate(lines)]

    l = init[:]
    for _ in range(iterations):
        for i, n in init:
            old_index = l.index((i, n))
            l.pop(old_index)
            new_index = (old_index + n) % len(l)
            l.insert(new_index, (i, n))
    l = [n for _, n in l]

    def groove(n):
        return l[(l.index(0) + n) % len(l)]

    return groove(1000) + groove(2000) + groove(3000)


print(part1_())
print(part1_(811589153, 10))
