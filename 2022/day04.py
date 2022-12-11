with open('2022/inputs/day04.txt') as f:
    lines = f.read().strip().split('\n')


def overlap1(start1, start2, end1, end2):
    return (start1 >= start2 and end1 <= end2) or (start2 >= start1 and end2 <= end1)


def overlap2(start1, start2, end1, end2):
    return (start2 <= end1 and end2 >= start1) or (start1 <= end2 and end1 >= start2)


def part1(overlap):
    count = 0
    for line in lines:
        e1, e2 = line.split(',')
        start1, end1 = e1.split('-')
        start2, end2 = e2.split('-')
        start1, start2, end1, end2 = int(start1), int(start2), int(end1), int(end2)
        if overlap(start1, start2, end1, end2):
            count += 1
    return count


print(part1(overlap1))
print(part1(overlap2))
