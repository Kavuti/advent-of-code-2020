import re

def get_input():
    with open("input.txt", "r") as file:
        return file.read()


def quiz1(data):
    memory = {}
    friends = {}
    appearance = {}
    for dish in data:
        ingredients = re.search(r"([a-z ]+) \(", dish).groups(1)[0].split(' ')
        allergenes = re.search(r"\(contains (.+)\)", dish).groups(1)[0].split(', ')
        for ingredient in ingredients:
            if not ingredient in appearance:
                appearance[ingredient] = 0
            appearance[ingredient] += 1
            if not ingredient in friends:
                friends[ingredient] = set()
            [friends[ingredient].add(i) for i in ingredients]
            if not ingredient in memory:
                memory[ingredient] = []
            distinct_ingredients = set(memory[ingredient])
            for allergene in allergenes:
                if not allergene in distinct_ingredients and len(distinct_ingredients) > 0:
                    for i in friends[ingredient]:
                        if i in memory and not allergene in memory[i]:
                            memory[i].append(allergene)
                else:
                    memory[ingredient].append(allergene)

    allergene_ranking = {}
    allergene_responsible = {}
    without_allergenes = []
    for ingredient, allergenes in memory.items():
        count_allergenes = {n: allergenes.count(n) for n in allergenes if allergenes.count(n) > 1}
        max_allerg_value = 0
        max_allerg = None
        for allergene, count in count_allergenes.items():
            if count > max_allerg_value:
                max_allerg_value = count
                max_allerg = allergene
        if max_allerg:
            if not max_allerg in allergene_ranking or max_allerg_value > allergene_ranking[max_allerg]:
                allergene_ranking[max_allerg] = max_allerg_value
                allergene_responsible[max_allerg] = ingredient
    
    all_ings = set()
    [all_ings.add(resp_ing) for _, resp_ing in allergene_responsible.items()]
    [without_allergenes.append(ing) for ing in appearance.keys() if ing not in all_ings]

    print(allergene_responsible)
    print(sum(appearance[ingredient] for ingredient in without_allergenes))

if __name__ == "__main__":
    data = get_input().splitlines()
    quiz1(data)