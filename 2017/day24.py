with open('2017/inputs/day24.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def part1():
    results = []

    def helper(bridge, port, strength):
        results.append((len(bridge), strength))

        for line in lines:
            ports = line.split("/")
            if port in ports and line not in bridge:
                component_strength = sum(int(n) for n in ports)
                ports.remove(port)
                helper(bridge + [line], ports[0],
                       strength + component_strength)

    helper([], "0", 0)
    strongest = max(strength for _, strength in results)
    longest = max(results)[1]
    return strongest, longest


print(part1())
