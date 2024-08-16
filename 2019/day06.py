
with open('2019/inputs/day06.txt') as f:
    input = f.read()


def graph():
    edges = {}
    nodes = set()

    for edge_str in input.split():
        u, v = edge_str.split(')')
        edges[v] = u
        nodes.add(v)
        nodes.add(u)

    total_orbits = 0
    for u in nodes:
        orbits = 0
        v = u
        while v != "COM":
            v = edges[v]
            orbits += 1
        total_orbits += orbits

    def path_to_com(u):
        l = []
        v = u
        while v != "COM":
            v = edges[v]
            l.append(v)
        return l

    # all nodes on path except first common node - 1 missing
    # we don't need to count node we are orbiting - 1 extra
    # so just return len
    return total_orbits, len(set(path_to_com('YOU')) ^ set(path_to_com('SAN')))


print(graph())
