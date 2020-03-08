from re import findall

input = open('2015/inputs/day14.txt').read()

def part2(s, time):
    reindeer_data = findall(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.', s)

    reindeer = {}
    for name, speed, flight, rest in reindeer_data:
        reindeer[name] = (int(speed), int(flight), int(rest))
    
    distances = { name: 0 for name in reindeer.keys() }
    points = { name: 0 for name in reindeer.keys() }
    for t in range(time):
        for name, (speed, flight, rest) in reindeer.items():
            if t % (flight + rest) < flight:
                distances[name] += speed
        
        lead = max(distances.values())
        for name in reindeer.keys():
            points[name] += 1 if distances[name] == lead else 0

    return max(distances.values()), max(points.values())

print(part2(input, 2503)[0])
print(part2(input, 2503)[1])