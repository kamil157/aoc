with open('2019/inputs/day03.txt') as f:
    input1, input2 = f.read().splitlines()


def path(s):
    ret = set()
    steps_for_cell = {}
    path_str = s.split(',')
    directions = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    # print(path_str)

    x = y = steps = 0
    for step in path_str:
        direction, dist = step[0], int(step[1:])
        # print()
        # print(direction, dist)

        for i in range(dist):
            x += directions[direction][0]
            y += directions[direction][1]
            steps += 1
            if (x, y) not in ret:
                ret.add((x, y))
                steps_for_cell[(x, y)] = steps
            # print(x, y, steps_for_cell[(x, y)])

    return ret, steps_for_cell


def manhattan(p):
    # distance from (0, 0)
    return abs(p[0]) + abs(p[1])


def distance(s1, s2):
    path1 = path(s1)[0]
    path2 = path(s2)[0]
    intersections = path1.intersection(path2)
    # print(intersections)

    return manhattan(min(intersections, key=manhattan))


assert distance("R8,U5,L5,D3", "U7,R6,D4,L4") == 6
assert distance("R75,D30,R83,U83,L12,D49,R71,U7,L72",
                "U62,R66,U55,R34,D71,R55,D58,R83") == 159
assert distance("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
                "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7") == 135

print(distance(input1, input2))


def steps(s1, s2):
    path1, steps1 = path(s1)
    path2, steps2 = path(s2)
    intersections = path1.intersection(path2)
    # print(intersections)

    def steps_to_point(p):
        return steps1[p] + steps2[p]

    return steps_to_point(min(intersections, key=steps_to_point))


assert steps("R8,U5,L5,D3", "U7,R6,D4,L4") == 30
assert steps("R75,D30,R83,U83,L12,D49,R71,U7,L72",
             "U62,R66,U55,R34,D71,R55,D58,R83") == 610
assert steps("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
             "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7") == 410

print(steps(input1, input2))
