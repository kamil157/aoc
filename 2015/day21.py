from itertools import combinations, product


with open('2015/inputs/day21.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')

weapons = r"""
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0
"""

armors = r"""
Armor:      Cost  Damage  Armor
None          0     0       0
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5
"""

rings = r"""
Rings:      Cost  Damage  Armor
None          0     0       0
None          0     0       0
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
"""


def parse(shop):
    return [[int(n) for n in line.split()[-3:]] for line in shop.split('\n')[2:-1]]


def part1():
    def fight(boss_hp, player_hp):
        while boss_hp > 0 and player_hp > 0:
            boss_hp -= max(1, player_damage - boss_armor)
            if boss_hp <= 0:
                return True
            player_hp -= max(1, boss_damage - player_armor)
            if player_hp <= 0:
                return False

    cheapest = 500
    most_expensive = 0

    for w, a, (r1, r2) in product(parse(weapons), parse(armors), combinations(parse(rings), 2)):
        items = [w, a, r1, r2]
        cost = sum(stats[0] for stats in items)
        player_damage = sum(stats[1] for stats in items)
        player_armor = sum(stats[2] for stats in items)
        player_hp = 100

        boss_hp, boss_damage, boss_armor = int(
            lines[0][12:]), int(lines[1][8:]), int(lines[2][7:])

        if fight(boss_hp, player_hp):
            cheapest = min(cost, cheapest)
        else:
            most_expensive = max(cost, most_expensive)

    return cheapest, most_expensive


print(part1())
