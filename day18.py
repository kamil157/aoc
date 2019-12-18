import collections

input = """#################################################################################
#.......#.A...........#.........#.......#.#.........#.............#...#..r......#
#.###.###.#####.#####.#.#######.#.#######.#.#.#####.#.#.#.#######.###.#.###.###.#
#...#.#...#.....#.#...#...#.....#.......#...#.#...#o#.#.#.#...#.#...#.#...#.#...#
#####.#.###.#####.#.###.#W###.#########.#####.#.#.###.#.#.#.#.#.###.#K###.#.#####
#.....#.#.#...#...#...#.#...#...........#...#...#.....#.#.#.#.#.#...#...#.#.....#
#M###.#.#.###.#.#####.#####.###########.#.#.###.#######.###.#.#.#.#####.#.#####.#
#.#...#...#...#.#...#.....#...#..z....#.#.#...#...#.....#...#.#.#.#...#.......#.#
#.###.###.#.###.#.#.#####.###.#.###.#.#.#.###.#####.#.###.###.#.#.#.#.#####.###.#
#...#...#.#.#....y#.....#.....#.#.#.#.#.#...#.#...#.#.#...#...#.#...#.#...#.#m..#
#.#.#####.#.###########.#######.#.#.#.#.###.#.#.#X#.#.#.###.###.#####.#.#.###.###
#.#.#...#.#s..#.......#.......#...#.#.#.#...#...#.#.#.#.#.#.#.......#...#...#...#
###.#.#.#.###.#.#####.###.###.#####.#.#.#.#######.#.###.#.#.#.#####.#######.###.#
#...#.#...#.#...#...#.#...#.......#.#.#.#.#.......#.....#.#.#.#.....#.....#.....#
#.###.#####.#####.#.#C#.###.#####.#.#.#.#.#####.###.#####.#.###.#####.#.#.#####.#
#.....#.....#.....#.#.#.#...#...#...#.#.#.#.F.#...#...#...#...#.#...#.#.#.....#.#
#.#######.#.###.###.#.#.#####.#.#######.#.#.#.###.###.###.###.#.#.#.#.#.#######.#
#.#.......#...#.#...#.#...#...#.#.......#...#.#.#...#.......#.#.#.#.#.#.........#
#.#.#########.#.#####.###N#.###.#.###########.#.###.#########.#.#.#.#.###########
#...#...#.......#.....#...#.#.#.#.......#...#.#...............#...#.#.#....q....#
#####.###.#######.#####.###.#.#.#######.#.#.#.#############.#####.#.#.#.#.#####.#
#g..#.....#.....#...#.#...#...#.......#.#.#.#..l..........#.#...#.#.#.#.#...#...#
###.#.#####.###.###.#T#.#.###.###.#####.###.#############.#####B#.#.#.#.###.#####
#...#.#...#...#.....#.#.#...#.#.#.#...#.#.......#.......#...#...#.#...#...#.....#
#.###.###.###.#####.#.###.###.#.#.#.#.#.#.#####.#.###.#####.#.###.#####.#######.#
#...#...#...#.#.#...#...#.I...#.#...#...#.....#.#...#.#...#...#.#...#.#.#.......#
###.###.#.###.#.#.#####.#####.#.#############.#####.#.#.#.#####.###.#.#.#.#######
#.....#.#...#.#.......#.#...#...........#.....#.....#...#.......#.#.#.#.#.......#
#.#####.###.#.#######.#.#.#.#####.#######.###.#.###########.###.#.#.#.#.#######.#
#...........#.#e....#.#...#...#...#.....#.#...#...#.........#.....#.#...#.......#
#.###########.#.###.#########.#####.###.#.#######.#.#####.#######.#.#####.#####.#
#.....#.#.....#.#.#.........#.......#...#.#.......#.#.....#.....#.#...#...#.#...#
#####.#.#.#####.#.#####.#.###########.###.#.#######.#####.#.###.#.###.#.###.#.###
#...#.#.#.......#.#.....#.#.........#.#.#...#.#.....#...#.#.#...#...#.#...#...#.#
#.###.#.#########.#.#####.#V#.#####.#.#.#.###.#.###.#.#.###.#.#######.###.#.###.#
#.#...#.....#.....#.#.....#.#...#...#.#.#.#...#.#.#.#.#.....#.........#...#.#...#
#.#.###.###.#.#####.#######.###.#.###.#.#.###.#.#.#.#.#################.###.#.#.#
#.#.....#.#.#.....#.......#.#.#.#...#.#.#.#...#.#...#.#.........#.......#.S.#.#.#
#.#######.#.#####.#######.#.#.#.#####.#.#.#.#.#.#####.#####.###.#.#######.###.#.#
#.......................#.....#.............#.#.............#.....#...........#.#
########################################@########################################
#...............#.....#.....#.............#.........................D.......#..u#
#.#############.#####.#.#.###.###.#####.#.#.#.#####.#######.###############.#.###
#.....#.....#...#...#...#.....#.#.#.....#...#....v#.#.....#.#.......#.....#.#.E.#
#####.#.#####.###.#.#.#########.#.#######.#######.###.###.###.#####.#.#####.#.#.#
#.....#.....#.....#.#.#...#.....#.......#.#.......#.....#.#...#...#.#....j#t#.#.#
#.#########.#######.#.#.#.#.###########.#.#.#######.#####.#.###.###.#####.#.#.#.#
#.......#...#...#...#...#...#.......#...#.#.#.....#.#.....#.#.....#.#...#.#.#.#.#
#######.#.#.###.#.#######.###.#####.#.#####.#.###.#.#.#####.#####.#.#.#.#.#.###.#
#.....#.#.#.....#...#.....#...#.....#...#...#.#.#...#.....#.......#...#.#.#.#...#
###.###.#.#####.###.#####.#.###.#####.#.#.#.#.#.#########.#######.#####.#.#.#.#.#
#...#...#...#...#.#.....#.#.#.#.#.....#.#.#d#.#.....#.......#.....#.....#.#...#.#
#.###.#####.#.###.#####.#.#.#.#.#######.#.###.###.#.#.#######.#####.#####.#####.#
#.....#...#.#.....#.....#.#.#.#...#.....#.....#...#.#.....#.....#...#...#.....#.#
#.#####.#.#.#.#####.#####.#.#.###.#.###.#######.#.#######.#.#####.#####.#.#.#.#.#
#.#.....#.#.#.#.....#.....#.#...#.#.#...#.......#.#.....#...#.#...#.....#.#.#.#.#
#.###.#.#.#.#.#.###########.###.#.#.#.###.#########.#.#######.#.#####.###.#.###.#
#.H.#.#.#.#.#.#.....#.....#.#...#...#...#.#.....#...#.........#.#.....#...#.....#
###.###.#.#.#.#####.#.###.#.#.#########.#.#.###.#.#######.#####.#.#.#.#.#########
#.#.#...#...#...#.#...#...#.#...#.......#...#.#...#.....#...#...#.#.#.#.........#
#.#.#.#.#######.#.#####.###.#.#.#.#######.###.#########.###.#.#####.#.#########.#
#...#.#.#...#.#.#...#...#...#.#.#...#...#...#...#.....#...#.#.#.....#.#.......#.#
#.###.###.#.#.#.###.#######.#.#.###.#.#.###.#.###.#.#.#.#.#.###.#####.###.###.#.#
#.#...#...#.#.#.#...........#.#...#.#.#.#.#.#.#...#.#...#.#.....#...#...#.#.#.#.#
#.###.#.###.#.#.#.###########.###.#.#.#.#.#.#.#.###.#####.#####.###.###.#.#.#.#.#
#...#...#.#.#.#...#...#.U...#.#.#...#.#.#...#.....#.#.....#...#...#...#...#...#.#
###.#.###.#.#.#####J#.#.#.###.#.#####.###.#######.#.#####.#.#####.#.#####.#####.#
#...#.Q.#.#.#.....#.#...#.....#.........#.......#.#f....#.L.#.....#h....#.#...#.#
#.#####.#.#.###.#.#.#################.#.#######.#.#####.###.#.#####.#.###.#.#.#.#
#.#...#...#...#.#.#.#...#.......#...#.#.#.#...G.#.....#.Z.#.#...#...#.....#.#...#
#.#.#####.###.###.#.#.#.#####.#.#.#.###.#.#.#############.#.###.#########.#.#####
#k#.#.....#.#...#.#..c#...#...#...#.#...#.#.#........n#...#...#.#.......#.#...#.#
#.#.#.#####.###.#.#######.#.#######.#.#.#.#.#.#######.#.###.###.#.#####.#####.#.#
#.#...#.....#...#.#.P...#.#.#.....#...#.#.#.#.#...#...#.#...#...#.....#.....#p..#
#.###.#.#.###.###.#.#.###.#.###.#.#####.#.#.#.#.###.###.###.#.#######.###.#####.#
#...#...#.#...#.#...#...#.#...#.#...#...#.O.#.#.....#.#...#b#.#.......#.#.#...#.#
###.#####.#.###.#.#####.#.###.#####.#.###.###.#.#####.#.#.###.#.#######.#.#.#.#.#
#.#.#.....#.#a..#.#...#.#.#...#.....#...#...#i#.#...#...#.Y.#.#.#....w..#.#.#...#
#.#R#######.#.#.#.###.#.#.#.###.#######.###.#.#.#.#.#######.#.#.#####.#.#.#.#####
#...........#.#.......#.....#...........#.....#x..#.........#.........#.#.......#
#################################################################################"""

