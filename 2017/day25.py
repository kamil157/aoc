from parse import search


with open('2017/inputs/day25.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n\n')


def parse_entry(entry):
    value = search("Write the value {:d}", entry[0])[0]
    move = 1 if search("to the {}", entry[1])[0] == "r" else -1
    next_state = search("Continue with state {}", entry[2])[0]
    return value, move, next_state


def parse():
    states = {}
    for line in lines[1:]:
        state = search("In state {}", line)[0]
        s = line.splitlines()

        states[state] = [parse_entry(s[2:5]), parse_entry(s[6:9])]
    return states


def part1():
    state = search("state {}", lines[0])[0]
    steps = search("{:d} steps", lines[0])[0]
    states = parse()

    cursor = 0
    ones = set()

    for _ in range(steps):
        value, move, next_state = states[state][cursor in ones]
        if value:
            ones.add(cursor)
        else:
            ones.discard(cursor)
        cursor += move
        state = next_state
    return len(ones)


print(part1())
