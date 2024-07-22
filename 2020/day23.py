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
