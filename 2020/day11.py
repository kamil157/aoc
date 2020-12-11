from copy import deepcopy

input = open('2020/inputs/day11.txt').readlines()

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def in_range(i, j, seats):
    return 0 <= i < len(seats) and 0 <= j < len(seats[0])

def neighbors1(seats, i, j):
    count = 0
    for di, dj in directions:
        if in_range(i + di, j + dj, seats) and seats[i + di][j + dj] == '#':
            count += 1
    return count

def neighbors2(seats, i, j):
    count = 0
    for di, dj in directions:
        distance = 1
        while in_range(i + distance * di, j + distance * dj, seats):
            neighbor = seats[i + distance * di][j + distance * dj]
            if neighbor == '#':
                count += 1
                break
            elif neighbor == 'L':
                break
            elif neighbor == '.':
                distance += 1
    return count

def tick(seats, tolerance, neighbors):
    result = deepcopy(seats)
    for i, line in enumerate(seats):
        for j, seat in enumerate(line):
            if seat == 'L' and neighbors(seats, i, j) == 0:
                result[i][j] = '#'
            elif seat == '#' and neighbors(seats, i, j) >= tolerance:
                result[i][j] = 'L'
    return result

def state(seats):
    return ''.join(''.join(line) for line in seats)

def part1(s, tolerance, neighbors):
    seats = [list(line.strip()) for line in s]
    
    visited = set()
    while True:
        if state(seats) in visited:
            return state(seats).count('#')
            
        visited.add(state(seats))
        seats = tick(seats, tolerance, neighbors)

print(part1(input, 4, neighbors1))
print(part1(input, 5, neighbors2))
