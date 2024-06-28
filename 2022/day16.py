from functools import cache
import re

with open('2022/inputs/day16.txt') as f:
    lines = f.read().strip().split('\n')

    graph = {}
    for line in lines:
        m = re.match(
            r"Valve ([A-Z]{2}) has flow rate=(\d+); tunnels? leads? to valves? (.*)", line)
        valve, flow, tunnels = m.groups()
        flow = int(flow)
        tunnels = tunnels.split(", ")
        graph[valve] = (flow, tunnels)


@cache
def paths(start):
    queue = [(start, 1)]
    visited = set()
    result = []
    while queue:
        node, cost = queue.pop(0)
        if node in visited:
            continue
        visited.add(node)
        if graph[node][0] != 0:
            result.append((node, graph[node][0], cost))
        for edge in graph[node][1]:
            queue.append((edge, cost + 1))
    return result


def dfs(flows, node, flow, time, open_valves):
    p = paths(node)
    for next_valve, valve_flow, time_to_open in p:
        time_left = time - time_to_open
        next_flow = flow + (valve_flow * time_left)
        if next_valve not in open_valves and time_left >= 0:
            flows.add((next_flow, tuple(open_valves + [next_valve])))
            dfs(flows, next_valve, next_flow, time_left,
                open_valves + [next_valve])


def part1():
    flows = set()
    dfs(flows, "AA", 0, 30, [])
    return max(flows)[0]


print(part1())


def part2():
    flows = set()
    dfs(flows, "AA", 0, 26, [])
    best = 0
    flows = sorted(flows, reverse=True)
    for my_flow, my_valves in flows:
        for elephant_flow, elephant_valves in flows:
            if len(set(my_valves) & set(elephant_valves)) == 0:
                best = max(best, my_flow + elephant_flow)
                if my_flow < best / 2:
                    return best


print(part2())
