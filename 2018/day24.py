from itertools import count
import re
from parse import search

with open('2018/inputs/day24.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n\n')


class Unit():
    def __init__(self, id, count, hp, weak, immune, damage, attack_type, initiative, side) -> None:
        self.id = id
        self.count = count
        self.hp = hp
        self.weak = weak or []
        self.immune = immune or []
        self.damage = damage
        self.attack_type = attack_type
        self.initiative = initiative
        self.target = None
        self.targeted = False
        self.side = side

    def __repr__(self) -> str:
        return str(self.__dict__)

    def power(self):
        return self.count * self.damage


def parse_side(s, side, boost=0):
    units = []
    for id, line in enumerate(s.splitlines()[1:], start=1):
        count, hp = search("{:d} units each with {:d} hit points", line)
        weak = re.search(r"weak to ([a-z, ]+)", line)
        if weak:
            weak = weak[1].split(", ")
        immune = re.search(r"immune to ([a-z, ]+)", line)
        if immune:
            immune = immune[1].split(", ")
        damage, attack_type = search(
            "with an attack that does {:d} {} damage", line)
        initiative = search("at initiative {:d}", line)[0]
        units.append(Unit(id, count, hp, weak, immune,
                     damage + boost, attack_type, initiative, side))
    return units


def target(units):
    for current in [True, False]:
        order = sorted(units[current], key=lambda u: (
            u.power(), u.initiative), reverse=True)
        for unit in order:
            targets = [u for u in units[not current]
                       if not u.targeted and unit.attack_type not in u.immune]
            if targets:
                enemy = max(targets, key=lambda enemy: (unit.attack_type in enemy.weak,
                                                        enemy.power(), enemy.initiative))
                unit.target = enemy
                enemy.targeted = True


def part1(boost=0):
    units = {}
    units[True] = parse_side(lines[0], True, boost)
    units[False] = parse_side(lines[1], False)

    while True:
        stalemate = True
        target(units)

        order = sorted(units[True] + units[False],
                       key=lambda u: u.initiative, reverse=True)
        for unit in order:
            if not unit.target:
                continue

            damage = unit.power() * 2 if unit.attack_type in unit.target.weak else unit.power()
            kills = max(int(damage / unit.target.hp), 0)
            unit.target.count -= kills
            if kills:
                stalemate = False

            if unit.target.count <= 0:
                units[unit.target.side].remove(unit.target)
                if not units[unit.target.side]:
                    return unit.side, sum(u.count for u in units[unit.side])

            unit.target.targeted = False
            unit.target = None

        if stalemate:
            return False, 0


print(part1()[1])


def part2():
    for boost in count():
        result = part1(boost)
        if result[0]:
            return result[1]


print(part2())
