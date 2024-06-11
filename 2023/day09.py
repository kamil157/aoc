

with open('2023/inputs/day09.txt') as f:
    lines = f.read().strip().split('\n')


def part1(s):
    total = 0
    total2 = 0
    for line in lines:
        history = [int(n) for n in line.split()]

        extrapolated = 0
        back = history[0]
        sign = -1

        while any(n != 0 for n in history):
            next = []
            for a, b in zip(history, history[1:]):
                next.append(b - a)

            extrapolated += history[-1]
            history = next
            back += sign * history[0]
            sign *= -1

        total += extrapolated
        total2 += back

    return total, total2


print(part1(lines))
