from re import findall

input = open('2015/inputs/day06.txt').read()

def toggle(command, cell):
    if command == 'toggle':
        return not cell
    elif command == 'turn on':
        return True
    elif command == 'turn off':
        return False


def brightness(command, cell):
    if command == 'toggle':
        return cell + 2
    elif command == 'turn on':
        return cell + 1
    elif command == 'turn off':
        return max(0, cell - 1)


def step1(s, f):
    grid = [[0] * 1000 for _ in range(1000)]

    commands = findall(r"(toggle|turn on|turn off) (\d+),(\d+) through (\d+),(\d+)", s)
    for command, i1, j1, i2, j2 in commands:
        for i in range(int(i1), int(i2) + 1):
            for j in range(int(j1), int(j2) + 1):
                grid[i][j] = f(command, grid[i][j])

    return sum(cell for row in grid for cell in row)


print(step1(input, toggle))
print(step1(input, brightness))
