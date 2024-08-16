from math import lcm
with open('2019/inputs/day12.txt') as f:
    input = f.read()


def parse():
    positions = []
    velocities = []

    for line in input.split("\n"):
        x, y, z = line.split(',')
        positions.append([int(x[3:]), int(y[3:]), int(z[3:-1])])
        velocities.append([0, 0, 0])

    return positions, velocities


def part1():
    positions, velocities = parse()
    count = len(positions)

    for _ in range(1000):
        # velocity += gravity
        for i in range(count):
            for j in range(i, count):
                for d in range(3):  # dimension
                    if positions[i][d] < positions[j][d]:
                        velocities[i][d] += 1
                        velocities[j][d] -= 1
                    if positions[i][d] > positions[j][d]:
                        velocities[i][d] -= 1
                        velocities[j][d] += 1

        # position += velocity
        for i in range(count):
            for d in range(3):
                positions[i][d] += velocities[i][d]

    energy = 0
    for i in range(count):
        pot = sum(abs(n) for n in positions[i])
        kin = sum(abs(n) for n in velocities[i])
        energy += pot * kin

    return energy


print(part1())


def part2():
    num_moons = 4
    positions, velocities = parse()

    steps = []
    for d in range(3):
        history = set()

        step = 0
        while True:
            # velocity += gravity
            for i in range(num_moons):
                for j in range(i, num_moons):
                    if positions[i][d] < positions[j][d]:
                        velocities[i][d] += 1
                        velocities[j][d] -= 1
                    if positions[i][d] > positions[j][d]:
                        velocities[i][d] -= 1
                        velocities[j][d] += 1

            # position += velocity
            for i in range(num_moons):
                positions[i][d] += velocities[i][d]

            state = (tuple(tuple(moon) for moon in positions),
                     tuple(tuple(moon) for moon in velocities))
            if state in history:
                steps.append(step)
                break
            history.add(state)
            step += 1

    return lcm(steps[0], steps[1], steps[2])


print(part2())
