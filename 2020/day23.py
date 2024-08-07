from collections import deque


def part1():
    cups = "137826495"
    cups = deque([int(c) for c in cups])
    for _ in range(100):
        current = cups.popleft()
        pickup = [cups.popleft(), cups.popleft(), cups.popleft()]
        destination = current - 1
        while destination in pickup or destination == 0:
            if destination == 0:
                destination = 9
            else:
                destination -= 1
        index = cups.index(destination) + 1
        cups.insert(index, pickup[2])
        cups.insert(index, pickup[1])
        cups.insert(index, pickup[0])
        cups.append(current)
        # print(cups, current, pickup, destination)

    while cups[0] != 1:
        cups.rotate()
    return "".join(str(n) for n in cups)[1:]


print(part1())


def part2():
    cups = [int(n) for n in "137826495"]

    a = {}
    for i in range(1, len(cups) + 1):
        a[i] = cups[(cups.index(i) + 1) % len(cups)]

    count = 1000000
    for i in range(10, count):
        a[i] = i + 1
    a[int(cups[-1])] = 10
    a[count] = int(cups[0])

    current = int(cups[0])
    for i in range(10000000):
        p1 = a[current]
        p2 = a[p1]
        p3 = a[p2]
        next = a[p3]
        pickup = [p1, p2, p3]
        destination = current - 1
        while destination in pickup or destination == 0:
            if destination == 0:
                destination = count
            else:
                destination -= 1
        a[current] = next
        a[p3] = a[destination]
        a[destination] = p1
        current = a[current]

    return a[1] * a[a[1]]


print(part2())
