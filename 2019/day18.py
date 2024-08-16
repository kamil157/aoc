import collections

with open('2019/inputs/day18_1.txt', encoding="utf-8") as f:
    input = f.read()


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


class MazeSolver:
    def __init__(self, s):
        self.cache = {}
        self.s = s
        self.paths = {}
        self.map = None
        self.results = {}

    def find_reachable_keys(self, pos):
        # find shortest path to all reachable keys
        reachable_keys = {}

        q = collections.deque()
        q.append((pos, 0, ""))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False] * len(self.map[0]) for _ in range(len(self.map))]

        while q:
            (x, y), length, doors = q.popleft()
            current = self.map[y][x]
            if visited[y][x] or current == '#':
                continue

            visited[y][x] = True

            if current.islower() and pos != (x, y):
                reachable_keys[current] = (length, (x, y), doors)

            if current.isupper():
                doors += current

            for d in directions:
                next_x, next_y = x + d[0], y + d[1]
                q.append(((next_x, next_y), length + 1, doors))
        return reachable_keys

    def dfs(self, node, path, length):
        # check cache
        if path:
            prev = path[-1]
            try:
                cached_path, cached_length = self.cache[(
                    ''.join(sorted(path)), prev, node)]
                self.results[path + cached_path] = cached_length + length
                return (cached_path, cached_length)
            except KeyError:
                pass

        # update state
        current_length = 0
        if path:
            current_length = self.paths[prev][node][0]
            length += current_length
        path += node

        subtrees = []
        if len(path) == len(self.paths):
            # found all keys, done
            self.results[path] = length
            return node, current_length
        else:
            # check all unlocked paths to other keys
            for key, (_, _, doors) in self.paths[node].items():
                if key in path or any(door.lower() not in path for door in doors):
                    continue

                subtree_path, subtree_length = self.dfs(key, path, length)
                subtrees.append(
                    (node + subtree_path, subtree_length + current_length))

        best_path, best_length = min(subtrees, key=lambda s: s[1])
        if len(path) > 1:
            cache_key = (''.join(sorted(path[:-1])), path[-2], node)
            self.cache[cache_key] = (best_path, best_length)
        return best_path, best_length

    def solve(self):
        """
        find shortest path from @ to all keys
        find shortest path from all keys to other keys

        for each reachable key:
            get this key first
            remember total path length
            get next keys (recurse)
        return best total path length
        """
        # find all key positions
        keys = {}
        self.map = self.s.splitlines()
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                current = self.map[y][x]
                if current == '@':
                    start = (x, y)
                if current.islower():
                    keys[current] = (x, y)

        # compute shortest paths between keys
        reachable_keys = self.find_reachable_keys(start)
        self.paths['@'] = reachable_keys
        for key, (x, y) in keys.items():
            self.paths[key] = self.find_reachable_keys((x, y))

        # compute stuff
        self.dfs(node='@', path='', length=0)
        return min(self.results.values())


assert MazeSolver(ex1).solve() == 8
assert MazeSolver(ex2).solve() == 86
assert MazeSolver(ex3).solve() == 132
assert MazeSolver(ex5).solve() == 81
assert MazeSolver(ex4).solve() == 136
print(MazeSolver(input).solve())  # 5402