ex1 = """#########
#b.A.@.a#
#########"""

ex2 = """########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################"""

ex3 = """########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################"""

ex4 = """#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################"""

ex5 = """########################
#@..............ac.GI.b#
###d#e#f################
###A#B#C################
###g#h#i################
########################"""


def find_reachable_keys(map, pos):
    # find shortest path to all reachable keys
    reachable_keys = set()

    q = collections.deque()
    q.append((pos, 0, set()))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * len(map[0]) for _ in range(len(map))]

    while q:
        (x, y), length, doors = q.popleft()
        current = map[y][x]
        if visited[y][x] or current == '#':
            continue

        visited[y][x] = True

        if current.islower() and pos != (x, y):
            reachable_keys.add((current, length, (x, y), frozenset(doors)))

        if current.isupper():
            doors.add(current)

        for d in directions:
            next_x, next_y = x + d[0], y + d[1]
            q.append(((next_x, next_y), length + 1, doors.copy()))
    return reachable_keys


cache = {}


def dfs(map, node, path, keys, results, paths): # do i need to remember visited?
    path += node
    if node != '@':        
        keys.add(node)

    if len(keys) == len(paths) - 1:
        # found all keys, done
        results.append(path)
    else:
        # check all unlocked paths
        for key, _, _, doors in paths[node]:
            if key in keys or any(door.lower() not in keys for door in doors):
                continue

            print('from', node, 'to', key, 'through', doors, 'have keys', keys)
            dfs(map, key, path, keys.copy(), results, paths)
    return path


