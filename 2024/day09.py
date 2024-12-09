with open('2024/inputs/day09.txt', encoding="utf-8") as f:
    lines = f.read()


def checksum(disk_map):
    result = 0
    for i, n in enumerate(disk_map):
        if n != ".":
            result += n * (i)
    return result


def part1():
    disk_map = []
    filled = True
    id = 0
    for c in lines:
        c = int(c)
        if filled:
            disk_map.extend([id] * c)
            id += 1
        else:
            disk_map.extend('.' * c)
        filled = not filled

    left = 0
    right = len(disk_map) - 1
    while left < right:
        while disk_map[left] != ".":
            left += 1
        while disk_map[right] == ".":
            right -= 1
        if left < right:
            disk_map[left] = disk_map[right]
            disk_map[right] = "."

        left += 1
        right -= 1

    return checksum(disk_map)


print(part1())


def part2():
    disk_map = []
    filled = True
    id = 0
    for c in lines:
        c = int(c)
        if filled:
            disk_map.append((id, c))
            id += 1
        else:
            disk_map.append(('.', c))
        filled = not filled

    current = id - 1

    while current > 0:
        found = False
        for i, (id, count_file) in enumerate(disk_map):
            if id == current:
                right = i
                break

        for i, (id, count_space) in enumerate(disk_map):
            if id == "." and count_space >= count_file:
                left = i
                found = True
                break

        if found and left < right:
            disk_map[right] = (".", count_file)
            disk_map = disk_map[:left] + [(current, count_file)] + \
                [(".", count_space - count_file)] + disk_map[left + 1:]

        current -= 1

    merged = []
    for id, count in disk_map:
        if id == ".":
            merged.extend("." * count)
        else:
            merged.extend([id] * count)

    return checksum(merged)


print(part2())
