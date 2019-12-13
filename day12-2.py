from math import gcd

input = """<x=-10, y=-13, z=7>
<x=1, y=2, z=1>
<x=-15, y=-3, z=13>
<x=3, y=7, z=-4>"""


def prod(l):
    return


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def nbody(s):
    num_moons = 4
    num_dimensions = 3

    steps = []
    for d in range(num_dimensions):
        positions = []
        velocities = []
        history = set()

        for line in s.split("\n"):
            x, y, z = line.split(',')
            positions.append([int(x[3:]), int(y[3:]), int(z[3:-1])])
            velocities.append([0, 0, 0])

        # print("After 0 steps:", positions, velocities)
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

            # print("After", step + 1, "steps:", positions, velocities)

            state = (tuple(tuple(moon) for moon in positions), tuple(tuple(moon) for moon in velocities))
            if state in history:
                # print(step)
                steps.append(step)
                break
            history.add(state)
            step += 1

    return lcm(lcm(steps[0], steps[1]), steps[2])


assert nbody("""<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>""") == 2772

assert nbody("""<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>""") == 4686774924

print(nbody(input))
