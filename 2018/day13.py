from collections import Counter


with open('2018/inputs/day13.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


class Cart:
    def __init__(self, y, x, c) -> None:
        self.y = y
        self.x = x
        self.dx = 0
        self.dy = 0
        match c:
            case "v":
                self.dy = 1
            case "^":
                self.dy = -1
            case "<":
                self.dx = -1
            case ">":
                self.dx = 1
        self.t = 0
        self.crashed = False

    def move(self, tracks):
        match tracks[self.y][self.x]:
            case "+":
                match self.t:
                    case 0:
                        self.dx, self.dy = self.dy, -self.dx
                    case 2:
                        self.dx, self.dy = -self.dy, self.dx
                self.t = (self.t + 1) % 3
            case "/":
                self.dx, self.dy = -self.dy, -self.dx
            case "\\":
                self.dx, self.dy = self.dy, self.dx

        self.y += self.dy
        self.x += self.dx


def part1():
    carts = []
    tracks = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c in "<>v^":
                carts.append(Cart(y, x, c))
        tracks.append(line.replace("<", "-").replace(">",
                      "-").replace("v", "|").replace("^", "|"))

    first = True
    while len(carts) > 1:
        for cart in carts:
            cart.move(tracks)

            pos = Counter((cart.x, cart.y) for cart in carts)
            if pos.most_common(1)[0][1] > 1:
                crash = pos.most_common(1)[0][0]
                if first:
                    print(crash)
                    first = False

                carts = [c for c in carts if (c.x, c.y) != crash]

        carts.sort(key=lambda cart: (cart.y, cart.x))

    return carts[0].x, carts[0].y


print(part1())
