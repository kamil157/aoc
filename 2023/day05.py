from parse import findall


with open('2023/inputs/day05.txt', encoding="utf-8") as f:
    lines = f.read().strip()


def parse():
    maps = lines.split('\n\n')
    seeds = [r[0] for r in findall("{:d}", maps[0])]
    return maps, seeds


def seed_to_location(maps, value):
    for m in maps:
        for rng in m.splitlines()[1:]:
            dst, src, length = map(int, rng.split())
            if src <= value < src + length:
                value = value + dst - src
                break
    return value


def part1():
    maps, seeds = parse()
    return min(seed_to_location(maps[1:], int(seed)) for seed in seeds)


print(part1())


def seed_to_location_range(maps, seed_start, seed_end):
    if not maps:
        return seed_start

    for map_range in maps[0].splitlines()[1:]:
        dst, src, m_length = map(int, map_range.split())
        map_start = src
        map_end = src + m_length

        start = max(map_start, seed_start)
        end = min(map_end, seed_end)
        if start < end:
            return min(
                seed_to_location_range(maps, seed_start, map_start),
                seed_to_location_range(
                    maps[1:], start + dst - src, end + dst - src),
                seed_to_location_range(maps, map_end, seed_end)
            )

    return seed_to_location_range(maps[1:], seed_start, seed_end)


def part2():
    maps, seeds = parse()
    return min(seed_to_location_range(maps[1:], seeds[i], seeds[i] + seeds[i + 1])
               for i in range(0, len(seeds), 2))


print(part2())
