import heapq
from math import inf


energy = {"A": 1, "B": 10, "C": 100, "D": 1000}
room_to_x = [2, 4, 6, 8]
hall_to_x = [0, 1, 3, 5, 7, 9, 10]


def is_path_clear(state, room_idx, hall_idx):
    room_x = room_to_x[room_idx]
    hall_x = hall_to_x[hall_idx]
    x1, x2 = min(room_x, hall_x), max(room_x, hall_x)

    for i, cur in enumerate(state[0]):
        if x1 < hall_to_x[i] < x2 and cur != ".":
            return False
    return True


def move_cost(room, amphipod, amphipod_idx, room_idx, hall_idx):
    y = len(room) - amphipod_idx
    x = abs(room_to_x[room_idx] - hall_to_x[hall_idx])
    return (x + y) * energy[amphipod]


def room_to_hall(state, room_idx, hall_idx):
    hall, rooms = state
    room = rooms[room_idx]
    if room == "." * len(room) or hall[hall_idx] != "." or not is_path_clear(state, room_idx, hall_idx):
        return

    amphipod_idx = room.index(".") - 1 if "." in room else len(room) - 1
    amphipod = room[amphipod_idx]

    room = room[:amphipod_idx] + "." + room[amphipod_idx + 1:]
    hall = hall[:hall_idx] + amphipod + hall[hall_idx + 1:]
    rooms = rooms[:room_idx] + (room,) + rooms[room_idx + 1:]

    return (hall, rooms), move_cost(room, amphipod, amphipod_idx, room_idx, hall_idx)


def hall_to_room(state, hall_idx, room_idx):
    hall, rooms = state
    room = rooms[room_idx]
    if "." not in room or hall[hall_idx] == "." or not is_path_clear(state, room_idx, hall_idx):
        return

    amphipod_idx = room.index(".")
    amphipod = hall[hall_idx]

    correct_room_idx = ord(amphipod) - ord("A")
    if room_idx != correct_room_idx or any(a not in [amphipod, "."] for a in room):
        return

    room = room[:amphipod_idx] + amphipod + room[amphipod_idx + 1:]
    hall = hall[:hall_idx] + "." + hall[hall_idx + 1:]
    rooms = rooms[:room_idx] + (room,) + rooms[room_idx + 1:]

    return (hall, rooms), move_cost(room, amphipod, amphipod_idx, room_idx, hall_idx)


def dijkstra(start, end):
    h = []
    dist = {start: 0}
    heapq.heappush(h, (0, start))

    while h:
        cost, state = heapq.heappop(h)
        if state == end:
            return cost

        hall, rooms = state
        for room_idx in range(len(rooms)):
            for hall_idx in range(len(hall)):
                for res in [room_to_hall(state, room_idx, hall_idx), hall_to_room(state, hall_idx, room_idx)]:
                    if res:
                        new_state, cost = res
                        alt = dist[state] + cost
                        if alt < dist.get(new_state, inf):
                            dist[new_state] = alt
                            heapq.heappush(h, (alt, new_state))


def solve(part2):
    with open('2021/inputs/day23.txt', encoding="utf-8") as f:
        lines = f.read().splitlines()
    if part2:
        lines = lines[:3] + ["  #D#C#B#A#", "  #D#B#A#C#"] + lines[3:]

    rooms = [[] for _ in range(4)]
    for line in lines:
        if line[3] in "ABCD":
            for i, room in enumerate(rooms):
                room.append(line[2 * i + 3])
    rooms = tuple("".join(room[::-1]) for room in rooms)

    if part2:
        end = ("." * 7, ("AAAA", "BBBB", "CCCC", "DDDD"))
    else:
        end = ("." * 7, ("AA", "BB", "CC", "DD"))

    return dijkstra(("." * 7, rooms), end)


print(solve(False))
print(solve(True))
