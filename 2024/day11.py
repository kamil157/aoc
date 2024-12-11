from collections import Counter

with open('2024/inputs/day11.txt', encoding="utf-8") as f:
    lines = f.read()


def change(stone):
    if stone == 0:
        return [1]
    digits = str(stone)
    if len(digits) % 2 == 0:
        mid = len(digits) // 2
        return [int(digits[:mid]), int(digits[mid:])]
    return [stone * 2024]


def solve(blinks):
    stones = Counter(int(n) for n in lines.split())
    for _ in range(blinks):
        new_stones = Counter()
        for stone, count in stones.items():
            for result in change(stone):
                new_stones[result] += count

        stones = new_stones

    return sum(stones.values())


print(solve(25))
print(solve(75))
