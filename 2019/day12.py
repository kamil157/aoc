with open('2019/inputs/day12.txt') as f:
    input = f.read()


def nbody(s, num_steps):
    positions = []
    velocities = []

    for line in s.split("\n"):
        x, y, z = line.split(',')
        positions.append([int(x[3:]), int(y[3:]), int(z[3:-1])])
        velocities.append([0, 0, 0])
    # print("After 0 steps:", positions, velocities)
    count = len(positions)

    for step in range(num_steps):
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

        # print("After", step + 1, "steps:", positions, velocities)

    energy = 0
    for i in range(count):
        pot = sum(abs(n) for n in positions[i])
        kin = sum(abs(n) for n in velocities[i])
        energy += pot * kin

    return energy


assert nbody("""<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>""", 10) == 179

assert nbody("""<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>""", 100) == 1940

print(nbody(input, 1000))
