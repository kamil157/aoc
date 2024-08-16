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

    def path_to_com(u):
        l = []
        v = u
        while True:
            if v == 'COM':
                break
            v = edges[v]
            l.append(v)
        return l

    you = path_to_com('YOU')
    san = path_to_com('SAN')
    print('YOU', you)
    print('SAN', san)

    # all nodes on path except first common node - 1 missing
    # we don't need to count node we are orbiting - 1 extra
    # so just return len
    xor = set(you) ^ set(san)
    print("xor", xor)
    return len(xor)


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
K)L
K)YOU
I)SAN""") == 4

print(graph(input))
