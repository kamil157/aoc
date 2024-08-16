
with open('2019/inputs/day06.txt') as f:
    input = f.read()


def graph(s):
    edges = {}
    nodes = set()

    edges_str = s.split()
    print(edges_str)
    for edge_str in edges_str:
        u, v = edge_str.split(')')
        print(edge_str, u, v)
        edges[v] = u
        nodes.add(v)
        nodes.add(u)

    print(edges)
    print(nodes)

    total_orbits = 0
    for u in nodes:
        orbits = 0
        v = u
        while True:
            if v == 'COM':
                break
            v = edges[v]
            orbits += 1
        print(u, orbits)
        total_orbits += orbits
    return total_orbits


assert graph("""COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L""") == 42

print(graph(input))
