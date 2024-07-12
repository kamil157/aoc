with open('2018/inputs/day12.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def part2(n):
    state = {}
    rules = {}
    for line in lines:
        if "initial state" in line:
            for i, c in enumerate(line[15:]):
                state[i] = c
        elif "=>" in line:
            rules[line[:5]] = line[9]

    values = {}
    for t in range(1, 110):
        new_state = {}
        for i in range(min(state.keys()) - 2, max(state.keys()) + 3):
            window = "".join(state.get(i + j, ".") for j in range(-2, 3))
            new_state[i] = rules.get(window, ".")
        state = new_state

        total = sum(i for i, pot in state.items() if pot == "#")
        values[t] = total
        if n == t:
            return total
    return values[t] + (values[t] - values[t - 1]) * (n - t)


print(part2(20))
print(part2(50000000000))