def collect_keys2(s):
    """
    find shortest path from @ to all keys
    find shortest path from all keys to other keys

    for each reachable key:
        get this key first
        remember total path length
        get next keys (recurse)
    return best total path length
    """

    # print(s)

    # find all key positions
    keys = {}
    map = s.splitlines()
    for y in range(len(map)):
        for x in range(len(map[y])):
            current = map[y][x]
            if current == '@':
                start = (x, y)
            if current.islower():
                keys[current] = (x, y)

    # compute shortest paths between keys
    paths = {}
    reachable_keys = find_reachable_keys(map, start)
    paths['@'] = reachable_keys
    # for k, v in paths.items():
    #     print(k, '=>', v)
    for key, (x, y) in keys.items():
        paths[key] = find_reachable_keys(map, (x, y))
    # for k, v in paths.items():
    #     print(k, '=>', v)

    # compute stuff
    results = []
    dfs(map, '@', '', set(), results, paths)
    # print(results)

    best = 99999
    for path in results:
        length = 0
        for i in range(len(path) - 1):
            edges = paths[path[i]]
            edge = next(e for e in edges if e[0] == path[i + 1])
            length += edge[1]
            # print(edge, length)
        best = min(best, length)
    print(best)
    return best


# assert collect_keys2(ex1) == 8
assert collect_keys2(ex2) == 86
# assert collect_keys2(ex3) == 132
# assert collect_keys2(ex5) == 81
# assert collect_keys2(ex4) == 136
# print(collect_keys2(input))
