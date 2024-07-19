from collections import defaultdict
from operator import itemgetter
from parse import search


with open('2017/inputs/day20.txt', encoding="utf-8") as f:
    lines = f.readlines()


def part1():
    a = {i: sum(map(abs, search("a=<{:d},{:d},{:d}>", line)))
         for i, line in enumerate(lines)}
    return min(a.items(), key=itemgetter(1))


print(part1())


def part2():
    particles = {}
    positions = defaultdict(list)
    for i, line in enumerate(lines):
        p = search("p=<{:d},{:d},{:d}>", line)[:]
        v = search("v=<{:d},{:d},{:d}>", line)[:]
        a = search("a=<{:d},{:d},{:d}>", line)[:]
        particles[i] = (p, v, a)
        positions[p].append(i)

    while True:
        positions = defaultdict(list)
        for i, (p, v, a) in particles.items():
            px, py, pz = p
            vx, vy, vz = v
            ax, ay, az = a
            v = (vx + ax, vy + ay, vz + ay)
            vx += ax
            vy += ay
            vz += az
            px += vx
            py += vy
            pz += vz
            particles[i] = ((px, py, pz), (vx, vy, vz), (ax, ay, az))
            positions[p].append(i)

        for collisions in positions.values():
            if len(collisions) > 1:
                for i in collisions:
                    del particles[i]

        if not any(sum(map(abs, p[0])) < 1000 for p in particles.values()):
            return len(particles)


print(part2())
