with open('2025/inputs/day03.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def solve(length):
    result = 0
    for bank in lines:
        max_joltage = bank[:length]
        for candidate in bank[length:]:
            best = max_joltage
            for to_remove in range(len(max_joltage)):
                best = max(best, max_joltage[:to_remove] + max_joltage[to_remove+1:] + candidate)
            max_joltage = max(max_joltage, best)
        result += int(max_joltage)
    return result

print(solve(2))
print(solve(12))
