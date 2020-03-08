from re import findall
from math import prod

input = open('2015/inputs/day15.txt').read()

def score(spoons, ingredients):
    def value(measure):
        v = sum(spoons[ingredient] * ingredients[ingredient][measure] for ingredient in range(len(ingredients)))
        return max(0, v)

    measures = len(ingredients[0]) - 1
    return prod(value(measure) for measure in range(measures))

def part1(s, calories_ok = lambda c: True):
    ingredients_data = findall(r'\w+: capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)', s)
    ingredients = [[int(n) for n in data] for data in ingredients_data]

    scores = []
    total_spoons = 100
    
    spoons = [0] * len(ingredients)

    for a in range(total_spoons - sum(spoons[:0]) + 1):
        spoons[0] = a
        for b in range(total_spoons - sum(spoons[:1]) + 1):
            spoons[1] = b
            for c in range(total_spoons - sum(spoons[:2]) + 1):
                spoons[2] = c
                d = total_spoons - sum(spoons[:3])
                spoons[3] = d

                calories = [spoons[i] * ingredients[i][4] for i in range(len(ingredients))]
                if calories_ok(sum(calories)):
                    scores.append(score(spoons, ingredients))                

    return max(scores)

print(part1(input))
print(part1(input, lambda c: c == 500))