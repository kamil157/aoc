
from collections import Counter


with open('2021/inputs/day06.txt', encoding="utf-8") as f:
    lines = f.read().split('\n')


def part1(days):
    values = [int(n) for n in lines[0].split(",")]
    fish = Counter(values)

    for _ in range(days):
        new_fish = {}

        for i in range(8):
            new_fish[i] = fish.get(i + 1, 0)
            if i == 6:
                new_fish[i] += fish.get(0, 0)
        new_fish[8] = fish.get(0, 0)

        fish = new_fish
    return sum(fish.values())


print(part1(80))
print(part1(256))
