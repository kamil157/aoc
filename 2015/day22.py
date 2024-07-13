from math import inf


with open('2015/inputs/day22.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def part1(difficulty):
    cost = {"m": 53, "d": 73, "s": 113, "p": 173, "r": 229, " ": 0}

    def fight(boss_hp, player_hp, mana, shield, poison, recharge, mana_spent, action, best):
        # difficulty
        player_hp -= difficulty
        if player_hp <= 0:
            return inf

        # player turn effects
        if poison:
            boss_hp -= 3
            poison -= 1
        if boss_hp <= 0:
            return mana_spent
        if recharge:
            mana += 101
            recharge -= 1
        if shield:
            shield -= 1

        # player spell
        mana -= cost[action]
        mana_spent += cost[action]

        if action == "m":
            boss_hp -= 4
        if action == "d":
            boss_hp -= 2
            player_hp += 2
        if boss_hp <= 0:
            return mana_spent
        if action == "s":
            shield = 6
        if action == "p":
            poison = 6
        if action == "r":
            recharge = 5

        # boss turn effects
        if poison:
            boss_hp -= 3
            poison -= 1
        if boss_hp <= 0:
            return mana_spent
        if recharge:
            mana += 101
            recharge -= 1
        player_armor = 0
        if shield:
            player_armor = 7
            shield -= 1

        # boss attack
        player_hp -= max(1, boss_damage - player_armor)
        if player_hp <= 0:
            return inf

        # next actions
        actions = "md"
        if shield <= 1:
            actions += "s"
        if poison <= 1:
            actions += "p"
        if recharge <= 1:
            actions += "r"

        # check remaining mana
        actions = [a for a in actions if mana >= cost[a]]
        if not actions:
            return inf

        # next step
        for action in actions:
            if mana_spent + cost[action] < best:
                best = min(best, fight(boss_hp, player_hp, mana,
                           shield, poison, recharge, mana_spent, action, best))
        return best

    boss_hp, boss_damage = int(lines[0][12:]), int(lines[1][8:])
    return min(fight(boss_hp, 50, 500, 0, 0, 0, 0, action, inf) for action in "mdspr")


print(part1(0))
print(part1(1))
